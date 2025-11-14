# 📧 Holehe Email Account Finder - Web Application

## 🎓 Academic Project Overview

This project is a comprehensive **Email OSINT (Open Source Intelligence)** tool built as a web application using **Flask**. It allows users to check if an email address is registered across **120+ popular websites and platforms** including social media, shopping sites, forums, CRM systems, and more.

---

## 📋 Table of Contents

- [Project Description](#project-description)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Architecture & Design](#architecture--design)
- [Project Structure](#project-structure)
- [Code Explanation](#code-explanation)
- [How It Works](#how-it-works)
- [Installation & Setup](#installation--setup)
- [Usage Guide](#usage-guide)
- [API Documentation](#api-documentation)
- [Module Categories](#module-categories)
- [Security & Ethics](#security--ethics)
- [Future Enhancements](#future-enhancements)

---

## 🎯 Project Description

**Holehe Email Account Finder** is an OSINT (Open Source Intelligence) reconnaissance tool that helps identify which online services are associated with a given email address. This is particularly useful for:

- **Cybersecurity professionals** conducting penetration testing
- **Digital forensics investigators** tracking online presence
- **Individuals** wanting to audit their own digital footprint
- **Researchers** studying online identity patterns

The application performs automated checks across multiple platforms by simulating registration attempts and analyzing responses to determine if an email is already registered.

---

## ✨ Key Features

### 1. **Comprehensive Coverage**
- Checks **120+ websites** across 23 different categories
- Includes social media, email services, shopping, forums, CRM systems, and more

### 2. **Modern Web Interface**
- Beautiful, responsive UI with gradient designs
- Real-time progress tracking
- Interactive filtering system
- Statistical dashboard showing results summary

### 3. **Asynchronous Processing**
- Uses **async/await** with `httpx` and `trio` for concurrent requests
- Non-blocking operations for better performance
- Background task processing with threading

### 4. **Smart Detection Methods**
- Registration simulation
- Password recovery checks
- API endpoint analysis
- Response pattern matching

### 5. **Result Management**
- Real-time result updates via polling
- Categorized results (Found, Not Found, Rate Limited, Errors)
- CSV export functionality
- Session caching for performance

### 6. **Error Handling**
- Graceful handling of rate limits
- Timeout management
- Network error recovery
- Detailed debug information

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
- **JavaScript (ES6+)** - Interactive functionality

### Other Libraries
- **termcolor** - Terminal color output
- **tqdm** - Progress bars
- **colorama** - Cross-platform colored terminal text

---

## 🏗️ Architecture & Design

### 1. **MVC Pattern**
```
Model (Data Layer)
  ├── Email validation logic
  ├── Website checking modules
  └── Result data structures

View (Presentation Layer)
  ├── HTML templates (index.html)
  ├── CSS styling (embedded)
  └── JavaScript frontend logic

Controller (Application Logic)
  ├── Flask routes (app.py)
  ├── Request handling
  └── Background processing
```

### 2. **Asynchronous Architecture**
```
User Request → Flask → Background Thread → Async Executor (Trio)
                           ↓
                    Result Cache ← Polling ← Frontend
```

### 3. **Module System**
```
holehe/
  modules/
    ├── social_media/ (Instagram, Twitter, etc.)
    ├── mails/ (Gmail, Yahoo, etc.)
    ├── shopping/ (Amazon, eBay, etc.)
    ├── forum/ (Various forums)
    ├── crm/ (Hubspot, Zoho, etc.)
    └── [20+ more categories]
```

---

## 📂 Project Structure

```
holehe/
│
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── templates/
│   └── index.html                 # Frontend web interface
│
└── holehe/                        # Core package
    ├── __init__.py                # Package initialization
    ├── core.py                    # Core functionality & CLI
    ├── instruments.py             # Progress tracking
    ├── localuseragent.py          # User agent strings
    │
    └── modules/                   # Website checking modules
        ├── __init__.py
        ├── social_media/          # Social platforms (Instagram, Twitter, etc.)
        ├── mails/                 # Email services (Gmail, Yahoo, etc.)
        ├── shopping/              # E-commerce (Amazon, eBay, etc.)
        ├── cms/                   # Content Management Systems
        ├── crm/                   # Customer Relationship Management
        ├── forum/                 # Discussion forums
        ├── learning/              # Educational platforms
        ├── music/                 # Music streaming services
        ├── medias/                # Media platforms
        ├── jobs/                  # Job portals
        ├── crowfunding/           # Crowdfunding sites
        ├── programing/            # Developer platforms
        ├── sport/                 # Sports platforms
        ├── transport/             # Transportation services
        ├── real_estate/           # Real estate platforms
        ├── products/              # Product platforms
        ├── productivity/          # Productivity tools
        ├── software/              # Software services
        ├── payment/               # Payment platforms
        ├── porn/                  # Adult content sites
        ├── osint/                 # OSINT tools
        ├── company/               # Company platforms
        └── medical/               # Medical platforms
```

---

## 💻 Code Explanation

### 1. **app.py - Flask Application**

#### Main Components:

```python
# Global cache to store results
results_cache = {}
```
- **Purpose**: Store analysis results temporarily
- **Structure**: `{email: {status, results, timestamp}}`

#### Key Functions:

**a) `run_holehe_async(email)`**
```python
def run_holehe_async(email):
    """Run holehe asynchronously and store results"""
    async def main():
        # Import all checking modules
        modules = import_submodules("holehe.modules")
        websites = get_functions(modules)
        
        # Create async HTTP client
        client = httpx.AsyncClient(timeout=30.0)
        out = []
        
        # Check each website
        for website in websites:
            await website(email, client, out)
        
        # Store results in cache
        results_cache[email] = processed_results
```
- **Threading**: Runs in background thread
- **Async Execution**: Uses `trio.run()` for async operations
- **Progress Tracking**: Updates cache with progress information
- **Error Handling**: Catches and logs errors for each module

**b) Flask Routes:**

```python
@app.route('/check_email', methods=['POST'])
def check_email():
    """Start email analysis"""
    # 1. Get email from request
    # 2. Check if already processing
    # 3. Start background thread
    # 4. Return processing status
```

```python
@app.route('/get_results/<email>')
def get_results(email):
    """Poll for results"""
    # 1. Check cache for email
    # 2. Return current status
    # 3. Return results when complete
```

### 2. **core.py - Core Logic**

#### Module Import System:

```python
def import_submodules(package, recursive=True):
    """Dynamically import all website checking modules"""
    # Uses pkgutil to discover all modules
    # Recursively imports submodules
    # Returns dictionary of module objects
```

**How it works:**
1. Scans `holehe/modules/` directory
2. Finds all Python files (modules)
3. Imports them dynamically
4. Returns as callable functions

#### Function Extraction:

```python
def get_functions(modules, args=None):
    """Extract checking functions from modules"""
    websites = []
    for module in modules:
        if len(module.split(".")) > 3:
            # Extract function from module
            websites.append(modu.__dict__[site])
    return websites
```

#### Email Validation:

```python
def is_email(email: str) -> bool:
    """Validate email format using regex"""
    EMAIL_FORMAT = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return bool(re.fullmatch(EMAIL_FORMAT, email))
```

### 3. **Website Checking Modules**

Each module follows a standard pattern:

#### Example: instagram.py

```python
async def instagram(email, client, out):
    name = "instagram"
    domain = "instagram.com"
    method = "register"
    
    # 1. GET request to obtain CSRF token
    freq = await client.get("https://www.instagram.com/accounts/emailsignup/")
    token = extract_csrf_token(freq.text)
    
    # 2. POST request to check email availability
    data = {'email': email, 'username': random_username()}
    headers["x-csrftoken"] = token
    check = await client.post(url, data=data, headers=headers)
    
    # 3. Analyze response
    if check["errors"]["email"][0]["code"] == "email_is_taken":
        # Email exists!
        out.append({"name": name, "exists": True, ...})
    else:
        # Email doesn't exist
        out.append({"name": name, "exists": False, ...})
```

**Standard Output Format:**
```python
{
    "name": "instagram",           # Platform name
    "domain": "instagram.com",     # Domain
    "method": "register",          # Detection method
    "frequent_rate_limit": True,   # Rate limit frequency
    "rateLimit": False,            # Current rate limit status
    "exists": True,                # Email found/not found
    "emailrecovery": "j***@gmail.com",  # Recovery email (if found)
    "phoneNumber": "+1***1234",    # Phone number (if found)
    "others": {...}                # Additional info
}
```

### 4. **Frontend (index.html)**

#### JavaScript Functionality:

**a) Form Submission & Polling:**
```javascript
async function submitEmail(email) {
    // 1. Send POST request to /check_email
    const response = await fetch('/check_email', {
        method: 'POST',
        body: JSON.stringify({ email: email })
    });
    
    // 2. Start polling for results
    if (data.status === 'processing') {
        startPolling(email);
    }
}
```

**b) Result Polling:**
```javascript
function startPolling(email) {
    pollInterval = setInterval(async () => {
        // Poll every 1 second
        const response = await fetch(`/get_results/${email}`);
        
        if (data.status === 'completed') {
            // Stop polling and display results
            clearInterval(pollInterval);
            displayResults(data);
        }
    }, 1000);
}
```

**c) Result Display:**
```javascript
function displayResults(data) {
    // 1. Create card for each result
    // 2. Color code by status (green=found, red=not found)
    // 3. Display recovery info if available
    // 4. Update statistics
}
```

**d) Filtering System:**
```javascript
function applyFilter(filter) {
    // Show/hide results based on:
    // - All Results
    // - Found (exists=true)
    // - Not Found (exists=false)
    // - Rate Limited
    // - Errors
}
```

### 5. **instruments.py - Progress Tracking**

```python
class TrioProgress(trio.abc.Instrument):
    """Custom Trio instrument for progress tracking"""
    
    def __init__(self, total):
        self.tqdm = tqdm(total=total)  # Initialize progress bar
    
    def task_exited(self, task):
        """Called when each async task completes"""
        if task.name == "launch_module":
            self.tqdm.update(1)  # Update progress
```

**Purpose**: Provides visual feedback in CLI mode using `tqdm` progress bars.

---

## ⚙️ How It Works

### Detection Methods:

#### 1. **Registration Simulation**
- Most common method
- Attempts to start registration with email
- Checks if email is "already taken"

**Example Flow:**
```
1. GET registration page → Extract CSRF token
2. POST registration attempt with email
3. Analyze response:
   - "Email already exists" → Found ✅
   - "Email available" → Not Found ❌
   - "Too many requests" → Rate Limited ⏰
```

#### 2. **Password Recovery**
- Alternative method for some sites
- Attempts password reset
- Checks if recovery email is revealed

**Example Flow:**
```
1. POST forgot password request
2. Analyze response:
   - Shows partial recovery email → Found ✅
   - "Email not found" → Not Found ❌
```

#### 3. **API Endpoint Checks**
- Direct API calls
- Checks username/email availability endpoints

**Example Flow:**
```
1. POST to /api/check-email endpoint
2. Parse JSON response:
   - {"available": false} → Found ✅
   - {"available": true} → Not Found ❌
```

### Async Concurrency Model:

```
Main Thread
    ↓
Background Thread
    ↓
Trio Async Runtime
    ↓
┌─────────┬──────────┬──────────┬─────────┐
│ Task 1  │ Task 2   │ Task 3   │ Task N  │
│Instagram│ Google   │ Twitter  │ Netflix │
└─────────┴──────────┴──────────┴─────────┘
    ↓         ↓          ↓          ↓
HTTP Client (shared, connection pooling)
    ↓
Results aggregated in 'out' list
    ↓
Stored in results_cache
    ↓
Retrieved by polling endpoint
```

**Benefits:**
- **Concurrent execution**: Multiple checks run simultaneously
- **Non-blocking**: Flask remains responsive
- **Efficient**: Shared HTTP client with connection pooling
- **Timeout management**: Individual timeouts per request

---

## 🚀 Installation & Setup

### Prerequisites:
- Python 3.8 or higher
- pip (Python package manager)
- Internet connection

### Step-by-Step Installation:

#### 1. **Clone/Download the Project**
```bash
cd C:\Users\ankit\OneDrive\Desktop\sandip\mail_check\holehe
```

#### 2. **Create Virtual Environment** (Recommended)
```powershell
python -m venv venv
.\venv\Scripts\activate
```

#### 3. **Install Dependencies**
```powershell
pip install -r requirements.txt
```

**Dependencies installed:**
```
flask==2.3.3          # Web framework
httpx==0.27.0         # HTTP client
trio==0.30.0          # Async runtime
bs4==0.0.2            # Web scraping
termcolor==3.1.0      # Colored output
tqdm==4.67.1          # Progress bars
colorama==0.4.6       # Cross-platform colors
```

#### 4. **Run the Application**
```powershell
python app.py
```

#### 5. **Access Web Interface**
Open your browser and navigate to:
```
http://localhost:5000
```

---

## 📖 Usage Guide

### Web Interface:

#### 1. **Enter Email Address**
- Type or paste email in the input field
- Click "Search" button or press Enter

#### 2. **Wait for Analysis**
- Progress indicator shows scanning status
- Typically takes 10-30 seconds
- Checks 120+ websites automatically

#### 3. **View Results**
Results are organized into categories:
- ✅ **Account Found** (Green) - Email is registered
- ❌ **Not Found** (Red) - Email not registered
- ⏰ **Rate Limited** (Yellow) - Too many requests, try later
- ⚠️ **Error** (Purple) - Technical issue with check

#### 4. **Filter Results**
Use filter buttons to show only:
- All Results
- Found accounts
- Not Found
- Rate Limited
- Errors

#### 5. **Export Data**
- Click "Export to CSV" to download results
- File naming: `holehe_results_[email]_[date].csv`

#### 6. **Clear & Start New Search**
- Click "Clear Results" to reset
- Enter new email address

### Command Line Interface:

The project also supports CLI usage (though the web interface is recommended):

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

### Endpoints:

#### 1. **POST /check_email**
Start email analysis

**Request:**
```json
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

#### 2. **GET /get_results/{email}**
Retrieve analysis results (polling endpoint)

**Response (Processing):**
```json
{
  "status": "processing",
  "progress": "45/120",
  "timestamp": "2025-11-14T10:30:00"
}
```

**Response (Completed):**
```json
{
  "status": "completed",
  "timestamp": "2025-11-14T10:30:45",
  "total_sites": 120,
  "found_accounts": 15,
  "results": [
    {
      "name": "instagram",
      "exists": true,
      "rateLimit": false,
      "emailrecovery": "j***@gmail.com",
      "phoneNumber": null,
      "others": null
    },
    ...
  ]
}
```

#### 3. **POST /clear_cache**
Clear results cache

**Response:**
```json
{
  "message": "Cache cleared successfully"
}
```

---

## 🗂️ Module Categories

The application checks across **23 categories** with **120+ websites**:

### 1. **Social Media** (social_media/)
- Instagram, Twitter, Facebook, TikTok, LinkedIn, Snapchat, Pinterest, Reddit, Tumblr, Discord, Telegram, WhatsApp, etc.

### 2. **Email Services** (mails/)
- Gmail (Google), Yahoo, Mail.ru, ProtonMail, La Poste

### 3. **Shopping** (shopping/)
- Amazon, eBay, Etsy, Deliveroo

### 4. **CRM Systems** (crm/)
- HubSpot, Salesforce, Zoho, Pipedrive, Insightly, Nutshell, Nimble

### 5. **Content Management** (cms/)
- WordPress, Atlassian, Gravatar, Vox Media

### 6. **Learning Platforms** (learning/)
- Duolingo, Quora, Diigo

### 7. **Music Services** (music/)
- Spotify, SoundCloud, Last.fm, Smule

### 8. **Programming** (programing/)
- GitHub, Stack Overflow, CodePen, Repl.it, Docker

### 9. **Forums** (forum/)
- MyBB, Various tech forums, Gaming forums

### 10. **Job Portals** (jobs/)
- Freelancer, Coroflot, SEOClerks

### 11. **Media Platforms** (medias/)
- Netflix, Flickr, Rambler

### 12. **Medical** (medical/)
- 7 Cups, CaringBridge

### 13. **Crowdfunding** (crowfunding/)
- Buy Me a Coffee, Patreon

### 14. **Software Services** (software/)
- Adobe, Evernote, LastPass

### 15. **Sport** (sport/)
- Strava, Nike

### 16. **Transport** (transport/)
- Uber, Lyft

### 17. **Real Estate** (real_estate/)
- Vrbo, Real estate platforms

### 18. **OSINT Tools** (osint/)
- RocketReach

### 19. **Productivity** (productivity/)
- Various productivity tools

### 20. **Products** (products/)
- Product platforms

### 21. **Payment** (payment/)
- Payment platforms

### 22. **Company** (company/)
- About.me

### 23. **Others**
- Gaming, entertainment, and miscellaneous platforms

---

## 🔒 Security & Ethics

### Ethical Considerations:

⚠️ **Important Guidelines:**

1. **Consent**: Only check email addresses you own or have permission to investigate
2. **Rate Limiting**: Respect website rate limits to avoid service disruption
3. **Privacy**: Handle results responsibly and securely
4. **Legal Compliance**: Ensure usage complies with local laws and regulations

### Technical Security:

1. **No Data Storage**: Results are stored temporarily in memory cache
2. **HTTPS**: All requests use secure HTTPS connections
3. **User Agents**: Randomized user agents prevent fingerprinting
4. **Timeout Management**: Prevents indefinite hanging requests
5. **Error Handling**: Graceful degradation on failures

### Legitimate Use Cases:

✅ **Acceptable:**
- Personal digital footprint audit
- Authorized security assessments
- Digital forensics investigations
- Research with proper authorization

❌ **Unacceptable:**
- Unauthorized surveillance
- Harassment or stalking
- Identity theft
- Privacy invasion

---

## 🎨 UI/UX Features

### Design Elements:

1. **Gradient Backgrounds**: Modern, eye-catching gradients
2. **Glass Morphism**: Semi-transparent elements with blur
3. **Smooth Animations**: Hover effects, transitions
4. **Responsive Design**: Works on mobile, tablet, desktop
5. **Color Coding**: Intuitive status indicators
6. **Loading States**: Visual feedback during processing
7. **Statistics Dashboard**: Real-time result summary
8. **Filter System**: Easy result categorization

### User Experience:

- **Single Page Application**: No page refreshes
- **Real-time Updates**: Polling-based progress
- **Keyboard Support**: Enter key submission
- **Export Functionality**: Download results as CSV
- **Clear Visual Hierarchy**: Easy to scan results
- **Error Messages**: Helpful error descriptions

---

## 🔧 Future Enhancements

### Potential Improvements:

#### 1. **Database Integration**
- Persistent storage of results
- Historical search tracking
- User accounts and saved searches

#### 2. **Advanced Features**
- Bulk email checking
- Scheduled periodic checks
- Email breach detection integration
- Dark mode toggle

#### 3. **API Enhancements**
- RESTful API for programmatic access
- Webhook notifications
- Rate limit management
- API authentication

#### 4. **Performance Optimizations**
- Redis caching
- Result pagination
- Faster module loading
- Better timeout handling

#### 5. **Additional Modules**
- Add more websites (200+ target)
- Regional platform support
- Professional networks
- Gaming platforms

#### 6. **Reporting**
- PDF export
- Detailed reports with screenshots
- Timeline visualization
- Network graphs

#### 7. **Security**
- User authentication
- API key management
- Audit logging
- Encrypted storage

---

## 📊 Technical Challenges & Solutions

### Challenge 1: **Concurrent Request Management**
**Problem**: Checking 120+ websites sequentially is too slow

**Solution**: 
- Implemented async/await with `trio`
- Concurrent execution with shared HTTP client
- Connection pooling for efficiency

### Challenge 2: **Rate Limiting**
**Problem**: Websites block excessive requests

**Solution**:
- Individual timeout management
- Graceful error handling
- Rate limit detection and reporting
- Randomized user agents

### Challenge 3: **Background Processing in Flask**
**Problem**: Flask blocks during long operations

**Solution**:
- Background threading
- Result caching
- Polling-based frontend updates

### Challenge 4: **Module Discovery**
**Problem**: Manually importing 120+ modules is impractical

**Solution**:
- Dynamic module discovery with `pkgutil`
- Recursive submodule import
- Function extraction from modules

### Challenge 5: **User Experience**
**Problem**: User doesn't know what's happening during analysis

**Solution**:
- Real-time progress updates
- Visual loading indicators
- Status dashboard
- Detailed result cards

---

## 📝 Code Quality & Best Practices

### Followed Principles:

1. **Modular Design**: Each website check is a separate module
2. **DRY (Don't Repeat Yourself)**: Common patterns abstracted
3. **Error Handling**: Try-except blocks throughout
4. **Async Best Practices**: Proper async/await usage
5. **Documentation**: Comments explaining complex logic
6. **Separation of Concerns**: Frontend/Backend separation
7. **RESTful API**: Standard HTTP methods and status codes

---

## 🎓 Learning Outcomes

This project demonstrates proficiency in:

### Backend Development:
- ✅ Flask web framework
- ✅ Async programming (trio, httpx)
- ✅ RESTful API design
- ✅ Background task processing
- ✅ Error handling and logging

### Frontend Development:
- ✅ Modern HTML/CSS/JavaScript
- ✅ Bootstrap framework
- ✅ Responsive design
- ✅ AJAX/Fetch API
- ✅ DOM manipulation

### Software Engineering:
- ✅ Modular architecture
- ✅ Code organization
- ✅ Design patterns
- ✅ Documentation
- ✅ Version control readiness

### Web Technologies:
- ✅ HTTP protocol understanding
- ✅ CSRF token handling
- ✅ Cookie management
- ✅ Web scraping techniques

---

## 🤝 Contributing & Development

### To extend this project:

#### Adding New Website Modules:

1. **Create new module file** in appropriate category:
```python
# holehe/modules/social_media/newsite.py

async def newsite(email, client, out):
    name = "newsite"
    domain = "newsite.com"
    method = "register"
    
    try:
        # Your checking logic here
        response = await client.post(url, data={'email': email})
        
        if "email exists" in response.text:
            out.append({
                "name": name,
                "domain": domain,
                "exists": True,
                # ... other fields
            })
    except Exception as e:
        # Handle errors
        pass
```

2. **Module auto-discovery**: Module is automatically loaded!

---

## 📚 References & Resources

### Technologies Used:
- [Flask Documentation](https://flask.palletsprojects.com/)
- [httpx Documentation](https://www.python-httpx.org/)
- [Trio Documentation](https://trio.readthedocs.io/)
- [Bootstrap 5](https://getbootstrap.com/)

### OSINT Concepts:
- Email reconnaissance techniques
- Digital footprint analysis
- Open source intelligence gathering

---

## 👨‍🎓 Author Information

**Project**: Email Account Finder (Holehe Web Application)
**Course**: [Your Course Name]
**Instructor**: [Teacher Name]
**Date**: November 2025

---

## 📜 License & Disclaimer

### Educational Purpose:
This project is developed for **educational purposes only** as part of academic coursework to demonstrate web development, async programming, and OSINT concepts.

### Disclaimer:
- Use responsibly and ethically
- Respect privacy and legal boundaries
- Only check emails you own or have permission to investigate
- The developers are not responsible for misuse

### Credits:
Based on the original [Holehe](https://github.com/megadose/holehe) project by megadose, adapted and enhanced with a modern web interface for educational purposes.

---

## 🎯 Conclusion

This **Email Account Finder** project showcases a comprehensive full-stack web application that combines:
- Modern web development practices
- Asynchronous programming techniques
- Real-world OSINT functionality
- User-friendly interface design
- Scalable architecture

The application successfully demonstrates technical proficiency in Python, Flask, async programming, web technologies, and software engineering principles, making it an excellent portfolio piece for academic and professional purposes.

---

**For questions or clarifications, please refer to the inline code comments or contact the project author.**

---

*Last Updated: November 14, 2025*
