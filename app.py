from flask import Flask, render_template, request, jsonify
import asyncio
import trio
import httpx
from holehe.core import get_functions, import_submodules
from holehe.activity_tracker import ActivityTracker
from holehe.osint_tools import OSINTTools
import json
import threading
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Global variable to store results
results_cache = {}

def run_holehe_async(email):
    """Run holehe asynchronously and store results"""
    async def main():
        try:
            # Import all modules
            modules = import_submodules("holehe.modules")
            websites = get_functions(modules)
            
            # Initialize client with timeout
            client = httpx.AsyncClient(timeout=30.0)
            out = []
            
            # Process all websites concurrently using trio with proper error handling
            total_websites = len(websites)
            
            async def safe_website_check(website, email, client, out):
                """Wrapper to handle errors in individual website checks"""
                try:
                    await website(email, client, out)
                except Exception as e:
                    # If a website check fails, add error result
                    name = website.__name__ if hasattr(website, '__name__') else 'unknown'
                    logger.warning(f"Error checking {name}: {str(e)}")
            
            # Use trio nursery with error-wrapped calls
            async with trio.open_nursery() as nursery:
                for website in websites:
                    nursery.start_soon(safe_website_check, website, email, client, out)
            
            await client.aclose()
            
            logger.info(f"Processed {len(out)}/{total_websites} websites for {email}")
            
            # Process results
            processed_results = []
            rate_limited_sites = []
            error_sites = []
            
            for result in out:
                if isinstance(result, dict):
                    site_result = {
                        'name': result.get('name', 'Unknown'),
                        'exists': result.get('exists', False),
                        'rateLimit': result.get('rateLimit', False),
                        'error': result.get('error', False),
                        'emailrecovery': result.get('emailrecovery', ''),
                        'phoneNumber': result.get('phoneNumber', ''),
                        'others': result.get('others', '')
                    }
                    processed_results.append(site_result)
                    
                    # Track rate limited and error sites
                    if site_result['rateLimit']:
                        rate_limited_sites.append(site_result['name'])
                    if site_result.get('error', False):
                        error_sites.append(site_result['name'])
            
            # Count found accounts for logging
            found_results = [r for r in processed_results if r.get('exists', False)]
            logger.info(f"Found {len(found_results)} accounts with exists=True")
            logger.info(f"Rate limited sites: {len(rate_limited_sites)}")
            logger.info(f"Error sites: {len(error_sites)}")
            
            for result in found_results:
                logger.info(f"Found account: {result.get('name', 'Unknown')} - exists: {result.get('exists')}")
            
            # Store results in cache with statistics
            results_cache[email] = {
                'status': 'completed',
                'results': processed_results,
                'timestamp': datetime.now().isoformat(),
                'total_sites': len(processed_results),
                'found_accounts': len(found_results),
                'rate_limited_count': len(rate_limited_sites),
                'error_count': len(error_sites),
                'success_rate': f"{((len(processed_results) - len(rate_limited_sites) - len(error_sites)) / len(processed_results) * 100):.1f}%"
            }
            logger.info(f"Analysis completed for {email}: {len(processed_results)} results, {len(found_results)} found, {len(rate_limited_sites)} rate limited, {len(error_sites)} errors")
            
        except Exception as e:
            logger.error(f"Error processing email {email}: {str(e)}")
            results_cache[email] = {
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    # Run the async function
    trio.run(main)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_email', methods=['POST'])
def check_email():
    data = request.get_json()
    email = data.get('email', '').strip()
    
    if not email:
        return jsonify({'error': 'Email is required'}), 400
    
    # Check if we already have results for this email
    if email in results_cache:
        return jsonify(results_cache[email])
    
    # Mark as processing
    results_cache[email] = {
        'status': 'processing',
        'timestamp': datetime.now().isoformat()
    }
    
    # Start processing in background thread
    thread = threading.Thread(target=run_holehe_async, args=(email,))
    thread.daemon = True
    thread.start()
    
    return jsonify({'status': 'processing', 'message': 'Analysis started'})

@app.route('/get_results/<email>')
def get_results(email):
    if email in results_cache:
        result = results_cache[email]
        logger.info(f"Returning results for {email}: {result['status']}")
        return jsonify(result)
    else:
        return jsonify({'error': 'No results found for this email'}), 404

@app.route('/clear_cache', methods=['POST'])
def clear_cache():
    results_cache.clear()
    return jsonify({'message': 'Cache cleared successfully'})

@app.route('/get_activities/<platform>/<email>')
def get_activities(platform, email):
    """
    Get recent activities for a specific platform
    Returns simulated activity data based on the platform
    """
    try:
        # Generate activities for the last 30 days
        activities = ActivityTracker.generate_activities(platform, days=30, count=20)
        
        # Get statistics
        stats = ActivityTracker.get_activity_stats(activities)
        
        return jsonify({
            'status': 'success',
            'platform': platform,
            'email': email,
            'activities': activities,
            'stats': stats,
            'note': 'Activities are simulated based on typical platform usage patterns. Real-time tracking requires platform API authentication.'
        })
    except Exception as e:
        logger.error(f"Error fetching activities for {platform}: {str(e)}")
        return jsonify({
            'status': 'error',
            'error': str(e)
        }), 500

@app.route('/osint/username_variations/<email>')
def username_variations(email):
    """Generate username variations for finding accounts on other platforms"""
    try:
        variations = OSINTTools.generate_username_variations(email)
        return jsonify({
            'status': 'success',
            'email': email,
            'data': variations
        })
    except Exception as e:
        logger.error(f"Error generating username variations: {str(e)}")
        return jsonify({'status': 'error', 'error': str(e)}), 500

@app.route('/osint/email_analysis/<email>')
def email_analysis(email):
    """Analyze email pattern for intelligence"""
    try:
        analysis = OSINTTools.analyze_email_pattern(email)
        return jsonify({
            'status': 'success',
            'data': analysis
        })
    except Exception as e:
        logger.error(f"Error analyzing email: {str(e)}")
        return jsonify({'status': 'error', 'error': str(e)}), 500

@app.route('/osint/breach_check/<email>')
def breach_check(email):
    """Check if email appears in known data breaches"""
    try:
        breaches = OSINTTools.check_data_breaches(email)
        return jsonify({
            'status': 'success',
            'data': breaches
        })
    except Exception as e:
        logger.error(f"Error checking breaches: {str(e)}")
        return jsonify({'status': 'error', 'error': str(e)}), 500

@app.route('/osint/related_emails/<email>')
def related_emails(email):
    """Generate possible related email addresses"""
    try:
        related = OSINTTools.generate_related_emails(email)
        return jsonify({
            'status': 'success',
            'data': related
        })
    except Exception as e:
        logger.error(f"Error generating related emails: {str(e)}")
        return jsonify({'status': 'error', 'error': str(e)}), 500

@app.route('/osint/domain_analysis/<email>')
def domain_analysis(email):
    """Analyze email domain for intelligence"""
    try:
        analysis = OSINTTools.analyze_domain(email)
        return jsonify({
            'status': 'success',
            'data': analysis
        })
    except Exception as e:
        logger.error(f"Error analyzing domain: {str(e)}")
        return jsonify({'status': 'error', 'error': str(e)}), 500

@app.route('/osint/full_report/<email>')
def full_osint_report(email):
    """Generate comprehensive OSINT report"""
    try:
        # Get found platforms from cache if available
        found_platforms = []
        if email in results_cache and 'results' in results_cache[email]:
            found_platforms = [
                r['name'] for r in results_cache[email]['results'] 
                if r.get('exists', False)
            ]
        
        report = OSINTTools.generate_osint_report(email, found_platforms)
        return jsonify({
            'status': 'success',
            'data': report
        })
    except Exception as e:
        logger.error(f"Error generating OSINT report: {str(e)}")
        return jsonify({'status': 'error', 'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 