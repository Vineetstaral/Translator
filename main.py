import streamlit as st
import requests

TRANSLATION_API_URL = "https://api-inference.huggingface.co/models/google-t5/t5-small"

def translate_text(text):
    """
    Translate the input text from English to defined language.
    """
    try:
        payload = {"inputs": text}
        response = requests.post(TRANSLATION_API_URL, json=payload)
        response.raise_for_status() 
        translation = response.json()[0]["translation_text"]
        return translation
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

st.title("Real-Time Language Translator")
st.write("Enter text in English ")

text = st.text_area("Input Text")

if st.button("Translate"):
    if text:
        with st.spinner('Translating text...'):
            translation = translate_text(text)
            st.write("### Translation")
            st.write(translation)
    else:
        st.warning("Please enter some text to translate.")

st.markdown("---")
st.markdown("Hello|Konichiwa")
