import streamlit as st
from google import genai
from google.genai import errors
import os
from dotenv import load_dotenv

# 1. Setup Security & Client
load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# 2. UI Design
st.set_page_config(page_title="2026 AI Summarizer", page_icon="⚡")
st.title("AI Summarizer")

user_input = st.text_area("Paste text here:", height=200)

if st.button("Summarize"):
    if user_input:
        with st.spinner("Analyzing with Gemini 2.5 Flash..."):
            try:
                # Updated to a valid 2026 stable model ID
                response = client.models.generate_content(
                    model="gemini-2.5-flash", 
                    contents=f"Summarize this text in 3 bullets: {user_input}"
                )
                st.success("Summary Complete!")
                st.write(response.text)
                
            except errors.ClientError as e:
                # Catching 404 and 429 specifically
                if "404" in str(e):
                    st.error("Error 404: The model name is incorrect or retired. Check AI Studio for the latest IDs.")
                elif "429" in str(e):
                    st.error("Error 429: Quota exceeded. Please wait a minute.")
                else:
                    st.error(f"API Error: {e}")
    else:
        st.warning("Please paste text first!")