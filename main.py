import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch the Hugging Face API key from the environment variable
API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Hugging Face model API endpoint for T5
T5_API_URL = "https://api-inference.huggingface.co/models/google-t5/t5-small"
headers = {"Authorization": f"Bearer {API_KEY}"}

def translate_text(text, source_lang, target_lang):
    """
    Translate the input text using the T5 model.
    """
    try:
        # Format the input for T5 (e.g., "translate English to French: Hello, how are you?")
        task = f"translate {source_lang} to {target_lang}: {text}"
        payload = {"inputs": task}
        response = requests.post(T5_API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        
        # Debug: Print the API response
        print("API Response:", response.json())
        
        # Extract the translation from the response
        translation = response.json()[0]["generated_text"]
        return translation
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    except KeyError:
        return "Error: Unable to parse the API response."

# Streamlit app
st.title("🌍 Real-Time Translation with T5 🈶")
st.write("Enter text and select the source and target languages for translation:")

# Text input area
text = st.text_area("Input Text")

# Language selection dropdowns
source_lang = st.selectbox(
    "Select Source Language",
    options=["English", "French", "Spanish", "German", "Chinese"]
)

target_lang = st.selectbox(
    "Select Target Language",
    options=["French", "Spanish", "German", "Chinese", "English"]
)

if st.button("Translate"):
    if text:
        with st.spinner('Translating text...'):
            translation = translate_text(text, source_lang, target_lang)
            st.write("### Translation")
            st.write(translation)
    else:
        st.warning("Please enter some text to translate.")

        
st.markdown("---")
st.markdown("Hello|Hola|Namaste|Konnichiwa")
