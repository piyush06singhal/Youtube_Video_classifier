# YouTube Comment Analyzer 

**Live App:** https://jam-packed-simplistic-wave.anvil.app/

---

## ⚠️ Important Disclaimer

**Backend Hosting:** This app uses Google Colab (free tier) as the backend server.

**What this means:**

- ✅ The app works perfectly when the server is running
- ⚠️ The backend stops automatically after 12 hours or when the browser is closed
- 🔄 **If the app doesn't respond, the server needs to be restarted manually**
- 📧 For live demo or if you encounter issues, please contact me

**Why Google Colab?** This is a portfolio/learning project using free hosting. For production deployment, a paid hosting service would be used.


---

## 🎥 Demo Video
Watch the demo here: [Click to watch](https://drive.google.com/file/d/1V9_dn8L7IPDGbKVOQDFDh8iwqqMH7yM1/view?usp=sharing)

---



---

## Project Overview

A professional web application built using **Anvil** and **Google Colab** that analyzes YouTube video comments with high accuracy. The app provides detailed sentiment analysis, genre classification, spam/bot detection, and generates downloadable Excel reports with comprehensive insights.

---

## Key Features

### 1. **Advanced Sentiment Analysis (85-90% Accuracy)**

- Uses **VADER** (Valence Aware Dictionary and sEntiment Reasoner)
- Specifically designed for social media text
- Handles slang, emojis, capitalization, and punctuation
- **Per-comment analysis** with individual sentiment scores
- Sentiment Categories:
  - Extremely Positive (score > 0.5)
  - Positive (score 0.05 to 0.5)
  - Neutral (score -0.05 to 0.05)
  - Negative (score -0.5 to -0.05)
  - Extremely Negative (score < -0.5)

### 2. **Intelligent Comment Fetching**

- Fetches up to **1000 comments** per video
- Prioritizes top comments (most liked/replied)
- Handles pagination automatically
- Fetches video metadata (title, channel, views, likes)
- Processes comments in 10-60 seconds

### 3. **Enhanced Genre Classification**

- **18 different genres** including:
  - Comedy, Music, Gaming, Educational, Tech, Sports
  - Food, Travel, Fashion, Horror, Action, Romance
  - Motivational, Relaxing, Drama, Documentary, Vlog
- Returns **top 3 genres** if multiple detected
- Advanced keyword matching algorithm

### 4. **Spam & Bot Detection**

- Automatically identifies spam comments based on:
  - Comment length, link count, repetitiveness
  - Excessive punctuation, all-caps text
- Detects bot accounts based on:
  - Username patterns, comment patterns
- Filters spam/bots from overall sentiment calculation

### 5. **Professional Excel Reports**

- **Summary Sheet** includes:
  - Video title, channel, views, likes
  - Overall sentiment and score
  - Genre classification
  - Total comments, spam count, bot count
  - Sentiment distribution (percentages)
- **Detailed Comments Sheet** includes:
  - Username, comment text (up to 500 chars)
  - Sentiment label and score
  - Positive/Neutral/Negative component scores
  - Like count, spam flag, bot flag
- Beautiful formatting with colors and styling
- File size: 1-2 MB for 1000 comments

### 6. **Direct Download**

- Click-to-download Excel reports
- No Google Drive authentication needed
- Automatic filename with video title and timestamp
- Works in all modern browsers

### 7. **Emoji & Text Processing**

- Converts emojis to text for better analysis
- Removes HTML tags and URLs
- Cleans extra whitespace
- Handles special characters properly

---

## Technologies Used

### **Frontend:**

- **Anvil**: Python-based full-stack web framework
- Responsive web interface

### **Backend:**

- **Google Colab**: Cloud-based Python environment
- **Anvil Uplink**: Connects Colab to Anvil app
- **Python 3.7+**: Core programming language

### **APIs & Libraries:**

- **YouTube Data API v3**: Fetches comments and video metadata
- **VADER Sentiment**: Advanced sentiment analysis for social media
- **openpyxl**: Excel file generation with formatting
- **emoji**: Emoji to text conversion
- **googleapiclient**: YouTube API integration

---

## How It Works

1. **Input the Video URL:**

   - User enters a YouTube video URL into the input field.

2. **Processing:**

   - The application fetches the comments using the YouTube Data API.
   - Analyzes the sentiment of the combined comments.
   - Classifies the genre based on keywords in the comments.

3. **Output:**
   - Displays the overall sentiment and genre on the web app.
   - Provides a sharable link to the comments file on Google Drive.

---

## File Structure

### **Frontend Code**

- Written in Python using Anvil’s framework.
- Handles user input, result display, and download link integration.

### **Backend Code**

- Fetches and processes YouTube comments.
- Saves processed data in an Excel file.
- Upload the Excel file to Google Drive.

---

## Prerequisites

- **Python 3.7+**
- **Google API Key** for YouTube Data API.
- **Google Service Account** for Drive API integration.
- **Anvil Uplink Key** for connecting the client-side and server-side.

---

# Challenges Faced

Pagination Handling: Ensuring all comments are fetched even for videos with large comment sections.
Genre Classification: Developing meaningful categories for classification based on keywords.
File Integration with Google Drive: Managing authentication and file upload using the Google Drive API.

---

# Future Enhancements

Real-Time Analysis: Enhance the backend to support real-time analysis for live videos.
Data Visualization: Integrate charts to visualize comment sentiments and trends.
Language Support: Expand to support multi-language comment analysis using NLP libraries.
User Accounts: Allow users to log in and save their analysis history.

---

# Contributions

Contributions are welcome! Please feel free to submit pull requests or create issues for improvements.

---

# License

This project is open-sourced under the MIT License.
