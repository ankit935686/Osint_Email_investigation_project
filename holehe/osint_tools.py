"""
OSINT Tools - Real investigative features that work with email addresses
These tools provide actual useful intelligence without requiring unauthorized access
"""

import re
import hashlib
import requests
from datetime import datetime
import json


class OSINTTools:
    """Collection of real OSINT tools for email investigation"""
    
    @staticmethod
    def generate_username_variations(email):
        """
        Generate possible username variations from email
        Useful for finding same person on other platforms
        """
        local_part = email.split('@')[0]
        domain = email.split('@')[1]
        
        variations = {
            'original': local_part,
            'variations': []
        }
        
        # Common variations
        variations['variations'].append(local_part.replace('.', ''))  # Remove dots
        variations['variations'].append(local_part.replace('_', ''))  # Remove underscores
        variations['variations'].append(local_part.replace('.', '_'))  # Dots to underscores
        variations['variations'].append(local_part.replace('_', '.'))  # Underscores to dots
        
        # Add numbers if not present
        if not any(char.isdigit() for char in local_part):
            for num in ['123', '01', '007', '99', '21']:
                variations['variations'].append(local_part + num)
        
        # Remove numbers if present
        no_numbers = re.sub(r'\d+', '', local_part)
        if no_numbers != local_part:
            variations['variations'].append(no_numbers)
        
        # Capitalize variations
        variations['variations'].append(local_part.capitalize())
        variations['variations'].append(local_part.upper())
        variations['variations'].append(local_part.lower())
        
        # Split by separators and recombine
        parts = re.split(r'[._-]', local_part)
        if len(parts) > 1:
            variations['variations'].append(''.join(parts))  # Combined
            variations['variations'].append('_'.join(parts))  # With underscores
            variations['variations'].append('.'.join(parts))  # With dots
            variations['variations'].append('-'.join(parts))  # With hyphens
        
        # Remove duplicates and original
        variations['variations'] = list(set(variations['variations']))
        variations['variations'] = [v for v in variations['variations'] if v != local_part]
        
        return variations
    
    @staticmethod
    def analyze_email_pattern(email):
        """
        Analyze email structure for intelligence
        Can reveal naming patterns, organization info, etc.
        """
        local_part = email.split('@')[0]
        domain = email.split('@')[1]
        
        analysis = {
            'email': email,
            'local_part': local_part,
            'domain': domain,
            'insights': []
        }
        
        # Check for name patterns
        if '.' in local_part:
            parts = local_part.split('.')
            if len(parts) == 2:
                analysis['insights'].append({
                    'type': 'naming_pattern',
                    'icon': '👤',
                    'finding': 'Possible first.last name format',
                    'value': f'{parts[0].capitalize()} {parts[1].capitalize()}',
                    'investigative_value': 'Real name likely revealed'
                })
        
        # Check for birth year
        year_match = re.search(r'(19|20)\d{2}', local_part)
        if year_match:
            year = int(year_match.group())
            age = datetime.now().year - year
            analysis['insights'].append({
                'type': 'birth_year',
                'icon': '📅',
                'finding': 'Possible birth year detected',
                'value': f'{year} (Age ~{age})',
                'investigative_value': 'Can narrow down identity'
            })
        
        # Check for organizational email
        org_patterns = ['corp', 'company', 'inc', 'ltd', 'org', 'edu', 'gov', 'mil']
        for pattern in org_patterns:
            if pattern in domain:
                analysis['insights'].append({
                    'type': 'organization',
                    'icon': '🏢',
                    'finding': 'Organizational email detected',
                    'value': f'{pattern.upper()} domain',
                    'investigative_value': 'Professional/institutional affiliation'
                })
                break
        
        # Check for common email providers
        providers = {
            'gmail.com': 'Google (Personal)',
            'yahoo.com': 'Yahoo (Personal)',
            'outlook.com': 'Microsoft Outlook',
            'hotmail.com': 'Microsoft Hotmail',
            'protonmail.com': 'ProtonMail (Privacy-focused)',
            'proton.me': 'Proton (Privacy-focused)',
            'icloud.com': 'Apple iCloud',
            'aol.com': 'AOL (Older generation)'
        }
        
        if domain in providers:
            analysis['insights'].append({
                'type': 'email_provider',
                'icon': '📧',
                'finding': 'Email provider identified',
                'value': providers[domain],
                'investigative_value': 'Reveals technology preference'
            })
        
        # Check for numbers
        numbers = re.findall(r'\d+', local_part)
        if numbers:
            analysis['insights'].append({
                'type': 'numbers',
                'icon': '🔢',
                'finding': 'Numbers in email',
                'value': ', '.join(numbers),
                'investigative_value': 'Could be birth year, age, or favorite number'
            })
        
        # Check length and complexity
        if len(local_part) < 5:
            analysis['insights'].append({
                'type': 'simplicity',
                'icon': '⚡',
                'finding': 'Short email address',
                'value': f'Only {len(local_part)} characters',
                'investigative_value': 'Early adopter or premium account'
            })
        
        return analysis
    
    @staticmethod
    def check_data_breaches(email):
        """
        Check if email appears in REAL data breaches using LeakCheck.io API
        This pulls LIVE breach data - 100% dynamic and real-time!
        API Key: b6c0aba19e5763a15e2d5799f1e3dbeeb46aa1fa
        """
        # LeakCheck.io API Configuration
        LEAKCHECK_API_KEY = "b6c0aba19e5763a15e2d5799f1e3dbeeb46aa1fa"
        
        breaches = {
            'email': email,
            'checked': True,
            'breaches_found': [],
            'total_breaches': 0,
            'risk_level': 'Unknown',
            'source': 'LeakCheck.io API - Real-time breach database',
            'note': ''
        }
        
        try:
            # LeakCheck.io Public API endpoint
            url = "https://leakcheck.io/api/public"
            headers = {
                'X-API-Key': LEAKCHECK_API_KEY,
                'Content-Type': 'application/json'
            }
            params = {
                'check': email,
                'type': 'email'
            }
            
            # Make REAL API request to LeakCheck
            print(f"🔍 Checking breaches for {email} using LeakCheck.io...")
            response = requests.get(url, headers=headers, params=params, timeout=15)
            
            print(f"📡 API Response Status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print(f"📊 API Response: {data}")
                
                # LeakCheck returns actual breach data
                if data.get('success') and data.get('found', 0) > 0:
                    sources = data.get('sources', [])
                    
                    print(f"⚠️ Found {len(sources)} breach sources!")
                    
                    for source in sources:
                        # Extract breach information
                        breach_info = {
                            'name': source.get('name', 'Unknown Breach'),
                            'date': source.get('date', 'Unknown Date'),
                            'data_exposed': ', '.join(source.get('fields', [])) if source.get('fields') else 'Multiple fields',
                            'severity': 'Critical' if len(source.get('fields', [])) > 5 else 'High',
                            'recommendation': f"⚠️ Password compromised in {source.get('name', 'this breach')}! Change immediately and enable 2FA!",
                            'source': 'LeakCheck.io (Live Data)'
                        }
                        breaches['breaches_found'].append(breach_info)
                    
                    breaches['total_breaches'] = data.get('found', len(sources))
                    breaches['risk_level'] = 'Critical' if breaches['total_breaches'] > 3 else 'High'
                    breaches['note'] = f"🚨 CRITICAL: Email found in {breaches['total_breaches']} REAL data breaches! (Live from LeakCheck.io)"
                    
                else:
                    # No breaches found - GOOD NEWS!
                    breaches['total_breaches'] = 0
                    breaches['risk_level'] = 'Low'
                    breaches['note'] = '✅ Excellent! Email not found in any known data breaches (Verified by LeakCheck.io)'
                    print("✅ No breaches found - email is clean!")
                    
            elif response.status_code == 404:
                # Email not found in breach database
                breaches['total_breaches'] = 0
                breaches['risk_level'] = 'Low'
                breaches['note'] = '✅ Good news! Email not found in any data breaches'
                print("✅ 404 - Email not in breach database")
                
            else:
                # API error
                breaches['note'] = f'⚠️ LeakCheck API returned status {response.status_code}. Try again later.'
                breaches['risk_level'] = 'Unknown'
                print(f"⚠️ API Error: Status {response.status_code}")
                print(f"Response: {response.text}")
                
        except requests.exceptions.Timeout:
            breaches['note'] = '⚠️ LeakCheck API timeout - service may be experiencing high load'
            breaches['risk_level'] = 'Unknown'
            print("⏱️ API Timeout")
            
        except requests.exceptions.ConnectionError:
            breaches['note'] = '⚠️ Cannot connect to LeakCheck API - check internet connection'
            breaches['risk_level'] = 'Unknown'
            print("🔌 Connection Error")
            
        except Exception as e:
            breaches['note'] = f'⚠️ Error checking breaches: {str(e)}'
            breaches['risk_level'] = 'Unknown'
            print(f"❌ Error: {str(e)}")
        
        return breaches
    
    @staticmethod
    def generate_related_emails(email):
        """
        Generate possible related email addresses
        Useful for finding alternative contact methods
        """
        local_part = email.split('@')[0]
        domain = email.split('@')[1]
        
        related = {
            'original': email,
            'possible_alternatives': []
        }
        
        # Common alternative domains
        common_domains = [
            'gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com',
            'icloud.com', 'protonmail.com', 'proton.me'
        ]
        
        # Add same username on different providers
        for alt_domain in common_domains:
            if alt_domain != domain:
                related['possible_alternatives'].append({
                    'email': f'{local_part}@{alt_domain}',
                    'reason': 'Same username, different provider',
                    'likelihood': 'Medium'
                })
        
        # Add variations with numbers
        if not any(char.isdigit() for char in local_part):
            for num in ['01', '123', '99']:
                related['possible_alternatives'].append({
                    'email': f'{local_part}{num}@{domain}',
                    'reason': 'Username with common numbers',
                    'likelihood': 'Medium'
                })
        
        # Add professional variations
        if '.' not in local_part and '_' not in local_part:
            # Try to split name
            if len(local_part) > 6:
                mid = len(local_part) // 2
                related['possible_alternatives'].append({
                    'email': f'{local_part[:mid]}.{local_part[mid:]}@{domain}',
                    'reason': 'Professional name format',
                    'likelihood': 'Low'
                })
        
        return related
    
    @staticmethod
    def analyze_domain(email):
        """
        Analyze the email domain for intelligence
        """
        domain = email.split('@')[1]
        
        analysis = {
            'domain': domain,
            'email': email,
            'insights': []
        }
        
        # Check TLD
        tld = domain.split('.')[-1]
        tld_info = {
            'com': {'type': 'Commercial', 'origin': 'International'},
            'org': {'type': 'Organization', 'origin': 'International'},
            'edu': {'type': 'Educational', 'origin': 'US-based'},
            'gov': {'type': 'Government', 'origin': 'US-based'},
            'mil': {'type': 'Military', 'origin': 'US Military'},
            'co': {'type': 'Commercial', 'origin': 'Colombia/Company'},
            'io': {'type': 'Tech Startup', 'origin': 'British Indian Ocean'},
            'ai': {'type': 'AI/Tech', 'origin': 'Anguilla'},
            'uk': {'type': 'United Kingdom', 'origin': 'UK'},
            'de': {'type': 'Germany', 'origin': 'Germany'},
            'fr': {'type': 'France', 'origin': 'France'},
            'ru': {'type': 'Russia', 'origin': 'Russia'},
            'in': {'type': 'India', 'origin': 'India'},
        }
        
        if tld in tld_info:
            analysis['insights'].append({
                'type': 'tld',
                'icon': '🌐',
                'finding': 'Domain Type',
                'value': f"{tld_info[tld]['type']} ({tld_info[tld]['origin']})",
                'investigative_value': 'Reveals geographic or organizational context'
            })
        
        # Check for suspicious patterns
        suspicious_keywords = ['temp', 'disposable', 'fake', 'test', 'spam']
        for keyword in suspicious_keywords:
            if keyword in domain:
                analysis['insights'].append({
                    'type': 'suspicious',
                    'icon': '⚠️',
                    'finding': 'Suspicious Domain',
                    'value': f'Contains "{keyword}"',
                    'investigative_value': 'May be temporary or fake email'
                })
        
        # Check for custom domain (not common provider)
        common_providers = ['gmail', 'yahoo', 'outlook', 'hotmail', 'icloud', 'protonmail', 'aol']
        is_custom = not any(provider in domain for provider in common_providers)
        
        if is_custom:
            analysis['insights'].append({
                'type': 'custom_domain',
                'icon': '🏢',
                'finding': 'Custom Domain',
                'value': 'Not a common email provider',
                'investigative_value': 'Likely business/organization email'
            })
        
        return analysis
    
    @staticmethod
    def get_email_metadata(email):
        """
        Generate comprehensive email metadata report
        """
        local_part = email.split('@')[0]
        domain = email.split('@')[1]
        
        metadata = {
            'email': email,
            'created_at': datetime.now().isoformat(),
            'components': {
                'local_part': local_part,
                'domain': domain,
                'tld': domain.split('.')[-1],
                'domain_parts': len(domain.split('.'))
            },
            'statistics': {
                'total_length': len(email),
                'local_part_length': len(local_part),
                'has_numbers': any(char.isdigit() for char in local_part),
                'has_special_chars': bool(re.search(r'[._-]', local_part)),
                'number_count': len(re.findall(r'\d', local_part)),
                'special_char_count': len(re.findall(r'[._-]', local_part))
            },
            'hashes': {
                'md5': hashlib.md5(email.encode()).hexdigest(),
                'sha256': hashlib.sha256(email.encode()).hexdigest()[:16] + '...'
            }
        }
        
        return metadata
    
    @staticmethod
    def generate_osint_report(email, found_platforms):
        """
        Generate comprehensive OSINT report
        """
        report = {
            'email': email,
            'generated_at': datetime.now().isoformat(),
            'summary': {
                'total_platforms_found': len(found_platforms),
                'platform_categories': {}
            },
            'username_variations': OSINTTools.generate_username_variations(email),
            'email_analysis': OSINTTools.analyze_email_pattern(email),
            'domain_analysis': OSINTTools.analyze_domain(email),
            'breach_check': OSINTTools.check_data_breaches(email),
            'related_emails': OSINTTools.generate_related_emails(email),
            'metadata': OSINTTools.get_email_metadata(email)
        }
        
        # Categorize found platforms
        categories = {
            'Social Media': ['instagram', 'facebook', 'twitter', 'snapchat', 'tiktok'],
            'Professional': ['linkedin', 'github', 'stackoverflow'],
            'Shopping': ['amazon', 'ebay', 'etsy'],
            'Streaming': ['netflix', 'spotify', 'youtube'],
            'Communication': ['gmail', 'yahoo', 'outlook', 'discord', 'telegram'],
            'Financial': ['paypal', 'venmo', 'cashapp']
        }
        
        for category, platforms in categories.items():
            count = sum(1 for p in found_platforms if any(x in p.lower() for x in platforms))
            if count > 0:
                report['summary']['platform_categories'][category] = count
        
        return report
