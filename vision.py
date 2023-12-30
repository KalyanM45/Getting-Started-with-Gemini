from dotenv import load_dotenv
import streamlit as st
from PIL import Image
import google.generativeai as genai
import os

# Load environment variables from .env
load_dotenv()

# Configure Streamlit
st.set_page_config(
    page_title="Generative AI Vision App",
    page_icon="🔮",
    layout="wide"
)

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro-vision')

# Function to generate content
def gen(input, image):
    if input != "":
        response = model.generate_content(input, image)
    else:
        response = model.generate_content(image)
    return response.text

# Streamlit app layout
st.title("Generative AI Vision App")
st.markdown(
    """
    Welcome to the Generative AI Vision App! 
    Ask a question about the uploaded image, and let the model describe it.
    """
)

# User input for question
input_question = st.text_input('Input your question here:', key='input')

# File upload for image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Button to trigger image description generation
submit_button = st.button('Tell me about the image')

# Generate and display response on button click
if submit_button:
    response_text = gen(input_question, image)
    st.write("Generated Description:")
    st.write(response_text)
