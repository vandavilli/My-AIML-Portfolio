# Import required libraries
import streamlit as st
from transformers import pipeline

# Initialize sentiment-analysis pipeline
nlp = pipeline("sentiment-analysis")

def analyze(text):
    result = nlp(text)[0]
    return result['label'], round(result['score'], 4)

# Title
st.title("NLP Sentiment Analysis")

# User input
text = st.text_area("Enter text for sentiment analysis", "")

# Analyze button
if st.button('Analyze'):
    if text == '':
        st.write('Please enter some text for analysis.')
    else:
        sentiment, score = analyze(text)
        st.write(f'Sentiment: {sentiment}, Score: {score}')
