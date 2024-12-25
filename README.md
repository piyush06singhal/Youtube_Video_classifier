# YouTube Comment Analyzer with Google Drive Integration

## Project Overview
This project is a web application built using **Anvil** that allows users to analyze YouTube video comments. It integrates features like sentiment analysis, genre classification, and exporting data to **Google Drive** in an organized format. The main objective is to provide users with insights about the comments of a YouTube video and a downloadable comments file for further analysis.

---

## Key Features
### 1. **Comment Fetching**
   - Fetches up to 100 comments at a time using the YouTube Data API.
   - Handles pagination to gather all available comments for a given video.

### 2. **Sentiment Analysis**
   - Analyzes the overall sentiment of comments using **TextBlob**.
   - Sentiment Categories:
     - Extremely Positive
     - Positive
     - Neutral
     - Negative
     - Extremely Negative

### 3. **Genre Classification**
   - Classifies the video based on keywords in comments.
   - Possible Genres:
     - Comedy
     - Romance
     - Action
     - Educational
     - Heartwarming
     - And more...

### 4. **Export to Excel**
   - Saves comments in a structured format in an Excel file.
   - Includes the username and comment in separate columns.
   - Each sheet contains up to 100 comments for better readability.

### 5. **Google Drive Integration**
   - Automatically uploads the Excel file to the user’s Google Drive.
   - Provides a sharable link to access the uploaded file directly.

---

## Technologies Used
### **Frontend:**
   - **Anvil**: A platform for building full-stack web applications with Python.

### **Backend:**
   - **Python**: For logic implementation, including sentiment analysis and genre classification.
   - **YouTube Data API**: For fetching comments from YouTube videos.
   - **TextBlob**: For performing sentiment analysis.
   - **Google Drive API**: For uploading the Excel file to Google Drive.

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
- Uploads the Excel file to Google Drive.

---

## Prerequisites
- **Python 3.7+**
- **Google API Key** for YouTube Data API.
- **Google Service Account** for Drive API integration.
- **Anvil Uplink Key** for connecting the client-side and server-side.

---

## Setup Instructions
### **1. Clone the Repository**
```bash
git clone <repository-link>
cd <repository-directory>

2. Install Required Python Libraries
bash
Copy code
pip install openpyxl textblob google-api-python-client anvil-uplink
3. Configure API Keys
Add your YouTube API Key and Google Service Account credentials in the respective parts of the backend code.
4. Start the Server
Run the Anvil server-side code:

bash
Copy code
python server_code.py
Challenges Faced
Pagination Handling: Ensuring all comments are fetched even for videos with large comment sections.
Genre Classification: Developing meaningful categories for classification based on keywords.
File Integration with Google Drive: Managing authentication and file upload using the Google Drive API.
Future Enhancements
Real-Time Analysis: Enhance the backend to support real-time analysis for live videos.
Data Visualization: Integrate charts to visualize comment sentiments and trends.
Language Support: Expand to support multi-language comment analysis using NLP libraries.
User Accounts: Allow users to log in and save their analysis history.
Contributions
Contributions are welcome! Please feel free to submit pull requests or create issues for improvements.

License
This project is open-sourced under the MIT License.

Contact
For any queries or collaborations, feel free to reach out:

Email: piyush@example.com
LinkedIn: Piyush Singhal
css
Copy code

This README file is detailed, professional, and follows a structured format, making it easy for anyone to understand and contribute to the project.





