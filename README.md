A web-based tool that leverages Google's Gemini 1.5 Flash model to summarize text documents into various formats.

Features

* Flexible Input: Accept raw text paste or .txt file uploads.  
* Customizable Output: Choose between Brief, Detailed, or Bullet Point summary styles.  
* Robust Error Handling: Handles Google API quotas and validation errors.  
* Clean UI: Built with Streamlit.

Setup Instructions

Prerequisites

* Python 3.9+  
* A Google API Key (Get it here: Google AI Studio)

Installation

1. Clone the repository: git clone \<your-repo-link\> cd gemini\_summarizer  
2. Install Dependencies: pip install \-r requirements.txt  
3. Run the Application: streamlit run app.py  
4. Usage:  
   * The app will open in your browser (http://localhost:8501).  
   * Enter your Google API Key in the sidebar.  
   * Select your desired summary style.  
   * Paste text or upload a file.  
   * Click "Generate Summary".

Tech Stack

* Frontend: Streamlit  
* AI Model: Google Gemini (gemini-1.5-flash) via google-generativeai SDK  
* Resilience: tenacity library for API retry logic.

