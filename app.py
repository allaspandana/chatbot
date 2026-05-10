import streamlit as st
import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyAyojFvx0qEF5psdM7MGwdPIMSBq7OCifg")

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("Gemini AI Chatbot")

user_input = st.text_input("Ask something:")

if st.button("Send"):

    if user_input:

        response = model.generate_content(user_input)

        st.write("Bot:", response.text)