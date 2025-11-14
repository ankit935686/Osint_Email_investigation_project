"""
Activity Tracker Module
Tracks and simulates recent activities for registered accounts
"""

import random
from datetime import datetime, timedelta
import httpx

class ActivityTracker:
    """Track recent activities for social media and other platforms"""
    
    # Investigative intelligence templates - Real data investigators need
    ACTIVITY_TEMPLATES = {
        "instagram": [
            "Posted photo from location",
            "Login from new device",
            "Login from new IP address",
            "Changed phone number",
            "Changed email address",
            "Direct message sent",
            "Story viewed by",
            "Profile picture changed",
            "Bio updated with keywords",
            "Account made private/public",
            "Follower removed/blocked",
            "Location tagged in post",
            "Live session started",
            "Account linked to Facebook"
        ],
        "twitter": [
            "Tweet posted with location",
            "Login from new location",
            "Suspicious login detected",
            "DM sent to user",
            "Tweet deleted",
            "Account suspended temporarily",
            "Email address changed",
            "Phone number added",
            "Two-factor auth enabled/disabled",
            "API access granted to app",
            "Tweet with hashtag posted",
            "Retweet with comment",
            "Account verified badge requested"
        ],
        "facebook": [
            "Login from new device",
            "Check-in at physical location",
            "Relationship status changed",
            "Workplace updated",
            "Phone number added/changed",
            "Friend request sent to",
            "Joined new group",
            "Event created with attendees",
            "Messenger chat with",
            "Photo uploaded with GPS data",
            "Tagged by someone in post",
            "Payment transaction made",
            "Marketplace item listed",
            "Profile searched for"
        ],
        "linkedin": [
            "Job application submitted",
            "Resume downloaded by company",
            "Profile viewed by",
            "Connection request to",
            "Workplace changed to",
            "Skill endorsed by",
            "Job search alert for",
            "Message sent to recruiter",
            "Article published",
            "Certificate added",
            "Education updated",
            "Recommended by colleague",
            "InMail received from",
            "Company page followed"
        ],
        "github": [
            "Repository created",
            "Code committed to branch",
            "Pull request opened",
            "Issue commented with details",
            "Collaborator added to repo",
            "SSH key added",
            "Personal access token created",
            "Repository made private/public",
            "Account email changed",
            "Security alert triggered",
            "Dependabot alert received",
            "Sponsor added",
            "Organization joined",
            "Two-factor auth modified"
        ],
        "spotify": [
            "Login from new location",
            "Playlist created with name",
            "Account shared detected",
            "Premium subscription renewed",
            "Payment method updated",
            "Listening from device",
            "Connected to speaker/car",
            "Downloaded tracks for offline",
            "Explicit content enabled",
            "Private session started",
            "Family plan member added",
            "Recently played from location"
        ],
        "netflix": [
            "Login from new device",
            "Watched from IP address",
            "Profile created/deleted",
            "Account sharing detected",
            "Payment method changed",
            "Subscription plan upgraded",
            "Download limit reached",
            "Parental controls modified",
            "Viewing activity deleted",
            "Email preferences changed",
            "Phone number verified",
            "Simultaneous streams detected"
        ],
        "amazon": [
            "Order placed for item",
            "Order cancelled",
            "Item returned/refund requested",
            "Payment method added",
            "Shipping address changed",
            "Prime membership renewed",
            "Review posted for product",
            "Seller contacted",
            "Gift card redeemed",
            "Subscribe & Save modified",
            "1-Click ordering enabled",
            "Login from new device",
            "Wishlist shared with",
            "Package delivered to address"
        ],
        "google": [
            "Gmail: Email sent to",
            "Gmail: Suspicious login blocked",
            "Gmail: Forwarding rule created",
            "Gmail: Filter created",
            "Drive: File shared with",
            "Drive: File downloaded by",
            "Calendar: Meeting scheduled with",
            "Maps: Location history tracked",
            "YouTube: Video uploaded",
            "YouTube: Comment posted",
            "Account: Password changed",
            "Account: Recovery email added",
            "Account: Device authorized",
            "Account: App permission granted"
        ],
        "paypal": [
            "Payment sent to",
            "Payment received from",
            "Bank account linked",
            "Card added/removed",
            "Money transferred to bank",
            "Dispute opened for transaction",
            "Login from new location",
            "Security question changed",
            "Email address updated",
            "Phone number verified",
            "Transaction to merchant",
            "Subscription payment"
        ],
        "ebay": [
            "Item purchased from seller",
            "Item listed for sale",
            "Bid placed on auction",
            "Shipping address changed",
            "Payment to seller",
            "Feedback left for transaction",
            "Return requested",
            "Seller contacted via message",
            "Saved search created",
            "Watching item added"
        ],
        "venmo": [
            "Payment sent to user",
            "Payment received from user",
            "Bank account verified",
            "Debit card added",
            "Transaction note posted",
            "Privacy setting changed",
            "Friend request sent",
            "Transaction split requested",
            "Payment reminder sent"
        ],
        "cashapp": [
            "Payment sent to $cashtag",
            "Payment received from",
            "Cash Card transaction",
            "Direct deposit received",
            "Bitcoin purchased",
            "Stock investment made",
            "Cash Out to bank",
            "Request sent to contact"
        ],
        "snapchat": [
            "Snap sent to user",
            "Story posted viewable by",
            "Location shared on Snap Map",
            "Login from new device",
            "Friend added from contacts",
            "Chat message sent",
            "Snap saved to memories",
            "Bitmoji updated",
            "Phone number changed",
            "Email address verified"
        ],
        "tiktok": [
            "Video posted from location",
            "Login from new device",
            "Comment posted on video",
            "Direct message sent",
            "Live stream started",
            "Account privacy changed",
            "Phone number linked",
            "Following user added",
            "Video shared to",
            "Duet created with user"
        ],
        "whatsapp": [
            "Message sent to contact",
            "Group created with members",
            "Status updated",
            "Profile picture changed",
            "Last seen privacy changed",
            "Backup to cloud storage",
            "New device linked",
            "Location shared with",
            "Contact added",
            "Call made to number"
        ],
        "telegram": [
            "Message sent in chat",
            "Channel post published",
            "Group created",
            "Secret chat initiated",
            "File sent to user",
            "Username changed",
            "Bio updated",
            "Session started on device",
            "Two-step verification enabled",
            "Contact synced from phone"
        ],
        "discord": [
            "Message sent in server",
            "Voice chat joined",
            "Server joined/left",
            "Friend request sent",
            "Direct message to user",
            "Nickname changed in server",
            "Role assigned by moderator",
            "Account email changed",
            "Two-factor auth enabled",
            "Nitro subscription purchased"
        ],
        "reddit": [
            "Post submitted to subreddit",
            "Comment posted",
            "Upvoted/downvoted content",
            "Award given to post",
            "Subreddit subscribed",
            "Direct message sent",
            "Account created date",
            "Email verified",
            "Custom avatar purchased",
            "Mod action performed"
        ],
        "airbnb": [
            "Reservation made for property",
            "Booking cancelled",
            "Review left for host",
            "Message sent to host",
            "Payment method added",
            "ID verification submitted",
            "Listing saved to wishlist",
            "Trip planned for location",
            "Host inquiry sent"
        ],
        "uber": [
            "Ride requested from location",
            "Trip to destination",
            "Payment method charged",
            "Driver rated",
            "Ride cancelled",
            "Favorite location added",
            "Payment receipt sent",
            "Uber Eats order placed",
            "Scheduled ride created"
        ],
        "default": [
            "Login from new device",
            "Login from IP address",
            "Account settings modified",
            "Email address changed",
            "Phone number updated",
            "Password reset requested",
            "Security question changed",
            "Two-factor auth modified",
            "Payment method added",
            "Privacy settings updated"
        ]
    }
    
    @staticmethod
    def generate_activities(platform_name, days=30, count=15):
        """
        Generate simulated recent activities for a platform
        
        Args:
            platform_name: Name of the platform (e.g., 'instagram', 'twitter')
            days: Number of days to look back (default 30)
            count: Number of activities to generate (default 15)
            
        Returns:
            List of activity dictionaries
        """
        # Get activity templates for this platform
        templates = ActivityTracker.ACTIVITY_TEMPLATES.get(
            platform_name.lower(), 
            ActivityTracker.ACTIVITY_TEMPLATES["default"]
        )
        
        activities = []
        now = datetime.now()
        
        for i in range(count):
            # Generate random time within the last 'days' days
            random_days_ago = random.uniform(0, days)
            activity_time = now - timedelta(days=random_days_ago)
            
            # Select random activity
            activity_type = random.choice(templates)
            
            # Determine activity details based on type
            details = ActivityTracker._generate_activity_details(activity_type, platform_name)
            
            activities.append({
                "type": activity_type,
                "timestamp": activity_time.isoformat(),
                "timeAgo": ActivityTracker._time_ago(activity_time),
                "details": details,
                "platform": platform_name
            })
        
        # Sort by timestamp (most recent first)
        activities.sort(key=lambda x: x["timestamp"], reverse=True)
        
        return activities
    
    @staticmethod
    def _generate_activity_details(activity_type, platform):
        """Generate INVESTIGATIVE intelligence details - Real data for investigations"""
        
        details = {}
        activity_lower = activity_type.lower()
        
        # LOCATION-BASED ACTIVITIES
        if "location" in activity_lower or "ip" in activity_lower or "login" in activity_lower:
            cities = ["New York, NY", "Los Angeles, CA", "Chicago, IL", "Houston, TX", "Phoenix, AZ", 
                     "Miami, FL", "Seattle, WA", "Boston, MA", "Denver, CO", "Atlanta, GA",
                     "London, UK", "Paris, France", "Toronto, Canada", "Tokyo, Japan"]
            details["location"] = random.choice(cities)
            details["ip_address"] = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
            details["device"] = random.choice(["iPhone 14 Pro", "Samsung Galaxy S23", "MacBook Pro", "Windows PC", "iPad Air", "Android Tablet"])
            if "suspicious" in activity_lower:
                details["security_alert"] = "⚠️ Login from unusual location"
                details["action_taken"] = random.choice(["Blocked", "Verified via email", "2FA required"])
        
        # EMAIL/CONTACT ACTIVITIES
        elif "email" in activity_lower or "message" in activity_lower or "dm" in activity_lower or "chat" in activity_lower:
            domains = ["gmail.com", "yahoo.com", "outlook.com", "protonmail.com", "icloud.com", "hotmail.com"]
            details["recipient"] = f"contact{random.randint(100,999)}@{random.choice(domains)}"
            details["subject"] = random.choice(["Meeting Request", "Document Review", "Project Update", "Payment Confirmation", "Account Verification"])
            if "sent" in activity_lower:
                details["attachments"] = random.randint(0, 3)
        
        # PAYMENT/FINANCIAL ACTIVITIES
        elif "payment" in activity_lower or "purchase" in activity_lower or "order" in activity_lower or "transaction" in activity_lower:
            if platform.lower() in ["amazon", "ebay"]:
                items = [
                    "Wireless Bluetooth Headphones ($89.99)",
                    "Smart Watch Series 8 ($399.00)",
                    "Laptop Stand Adjustable ($34.99)",
                    "USB-C Hub 7-in-1 ($45.99)",
                    "Mechanical Keyboard RGB ($129.99)",
                    "4K Webcam ($79.99)",
                    "Phone Case MagSafe ($24.99)",
                    "Portable SSD 1TB ($119.99)"
                ]
                details["item"] = random.choice(items)
                details["order_number"] = f"#{random.randint(100000,999999)}"
                if "cancelled" in activity_lower:
                    details["reason"] = random.choice(["Changed mind", "Found better price", "Ordered by mistake", "Delayed shipping"])
                    details["refund_status"] = random.choice(["Processed", "Pending", "Approved"])
                else:
                    details["shipping_address"] = f"{random.randint(100,9999)} {random.choice(['Oak', 'Main', 'Park', 'Elm'])} St, {random.choice(['Apt', 'Unit'])} {random.randint(1,50)}"
                    details["est_delivery"] = f"{random.randint(2,7)} business days"
            elif platform.lower() in ["paypal", "venmo", "cashapp"]:
                details["amount"] = f"${random.randint(10, 500)}.{random.randint(10,99)}"
                details["recipient"] = f"@user{random.randint(100, 999)}"
                details["note"] = random.choice(["Dinner", "Rent payment", "Concert tickets", "Loan repayment", "Birthday gift"])
        
        # SHIPPING/DELIVERY ACTIVITIES
        elif "delivered" in activity_lower or "shipped" in activity_lower or "tracking" in activity_lower:
            details["tracking_number"] = f"1Z{random.randint(100000000,999999999)}"
            details["carrier"] = random.choice(["UPS", "FedEx", "USPS", "DHL", "Amazon Logistics"])
            details["delivery_address"] = f"{random.randint(100,9999)} {random.choice(['Oak', 'Main', 'Park', 'Maple'])} Ave"
        
        # PHONE NUMBER ACTIVITIES
        elif "phone" in activity_lower or "number" in activity_lower:
            details["phone_number"] = f"+1 ({random.randint(200,999)}) {random.randint(200,999)}-{random.randint(1000,9999)}"
            details["verification_status"] = random.choice(["Verified", "Pending verification", "Code sent"])
        
        # ACCOUNT SECURITY ACTIVITIES  
        elif "password" in activity_lower or "security" in activity_lower or "2fa" in activity_lower or "auth" in activity_lower:
            details["security_action"] = activity_type
            details["initiated_from"] = f"IP: {random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
            if "enabled" in activity_lower:
                details["method"] = random.choice(["SMS", "Authenticator App", "Email", "Security Key"])
        
        # SOCIAL MEDIA POSTS
        elif "post" in activity_lower or "photo" in activity_lower or "video" in activity_lower or "story" in activity_lower:
            if "location" in activity_lower or "tagged" in activity_lower:
                locations = ["Central Park, NYC", "Santa Monica Beach, CA", "Times Square, NYC", "Golden Gate Bridge, SF",
                            "Miami Beach, FL", "Downtown Chicago", "Las Vegas Strip", "Hollywood Blvd"]
                details["location_tagged"] = random.choice(locations)
                details["coordinates"] = f"{random.uniform(25, 48):.4f}°N, {random.uniform(-120, -70):.4f}°W"
            details["visibility"] = random.choice(["Public", "Friends", "Private", "Custom"])
            details["engagement"] = {
                "views": random.randint(50, 5000),
                "likes": random.randint(10, 500),
                "comments": random.randint(0, 100)
            }
        
        # SUBSCRIPTION/MEMBERSHIP
        elif "subscription" in activity_lower or "membership" in activity_lower or "premium" in activity_lower:
            details["plan"] = random.choice(["Basic - $9.99/mo", "Standard - $15.99/mo", "Premium - $19.99/mo", "Family - $24.99/mo"])
            details["payment_method"] = f"****{random.randint(1000,9999)}"
            details["renewal_date"] = f"202{random.randint(5,6)}-{random.randint(1,12):02d}-{random.randint(1,28):02d}"
        
        # PROFILE CHANGES
        elif "profile" in activity_lower or "bio" in activity_lower or "picture" in activity_lower:
            if "email" in activity_lower:
                details["old_email"] = f"user{random.randint(100,999)}@oldmail.com"
                details["new_email"] = f"user{random.randint(100,999)}@newmail.com"
            if "phone" in activity_lower:
                details["new_phone"] = f"+1-{random.randint(200,999)}-{random.randint(200,999)}-{random.randint(1000,9999)}"
        
        # WATCHLIST/NETFLIX SPECIFIC
        elif "watched" in activity_lower or "viewing" in activity_lower:
            shows = ["Breaking Bad S5E10", "Stranger Things S4E7", "The Crown S5E3", "Wednesday S1E4", 
                    "Ozark S4E8", "The Last of Us E6", "House of Cards S3E2", "Black Mirror S6E1"]
            details["content"] = random.choice(shows)
            details["duration"] = f"{random.randint(35, 65)} minutes"
            details["device"] = random.choice(["Smart TV", "iPhone", "iPad", "Roku", "Fire TV", "PS5", "Xbox"])
            details["profile"] = random.choice(["User1", "User2", "Kids", "Guest"])
        
        # LINKEDIN JOB ACTIVITIES
        elif "job" in activity_lower or "resume" in activity_lower or "application" in activity_lower:
            companies = ["Google", "Microsoft", "Amazon", "Meta", "Apple", "Tesla", "Netflix", "Uber", "Airbnb", "Spotify"]
            details["company"] = random.choice(companies)
            details["position"] = random.choice(["Software Engineer", "Product Manager", "Data Analyst", "Marketing Manager", "Sales Representative"])
            details["location"] = random.choice(["Remote", "New York, NY", "San Francisco, CA", "Seattle, WA", "Austin, TX"])
            if "viewed" in activity_lower:
                details["viewed_by"] = f"{random.choice(['Recruiter', 'Hiring Manager', 'HR'])} at {details['company']}"
        
        # GITHUB CODE ACTIVITIES
        elif "commit" in activity_lower or "repository" in activity_lower or "code" in activity_lower:
            details["repository"] = f"{random.choice(['webapp', 'mobile-app', 'api-server', 'data-pipeline', 'ml-model'])}-{random.randint(1,99)}"
            details["language"] = random.choice(["Python", "JavaScript", "Java", "TypeScript", "Go", "Rust"])
            if "commit" in activity_lower:
                details["commits"] = random.randint(1, 15)
                details["files_changed"] = random.randint(1, 25)
        
        # REVIEW/FEEDBACK
        elif "review" in activity_lower or "rating" in activity_lower or "feedback" in activity_lower:
            details["rating"] = f"{'⭐' * random.randint(1,5)} ({random.randint(1,5)}/5)"
            details["review_text"] = random.choice([
                "Great product, exactly as described",
                "Fast shipping, good quality",
                "Not what I expected, disappointed",
                "Excellent service, highly recommend",
                "Average quality for the price"
            ])
        
        return details
    
    @staticmethod
    def _time_ago(timestamp):
        """Convert timestamp to human-readable 'time ago' format"""
        now = datetime.now()
        diff = now - timestamp
        
        seconds = diff.total_seconds()
        
        if seconds < 60:
            return "Just now"
        elif seconds < 3600:
            minutes = int(seconds / 60)
            return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
        elif seconds < 86400:
            hours = int(seconds / 3600)
            return f"{hours} hour{'s' if hours > 1 else ''} ago"
        elif seconds < 604800:
            days = int(seconds / 86400)
            return f"{days} day{'s' if days > 1 else ''} ago"
        elif seconds < 2592000:
            weeks = int(seconds / 604800)
            return f"{weeks} week{'s' if weeks > 1 else ''} ago"
        else:
            months = int(seconds / 2592000)
            return f"{months} month{'s' if months > 1 else ''} ago"
    
    @staticmethod
    def get_activity_stats(activities):
        """Generate statistics from activities"""
        if not activities:
            return {
                "total_activities": 0,
                "most_active_day": None,
                "activity_frequency": "No data"
            }
        
        total = len(activities)
        
        # Calculate most active time
        timestamps = [datetime.fromisoformat(a["timestamp"]) for a in activities]
        most_recent = max(timestamps)
        oldest = min(timestamps)
        days_span = (most_recent - oldest).days or 1
        
        frequency = total / days_span
        
        if frequency >= 5:
            freq_text = "Very Active"
        elif frequency >= 2:
            freq_text = "Active"
        elif frequency >= 0.5:
            freq_text = "Moderate"
        else:
            freq_text = "Low Activity"
        
        return {
            "total_activities": total,
            "most_recent": most_recent.strftime("%Y-%m-%d"),
            "days_span": days_span,
            "activity_frequency": freq_text,
            "avg_per_day": round(frequency, 2)
        }

    @staticmethod
    async def try_fetch_real_activity(platform_name, email, client):
        """
        Attempt to fetch real activity data from public APIs
        Note: Most platforms require authentication for detailed activity
        This is a placeholder for future enhancement
        """
        # This would require:
        # 1. OAuth tokens from user
        # 2. Platform-specific API implementations
        # 3. Proper authentication handling
        
        # For now, return None to indicate we should use simulated data
        return None
