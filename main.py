import streamlit as st
import requests
import io
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()

# Sentiment Analysis
SENTIMENT_API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
SENTIMENT_HEADERS = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

def query_sentiment(payload):
    response = requests.post(SENTIMENT_API_URL, headers=SENTIMENT_HEADERS, json=payload)
    return response.json()

# Text Summarization
SUMMARIZATION_API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
SUMMARIZATION_HEADERS = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

def query_summarization(payload):
    response = requests.post(SUMMARIZATION_API_URL, headers=SUMMARIZATION_HEADERS, json=payload)
    return response.json()

# Question Answering
QA_API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
QA_HEADERS = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

def query_qa(payload):
    response = requests.post(QA_API_URL, headers=QA_HEADERS, json=payload)
    return response.json()

st.title("Hugging Face API Demo")

# Sentiment Analysis Section
st.header("Sentiment Analysis")
sentiment_text = st.text_area("Enter text for sentiment analysis:")
if st.button("Analyze Sentiment"):
    if sentiment_text:
        with st.spinner("Analyzing sentiment..."):
            sentiment_result = query_sentiment({"inputs": sentiment_text})
            if sentiment_result:
                st.write(f"**Sentiment:** {sentiment_result[0][0]['label']}")
                st.write(f"**Confidence:** {sentiment_result[0][0]['score']:.4f}")
            else:
                st.error("Error analyzing sentiment.")
    else:
        st.warning("Please enter text for sentiment analysis.")

# Text Summarization Section
st.header("Text Summarization")
summarization_text = st.text_area("Enter text for summarization:")
if st.button("Summarize"):
    if summarization_text:
        with st.spinner("Summarizing text..."):
            summarization_result = query_summarization({"inputs": summarization_text})
            if summarization_result and "summary_text" in summarization_result[0]:
                st.write(f"**Summary:** {summarization_result[0]['summary_text']}")
            else:
                st.error("Error summarizing text.")
    else:
        st.warning("Please enter text for summarization.")

# Question Answering Section
st.header("Question Answering")
qa_context = st.text_area("Enter context for question answering:")
qa_question = st.text_input("Enter your question:")
if st.button("Answer Question"):
    if qa_context and qa_question:
        with st.spinner("Answering question..."):
            qa_result = query_qa({"inputs": {"question": qa_question, "context": qa_context}})
            if qa_result and "answer" in qa_result:
                st.write(f"**Answer:** {qa_result['answer']}")
                st.write(f"**Score:** {qa_result['score']:.4f}")
            else:
                st.error("Error answering question.")
    else:
        st.warning("Please enter context and question.")

st.markdown("---")
st.markdown("Using Free Hugging Face Models")
