# 📧 Holehe Email Account Finder - Web Application

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-Educational-yellow.svg)]()
[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()

> A comprehensive **Email OSINT (Open Source Intelligence)** tool that checks if an email address is registered across **120+ popular websites** with professional intelligence analysis tools. No API keys required - works with just the email address!



## 🚀 Quick Start (5 Minutes)

### Prerequisites
- Python 3.8+ ([Download](https://www.python.org/downloads/))
- Internet connection
- Modern web browser

### Installation

```bash
# Navigate to project directory
cd holehe

# Install dependencies (takes ~2-3 minutes)
pip install -r requirements.txt

# Run the application
python app.py

# Open browser and go to:
# http://localhost:5000
```

### Quick Test
1. Enter email: `test@gmail.com`
2. Click "Search"
3. Wait 10-30 seconds
4. View results across 120+ websites!

---

## 📋 Table of Contents

- [Features](#-features)
- [OSINT Intelligence Tools](#-osint-intelligence-tools)
- [Technology Stack](#-technology-stack)
- [Installation Guide](#-installation-guide)
- [Usage Guide](#-usage-guide)
- [API Documentation](#-api-documentation)
- [Supported Platforms](#-supported-platforms)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Security & Ethics](#-security--ethics)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### 🔍 Core Capabilities

- **120+ Website Coverage** - Check across 23 different categories (social media, shopping, forums, etc.)
- **Real-time Processing** - Asynchronous checks with live progress updates
- **Modern Web Interface** - Beautiful, responsive UI with gradient designs and glassmorphism
- **Smart Filtering** - Filter results by status (Found, Not Found, Rate Limited, Errors)
- **CSV Export** - Download results for further analysis
- **Session Caching** - Fast result retrieval with background processing

### 🆕 Professional OSINT Intelligence Tools ⭐

**These are REAL investigative tools used by cybersecurity professionals!**

#### 1. 📧 Email Pattern Analysis
**Extracts intelligence from email structure:**
- Real name identification (`john.smith` → "John Smith")
- Birth year detection (`email1990` → Age ~35)
- Email provider type (personal vs organizational)
- Naming pattern recognition

**Example Output:**
```
Email: john.smith1985@company.com

✓ Naming Pattern: Likely "John Smith"
✓ Birth Year: 1985 (Age ~40)
✓ Organizational Email: Corporate domain
✓ Numbers: Could indicate birth year
```

#### 2. 👤 Username Variations Generator (MOST USEFUL!)
**Generates 20+ username alternatives for cross-platform searching:**
- Removes/adds numbers, dots, underscores, hyphens
- Different capitalizations and combinations
- **Use Case**: Search these variations on Twitter, Instagram, Reddit, GitHub, gaming sites to find the same person!

**Example Output:**
```
Original: john.smith123

Variations:
✓ johnsmith (no numbers)
✓ john_smith
✓ john-smith  
✓ JohnSmith
✓ john.smith
✓ johnsmith01
✓ smithjohn
... and 13 more variations
```

#### 3. 🔓 Data Breach Checker
**Checks if email appeared in known data breaches:**
- Shows breach details (dates, exposed data)
- Security recommendations
- Risk level assessment

**Example Output:**
```
Risk Level: HIGH
Total Breaches: 2

1. LinkedIn Breach (2021)
   Records: 700M users
   Data Exposed: Emails, names, phone numbers
   Recommendation: Change LinkedIn password immediately

2. Adobe Breach (2013)
   Records: 153M users
   Data Exposed: Emails, passwords
   Recommendation: Change all similar passwords
```

#### 4. 📨 Related Emails Generator
**Suggests possible alternative email addresses:**
- Same username on different providers (Gmail, Yahoo, Outlook)
- Professional email variations
- **Use Case**: Search these alternative emails to find more accounts!

**Example Output:**
```
Original: john.smith@gmail.com

Possible Alternatives:
✓ john.smith@yahoo.com (Medium likelihood)
✓ john.smith@outlook.com (Medium likelihood)
✓ john.smith01@gmail.com (Medium likelihood)
✓ john.smith@company.com (Professional variation)
```

#### 5. 🌐 Domain Intelligence Analysis
**Analyzes email domain for context:**
- TLD type identification (geographic origin)
- Custom vs common provider detection
- Business/personal/educational classification
- Suspicious domain flagging

**Example Output:**
```
Domain: example.co.uk

✓ Domain Type: United Kingdom (UK)
✓ Custom Domain: Not a common provider
✓ Likely business/organization email
✓ Geographic Context: British origin
```

---

## 🎯 OSINT Intelligence Tools

### What Makes This Professional?

✅ **No API Keys Required** - All tools work with just the email address
✅ **Legal & Ethical** - Uses pattern analysis, no unauthorized access
✅ **Immediately Useful** - Generated username variations can be searched right away
✅ **Professional Grade** - Same methods used by cybersecurity investigators
✅ **Educational Value** - Teaches real investigation techniques

### Real Investigation Workflow Example

**Target Email:** `suspicious.person1990@gmail.com`

**Step 1: Initial Search**
```
Found on: Instagram ✓, Twitter ✓, LinkedIn ✓, GitHub ✓
```

**Step 2: OSINT Analysis**
- Birth Year: 1990 (Age ~35)
- Email Provider: Gmail (Personal)
- Found in LinkedIn breach (2021)
- Phone number may be exposed

**Step 3: Username Variations**
```
Search these on other platforms:
- suspiciousperson
- suspicious_person
- suspicious.person
```

**Step 4: Extended Results**
- Found "suspiciousperson" on Reddit ✓
- Found "suspicious_person" on Discord ✓
- Found same username on gaming platforms ✓

**Step 5: Alternative Emails**
```
suspicious.person@gmail.com
- Found on Facebook ✓
- Found on PayPal ✓
```

### Why These Tools Matter

| Feature | Traditional Email Checker | Our OSINT Tools |
|---------|--------------------------|-----------------|
| Legal | ✅ Yes | ✅ Yes |
| Real Data | ❌ Limited | ✅ Actionable |
| Professional Use | ❌ Basic | ✅ Advanced |
| Educational Value | ⚠️ Low | ✅ High |
| No Auth Required | ✅ Yes | ✅ Yes |

---

## 🛠️ Technology Stack

### Backend
- **Flask 2.3.3** - Python web framework
- **httpx 0.27.0** - Modern async HTTP client
- **trio 0.30.0** - Async/await concurrency library
- **BeautifulSoup4** - HTML parsing and web scraping

### Frontend
- **HTML5/CSS3** - Structure and styling
- **Bootstrap 5.1.3** - Responsive UI framework
- **Font Awesome 6.0** - Icon library
- **JavaScript ES6+** - Interactive functionality

### Other Libraries
- **termcolor** - Terminal colored output
- **tqdm** - Progress bars
- **colorama** - Cross-platform colors

---

## 📥 Installation Guide

### Method 1: Quick Setup

```bash
# Clone or download the project
cd holehe

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### Method 2: Direct Installation

```bash
# Install all dependencies directly
pip install flask==2.3.3 httpx==0.27.0 trio==0.30.0 bs4 termcolor tqdm colorama

# Run the application
python app.py
```

### Access the Application

Open your browser and navigate to:
```
http://localhost:5000
```

---

## 📖 Usage Guide

### Web Interface

#### 1. Basic Email Search
1. **Enter Email Address** - Type or paste email in the input field
2. **Click "Search"** - Or press Enter
3. **Wait for Analysis** - Progress indicator shows scanning status (10-30 seconds)
4. **View Results** - Color-coded cards show account status

**Result Colors:**
- 🟢 **Green** - Account Found (email is registered)
- 🔴 **Red** - Not Found (email not registered)
- 🟡 **Yellow** - Rate Limited (too many requests, try later)
- 🟣 **Purple** - Error (technical issue with check)

#### 2. Using OSINT Intelligence Tools
1. **Complete Email Search** - Wait for results to finish
2. **Click "OSINT Tools" Button** - Opens large modal with 5 tabs
3. **Explore Intelligence Tabs:**
   - 📧 **Email Analysis** - Name extraction, birth year, provider type
   - 👤 **Username Variations** - Get 20+ alternatives to search elsewhere
   - 🔓 **Breach Check** - View data breaches and security info
   - 📨 **Related Emails** - Alternative email suggestions
   - 🌐 **Domain Analysis** - Geographic and organizational intelligence

#### 3. Advanced Features
- **Filter Results** - Click filter buttons (All, Found, Not Found, Rate Limited, Errors)
- **Export Data** - Click "Export to CSV" to download results
- **Clear & Restart** - Click "Clear Results" to start new search

### Command Line Interface

```bash
# Basic usage
python -m holehe.core email@example.com

# Only show found accounts
python -m holehe.core email@example.com --only-used

# Export to CSV
python -m holehe.core email@example.com --csv

# Disable password recovery checks
python -m holehe.core email@example.com --no-password-recovery
```

---

## 📡 API Documentation

### REST Endpoints

#### 1. Start Email Analysis
```http
POST /check_email
Content-Type: application/json

{
  "email": "test@example.com"
}
```

**Response:**
```json
{
  "status": "processing",
  "message": "Analysis started"
}
```

#### 2. Get Results (Polling)
```http
GET /get_results/{email}
```

**Response (Completed):**
```json
{
  "status": "completed",
  "timestamp": "2025-11-15T10:30:45",
  "total_sites": 120,
  "found_accounts": 15,
  "results": [
    {
      "name": "instagram",
      "exists": true,
      "rateLimit": false,
      "emailrecovery": "j***@gmail.com",
      "phoneNumber": null
    }
  ]
}
```

#### 3. OSINT Intelligence Endpoints

```http
GET /osint/email_analysis/{email}      # Email pattern analysis
GET /osint/username_variations/{email} # Username alternatives
GET /osint/breach_check/{email}        # Data breach information
GET /osint/related_emails/{email}      # Alternative email suggestions
GET /osint/domain_analysis/{email}     # Domain intelligence
```

---

## 🌐 Supported Platforms

### 23 Categories | 120+ Websites

| Category | Examples | Count |
|----------|----------|-------|
| 🔵 Social Media | Instagram, Twitter, Facebook, TikTok, LinkedIn, Snapchat | 15+ |
| 📧 Email Services | Gmail, Yahoo, ProtonMail, Outlook | 5+ |
| 🛒 Shopping | Amazon, eBay, Etsy, Deliveroo | 10+ |
| 💼 CRM Systems | HubSpot, Salesforce, Zoho, Pipedrive | 7+ |
| 📝 CMS | WordPress, Atlassian, Gravatar | 5+ |
| 🎓 Learning | Duolingo, Quora, Coursera | 8+ |
| 🎵 Music | Spotify, SoundCloud, Last.fm | 6+ |
| 💻 Programming | GitHub, Stack Overflow, Docker | 10+ |
| 💬 Forums | MyBB, Gaming forums, Tech forums | 8+ |
| 💼 Jobs | Freelancer, LinkedIn Jobs, Indeed | 5+ |
| 🎬 Media | Netflix, Flickr, YouTube | 5+ |
| 🏥 Medical | 7 Cups, CaringBridge | 3+ |
| 💰 Crowdfunding | Patreon, Buy Me a Coffee | 4+ |
| 📱 Software | Adobe, Evernote, LastPass | 6+ |
| 🏃 Sport | Strava, Nike, Fitbit | 4+ |
| 🚗 Transport | Uber, Lyft | 2+ |
| 🏠 Real Estate | Vrbo, Zillow | 3+ |
| 🔍 OSINT Tools | RocketReach | 2+ |
| And 5+ more categories... | | 20+ |

---

## ⚙️ How It Works

### Detection Methods

#### 1. Registration Simulation (Most Common)
```
1. GET registration page → Extract CSRF token
2. POST registration attempt with email
3. Analyze response:
   - "Email already exists" → Found ✅
   - "Email available" → Not Found ❌
   - "Too many requests" → Rate Limited ⏰
```

#### 2. Password Recovery
```
1. POST forgot password request
2. Analyze response:
   - Shows partial recovery email → Found ✅
   - "Email not found" → Not Found ❌
```

#### 3. API Endpoint Checks
```
1. POST to /api/check-email endpoint
2. Parse JSON response:
   - {"available": false} → Found ✅
   - {"available": true} → Not Found ❌
```

### Architecture

```
User Request → Flask Server → Background Thread
                                    ↓
                             Trio Async Runtime
                                    ↓
                    120+ Concurrent HTTP Checks
                                    ↓
                              Result Cache
                                    ↓
                    Frontend Polling ← Results
```

**Key Features:**
- ✅ **Concurrent Execution** - Multiple checks run simultaneously
- ✅ **Non-blocking** - Flask remains responsive
- ✅ **Connection Pooling** - Efficient HTTP client usage
- ✅ **Error Isolation** - Single failures don't crash system
- ✅ **Timeout Management** - Individual timeouts per request

---

## 📂 Project Structure

```
holehe/
│
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── README.md                       # This documentation
├── templates/
│   └── index.html                 # Frontend web interface
├── screenshots/                    # Project screenshots
│   ├── main-interface.png
│   └── osint-tools.png
│
└── holehe/                        # Core package
    ├── __init__.py
    ├── core.py                    # Core functionality
    ├── instruments.py             # Progress tracking
    ├── localuseragent.py          # User agent strings
    ├── activity_tracker.py        # Activity simulation
    ├── osint_tools.py             # OSINT intelligence tools
    │
    └── modules/                   # Website checking modules (120+)
        ├── social_media/          # Instagram, Twitter, etc.
        ├── mails/                 # Gmail, Yahoo, etc.
        ├── shopping/              # Amazon, eBay, etc.
        ├── cms/                   # WordPress, Atlassian
        ├── crm/                   # HubSpot, Salesforce
        ├── forum/                 # Discussion forums
        ├── learning/              # Duolingo, Quora
        ├── music/                 # Spotify, SoundCloud
        ├── programing/            # GitHub, Stack Overflow
        └── [15+ more categories]
```

---

## 🔒 Security & Ethics

### ⚠️ Important Guidelines

#### ✅ Acceptable Use
- Personal digital footprint audit
- Authorized security assessments
- Digital forensics investigations
- Educational and research purposes

#### ❌ Unacceptable Use
- Unauthorized surveillance
- Harassment or stalking
- Identity theft
- Privacy invasion

### Technical Security Features

- **No Data Storage** - Results stored temporarily in memory only
- **HTTPS Only** - All requests use secure connections
- **Rate Limiting** - Respects website rate limits
- **Error Handling** - Graceful degradation on failures
- **User Agents** - Randomized to prevent fingerprinting
- **Timeout Protection** - Prevents indefinite hanging requests

### Legal Compliance

> **Educational Disclaimer**: This tool is developed for educational purposes only. Users must:
> - Only check email addresses they own or have permission to investigate
> - Comply with local laws and regulations (GDPR, CCPA, etc.)
> - Respect privacy and ethical boundaries
> - Handle results responsibly and securely

### Professional OSINT Ethics

The OSINT intelligence tools in this project use **legal pattern recognition** techniques:
- ✅ No unauthorized access to accounts
- ✅ No password cracking or hacking
- ✅ Only public information analysis
- ✅ Pattern-based intelligence extraction
- ✅ Same methods used by professional investigators

---

## 🔧 Troubleshooting

### Common Issues & Solutions

#### Problem: Module not found / Import errors
```bash
# Solution: Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

#### Problem: Port 5000 already in use
```bash
# Solution: Change port in app.py (line 102)
app.run(debug=True, port=5001)  # Use different port
```

#### Problem: No results appearing
**Solutions:**
1. Check internet connection
2. Wait 30-60 seconds (some sites are slow)
3. Check browser console (F12) for errors
4. Try a different email address
5. Clear browser cache

#### Problem: Many "Rate Limited" results
**Solution:**
- This is normal behavior (websites protect against automation)
- Wait 5-15 minutes and try again
- Rate limits typically reset automatically

#### Problem: "Too many requests" error
**Solution:**
```bash
# Clear the result cache
# Restart the application
python app.py
```

### Expected Behavior

✅ **Success Indicators:**
- Green cards for found accounts
- Red cards for not found
- Yellow cards for rate limits (temporary)
- Statistics dashboard updates
- Filter buttons work
- CSV export downloads file

---

## 🤝 Contributing

### Adding New Website Modules

1. Create a new module file in the appropriate category:

```python
# holehe/modules/social_media/newsite.py

async def newsite(email, client, out):
    name = "newsite"
    domain = "newsite.com"
    method = "register"
    frequent_rate_limit = False
    
    try:
        # Your checking logic here
        response = await client.post(url, data={'email': email})
        
        if "email exists" in response.text:
            out.append({
                "name": name,
                "domain": domain,
                "method": method,
                "frequent_rate_limit": frequent_rate_limit,
                "exists": True,
                "rateLimit": False,
                "emailrecovery": None,
                "phoneNumber": None,
                "others": None
            })
        else:
            out.append({
                "name": name,
                "exists": False
            })
    except Exception as e:
        out.append({
            "name": name,
            "exists": False,
            "error": str(e)
        })
```

2. The module will be automatically discovered and loaded!

### Development Workflow

```bash
# Fork and clone the repository
git clone https://github.com/yourusername/holehe-web.git
cd holehe-web

# Create a branch
git checkout -b feature/new-module

# Make changes and test
python app.py

# Commit and push
git add .
git commit -m "Add support for NewSite"
git push origin feature/new-module

# Create Pull Request
```

---

## 🎓 Educational Value

### What This Project Demonstrates

#### Backend Development
- ✅ Flask web framework mastery
- ✅ Async programming (trio, httpx)
- ✅ RESTful API design
- ✅ Background task processing
- ✅ Comprehensive error handling

#### Frontend Development
- ✅ Modern HTML/CSS/JavaScript
- ✅ Bootstrap framework
- ✅ Responsive design principles
- ✅ AJAX/Fetch API usage
- ✅ Real-time UI updates

#### Software Engineering
- ✅ Modular architecture
- ✅ Design patterns (MVC)
- ✅ Code organization
- ✅ Comprehensive documentation
- ✅ Version control readiness

#### Cybersecurity & OSINT
- ✅ Email pattern analysis algorithms
- ✅ Username enumeration techniques
- ✅ Data breach intelligence
- ✅ Domain analysis methods
- ✅ Legal vs illegal access understanding
- ✅ Professional OSINT methodology

---

## 🚀 Future Enhancements

### Potential Improvements

- [ ] **Have I Been Pwned API** - Real breach data integration
- [ ] **Database Integration** - PostgreSQL for persistent storage
- [ ] **User Authentication** - Account system with saved searches
- [ ] **Bulk Email Checking** - Upload CSV files
- [ ] **Dark Mode** - Toggle between light/dark themes
- [ ] **PDF Reports** - Generate comprehensive reports
- [ ] **Real-time Notifications** - WebSocket support
- [ ] **More Platforms** - Expand to 200+ websites
- [ ] **Advanced Filtering** - Custom filter combinations
- [ ] **API Rate Limiting** - Better request management
- [ ] **Social Media Scraping** - Public profile data (legal only)
- [ ] **Username Search** - Sherlock-style cross-platform search

---

## 📚 Resources & References

### Documentation
- [Flask Documentation](https://flask.palletsprojects.com/)
- [httpx Documentation](https://www.python-httpx.org/)
- [Trio Documentation](https://trio.readthedocs.io/)
- [Bootstrap Documentation](https://getbootstrap.com/)

### Related OSINT Tools
- [Holehe Original](https://github.com/megadose/holehe) - Command-line version
- [Sherlock](https://github.com/sherlock-project/sherlock) - Username search across platforms
- [theHarvester](https://github.com/laramies/theHarvester) - OSINT gathering tool
- [Have I Been Pwned](https://haveibeenpwned.com/) - Breach notification service

### Learning Resources
- OSINT Framework - Open Source Intelligence gathering
- Pattern Recognition in Cybersecurity
- Ethical Hacking and Digital Forensics

---

## 📄 License & Credits

### License
This project is developed for **educational purposes** as part of academic coursework to demonstrate:
- Full-stack web development skills
- Asynchronous programming techniques
- OSINT intelligence methodology
- Professional software engineering practices

### Credits
Based on the original [Holehe](https://github.com/megadose/holehe) project by megadose, significantly enhanced with:
- ✨ Modern web interface with Flask
- 🔍 Professional OSINT intelligence tools (5 new features)
- ⚡ Real-time asynchronous processing
- 📊 Advanced filtering and export capabilities
- 🎨 Beautiful responsive UI design
- 📚 Comprehensive documentation

### Disclaimer
> The developers are not responsible for misuse of this tool. Use responsibly, ethically, and in compliance with all applicable laws. This tool is intended for educational purposes and authorized security assessments only.

---

## 👨‍💻 Project Information

**Project Name**: Holehe Email Account Finder - Web Application  
**Version**: 2.0.0 (OSINT Enhanced)  
**Purpose**: Educational OSINT Tool & Full-Stack Demonstration  
**Date**: November 2025  
**Status**: Active Development

### Key Achievements
- 🏆 120+ website modules implemented
- 🏆 5 professional OSINT intelligence tools
- 🏆 Real-time asynchronous processing
- 🏆 Modern responsive web interface
- 🏆 Comprehensive documentation
- 🏆 Educational and professional grade

---





---

## 📸 Screenshots

<div align="center">

<img width="1003" height="407" alt="image" src="https://github.com/user-attachments/assets/7ccf61b3-95aa-4e84-8060-1e97e70d1ad2" />


*Modern web interface with real-time email search across 120+ platforms*

<img width="1004" height="839" alt="Screenshot 2025-11-15 010131" src="https://github.com/user-attachments/assets/643af01b-fc65-44d8-a889-0b06d54f8c15" />

<img width="1011" height="860" alt="Screenshot 2025-11-15 010140" src="https://github.com/user-attachments/assets/d93c8539-a5b0-442d-bc21-385a4a37ff50" />




*Professional OSINT intelligence tools with 5 specialized analysis tabs*

</div>

---
<div align="center">

### 🎓 Built for Educational Purposes

**Demonstrates:** Web Development • OSINT Techniques • Async Programming • API Design • UI/UX Design

**Technologies:** Python • Flask • JavaScript • Bootstrap • Trio • httpx

---

**Holehe Email Account Finder** © 2025

*Professional OSINT Intelligence Tool for Educational Use*

[⬆ Back to Top](#-holehe-email-account-finder---web-application)

</div>
