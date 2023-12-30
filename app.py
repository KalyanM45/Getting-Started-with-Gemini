from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import os

# Load environment variables from .env
load_dotenv()

# Configure Streamlit
st.set_page_config(
    page_title="Generative AI Question Answering",
    page_icon="❓",
    layout="wide"
)

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

# Function to generate content
def gen(question):
    response = model.generate_content(question)
    return response.text

# Streamlit app layout
st.title("Generative AI Question Answering")
st.markdown(
    """
    Welcome to the Generative AI Question Answering App! 
    Enter your question, and let the model generate a response for you.
    """
)

# User input for question
input_question = st.text_input('Input your question here:')

# Button to trigger question answering
submit_button = st.button('Submit')

# Generate and display response on button click
if submit_button:
    response_text = gen(input_question)
    st.write("Generated Response:")
    st.write(response_text)