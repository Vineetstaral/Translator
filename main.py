import streamlit as st
import requests

# Hugging Face model API endpoint for T5
T5_API_URL = "https://huggingface.co/google-t5/t5-small"

def translate_text(text, source_lang, target_lang):
    """
    Translate the input text using the T5 model.
    """
    try:
        task = f"translate {source_lang} to {target_lang}: {text}"
        payload = {"inputs": task}
        response = requests.post(T5_API_URL, json=payload)
        response.raise_for_status() 
        translation = response.json()[0]["generated_text"]
        return translation
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"


st.title(" Real-Time Translation ")
st.write("Enter text and select the source and target languages for translation:")

text = st.text_area("Input Text")

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
