import streamlit as st
import google.generativeai as genai
import sys

st.set_page_config(page_title="Debug Mode", page_icon="🛠️")
st.title("🛠️ Gemini Debugger")

# 1. Check Library Version (Crucial!)
st.subheader("1. System Info")
st.write(f"**Python Version:** {sys.version.split()[0]}")
try:
    # If this is below 0.7.0, you will get 404 errors for Flash
    st.write(f"**Google GenAI Library Version:** `{genai.__version__}`") 
except AttributeError:
    st.error("⚠️ Library is too old to show version! Update required.")

# 2. Check Available Models
st.subheader("2. Check Available Models")
st.markdown("Enter your key to see exactly which models Google allows this server to use.")

api_key = st.text_input("Google API Key", type="password")

if st.button("List My Models"):
    if not api_key:
        st.warning("Please enter a key.")
    else:
        try:
            genai.configure(api_key=api_key)
            
            # Try to list models
            all_models = list(genai.list_models())
            chat_models = [m.name for m in all_models if 'generateContent' in m.supported_generation_methods]
            
            if chat_models:
                st.success(f"✅ Success! The API Key works. Found {len(chat_models)} compatible models.")
                st.markdown("### Copy one of these names exactly into your `utils.py`:")
                st.code("\n".join(chat_models))
            else:
                st.error("⚠️ Connection successful, but NO chat models were found. This API key might be restricted.")
                
        except Exception as e:
            st.error(f"❌ Connection Failed: {e}")