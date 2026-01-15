import google.generativeai as genai
import os

# ---------------------------------------------------------
# PASTE YOUR API KEY INSIDE THE QUOTES BELOW
# ---------------------------------------------------------
MY_API_KEY = "PASTE_YOUR_KEY_HERE" 

try:
    print("1. Configuring API...")
    genai.configure(api_key=MY_API_KEY)

    print("2. Connecting to Gemini Model...")
    model = genai.GenerativeModel('gemini-1.5-flash')

    print("3. Sending test message...")
    response = model.generate_content("Say hello")
    
    print("\n✅ SUCCESS! Your API Key works.")
    print("Response from Google:", response.text)

except Exception as e:
    print("\n❌ FAILURE. Here is the real error:")
    print(e)