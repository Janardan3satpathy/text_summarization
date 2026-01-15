import streamlit as st
from utils import SummarizerService

# Page Config
st.set_page_config(page_title="Gemini Doc Summarizer", page_icon="✨")

# Title and Description
st.title("✨ Gemini Document Summarizer")
st.markdown("Upload a text file or paste text below to generate a summary using **Google Gemini**.")

# Sidebar for Configuration
with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Google API Key", type="password", help="Get your key from Google AI Studio.")
    
    st.markdown("---")
    st.markdown("### Options")
    summary_style = st.selectbox(
        "Summarization Style",
        ("Brief", "Detailed", "Bullet Points")
    )
    st.caption("Model: gemini-1.5-flash")

# Main Input Area
input_method = st.radio("Choose input method:", ("Paste Text", "Upload File"))

text_input = ""

if input_method == "Paste Text":
    text_input = st.text_area("Paste your text here:", height=200)
else:
    uploaded_file = st.file_uploader("Choose a .txt file", type=['txt'])
    if uploaded_file is not None:
        try:
            text_input = uploaded_file.getvalue().decode("utf-8")
            st.success("File uploaded successfully!")
            with st.expander("View uploaded text"):
                st.text(text_input)
        except Exception as e:
            st.error(f"Error reading file: {e}")

# Summarize Button
if st.button("Generate Summary", type="primary"):
    # 1. Validation: Check API Key
    if not api_key:
        st.warning("⚠️ Please enter your Google API Key in the sidebar.")
    
    # 2. Validation: Check Input Text
    elif not text_input.strip():
        st.warning("⚠️ Please provide some text to summarize.")
    
    else:
        with st.spinner("Gemini is analyzing..."):
            try:
                # Initialize Service
                summarizer = SummarizerService(api_key)
                
                # Get Summary
                summary = summarizer.summarize(text_input, summary_style)
                
                # Display Result
                st.subheader("Summary Result")
                st.markdown(summary) # Markdown works well with Gemini's output
                
                # Option to download summary
                st.download_button(
                    label="Download Summary",
                    data=summary,
                    file_name="gemini_summary.txt",
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"❌ Error: {e}")

# Footer
st.markdown("---")
st.caption("Simple Document Summarization Service | Built with Streamlit & Google Gemini")