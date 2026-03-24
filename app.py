import streamlit as st
from google import genai
from google.genai import errors

# --- AI SETUP ---
# Use your API Key here
client = genai.Client(api_key="GEMINI_API_KEY = "AIzaSyCFK3Hzhbthrlkz3CN8k7GOXhRN61rHT0w")

# --- CUSTOMER INTERFACE ---
st.set_page_config(page_title="iKON Xerox Solutions", page_icon="🖨️")
st.title("iKON Xerox & Copier Services")
st.subheader("Professional Repair & Parts")

# Business Features
st.info("""
**Our Services:**
* 🛠️ Full Machine Servicing & Repair
* 📄 High-Quality Bulk Xerox & Printing
* 🧪 Toner Refilling & Drum Replacement
* ⚙️ Genuine Spare Parts for All Models
""")

st.write("---")

# --- XEROX EXPERT AI ---
st.write("### Ask our Technical Assistant")
user_query = st.text_input("Describe the issue or part you need (e.g., 'Error code SC542' or 'Toner price')")

if st.button("Consult Expert"):
    if user_query:
        try:
            # We tell the AI exactly who it is here:
            specialized_prompt = f"You are a Xerox machine repair expert. Answer this customer query accurately: {user_query}"
            
            response = client.models.generate_content(
                model="gemini-1.5-flash", 
                contents=specialized_prompt
            )
            st.success(response.text)
            
        except errors.ClientError as e:
            if "429" in str(e):
                st.error("⚠️ The AI expert is currently busy helping another customer. Please wait 60 seconds and try again.")
            else:
                st.error("⚠️ Connection error. Please refresh the page.")
    else:
        st.warning("Please enter a question or error code first.")
