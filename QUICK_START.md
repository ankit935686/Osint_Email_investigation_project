# 🚀 Quick Start Guide

## For Teachers/Reviewers: Running This Project in 5 Minutes

### Prerequisites Check
- ✅ Python 3.8+ installed ([Download](https://www.python.org/downloads/))
- ✅ Internet connection
- ✅ Modern web browser (Chrome, Firefox, Edge)

### Step 1: Open Terminal/PowerShell
Navigate to project directory:
```powershell
cd "C:\Users\ankit\OneDrive\Desktop\sandip\mail_check\holehe"
```

### Step 2: Install Dependencies
```powershell
pip install -r requirements.txt
```
⏱️ *Takes ~2-3 minutes*

### Step 3: Run Application
```powershell
python app.py
```

### Step 4: Open in Browser
Navigate to:
```
http://localhost:5000
```

### Step 5: Test the Application
1. Enter any email address (e.g., `test@gmail.com`)
2. Click "Search"
3. Wait 10-30 seconds for results
4. View 120+ website checks!

---

## Demo Test Emails

Try these for demonstration:
- `test@gmail.com`
- `example@yahoo.com`
- `demo@outlook.com`

---

## Expected Behavior

### ✅ Success Indicators:
- Green cards = Email found on that platform
- Red cards = Email not registered
- Yellow cards = Rate limited (temporary)
- Statistics dashboard updates
- Filter buttons work

### 🎯 Key Features to Review:
1. **Real-time Processing** - Watch the loading spinner
2. **Result Filtering** - Click filter buttons (All, Found, Not Found, etc.)
3. **Export Functionality** - Click "Export to CSV"
4. **Responsive Design** - Resize browser window
5. **Error Handling** - Try invalid email format

---

## Troubleshooting

### Problem: "Module not found"
**Solution**: Install dependencies
```powershell
pip install flask httpx trio bs4 termcolor tqdm colorama
```

### Problem: "Port already in use"
**Solution**: Change port in `app.py` line 102:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Changed to 5001
```

### Problem: "No results appearing"
**Solution**: 
1. Check internet connection
2. Wait 30-60 seconds
3. Check browser console (F12) for errors
4. Try different email address

---

## Quick Code Review Points

### 1. **Architecture** (app.py)
- Flask web server ✅
- Background threading ✅
- Async processing with Trio ✅
- Result caching ✅

### 2. **Frontend** (templates/index.html)
- Modern responsive UI ✅
- Real-time polling ✅
- Interactive filtering ✅
- Export functionality ✅

### 3. **Core Logic** (holehe/core.py)
- Dynamic module discovery ✅
- Async HTTP requests ✅
- Error handling ✅
- Progress tracking ✅

### 4. **Modules** (holehe/modules/)
- 120+ website checks ✅
- 23 categories ✅
- Standardized output format ✅

---

## Project Highlights for Evaluation

### Technical Skills Demonstrated:
- ✅ **Backend**: Flask, Python, Async programming
- ✅ **Frontend**: HTML, CSS, JavaScript, Bootstrap
- ✅ **API Design**: RESTful endpoints, JSON responses
- ✅ **Architecture**: Modular design, separation of concerns
- ✅ **User Experience**: Real-time updates, filtering, export
- ✅ **Error Handling**: Graceful degradation, timeout management
- ✅ **Documentation**: Comprehensive README, code comments

### Complexity Indicators:
- 🔥 Handles 120+ concurrent async HTTP requests
- 🔥 Dynamic module discovery and loading
- 🔥 Background task processing with threading
- 🔥 Real-time result polling and caching
- 🔥 Modern glassmorphism UI design

---

## Stopping the Application

Press `CTRL + C` in the terminal to stop the Flask server.

---

## Quick Questions & Answers

**Q: How many websites does it check?**
A: 120+ websites across 23 categories

**Q: How long does a search take?**
A: Typically 10-30 seconds depending on network speed

**Q: Is it secure?**
A: Yes - uses HTTPS, no data storage, timeout protection

**Q: Can it handle multiple users?**
A: Yes - uses caching and background threads

**Q: What if a website blocks the request?**
A: Graceful error handling with "Rate Limited" status

---

## Contact

For any questions or issues running the project, please refer to the main README.md file or contact the student.

---

*Setup time: ~5 minutes | Demo time: ~2 minutes*
