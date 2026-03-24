import streamlit as st
from google import genai

# --- AI SETUP ---
# PASTE YOUR ACTUAL KEY BETWEEN THE QUOTES BELOW
MY_API_KEY = "AIzaSyCFK3Hzhbthrlkz3CN8k7GOXhRN61rHT0w"
from google import genai

# --- AI SETUP ---
# PASTE YOUR ACTUAL KEY BETWEEN THE QUOTES BELOW
MY_API_KEY = "PASTE_YOUR_AIza_KEY_HERE" 

client = genai.Client(api_key=MY_API_KEY)

# --- WEBSITE INTERFACE ---
st.set_page_config(page_title="iKON Xerox Expert", page_icon="🖨️")
st.title("iKON Xerox & Copier Solutions")
st.subheader("AI Technical Assistant")

# --- CHAT FEATURE ---
user_query = st.text_input("Enter Xerox Error Code (e.g., SC542):")

if st.button("Ask Expert"):
    if user_query:
        try:
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=f"You are a professional Xerox repair technician. Help with: {user_query}"
            )
            st.success(response.text)
        except Exception as e:
            st.error(f"Wait 60 seconds and refresh. Error: {e}")
    else:
        st.warning("Please type something first!")" 

client = genai.Client(api_key=MY_API_KEY)

# --- WEBSITE INTERFACE ---
st.set_page_config(page_title="iKON Xerox Expert", page_icon="🖨️")
st.title("iKON Xerox & Copier Solutions")
st.subheader("AI Technical Assistant")

# --- CHAT FEATURE ---
user_query = st.text_input("Enter Xerox Error Code (e.g., SC542):")

if st.button("Ask Expert"):
    if user_query:
        try:
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=f"You are a professional Xerox repair technician. Help with: {user_query}"
            )
            st.success(response.text)
        except Exception as e:
            st.error(f"Wait 60 seconds and refresh. Error: {e}")
    else:
        st.warning("Please type something first!")
