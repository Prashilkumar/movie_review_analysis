## Import all the libraries
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model

## Load the IMDB Dataset word index
word_index = imdb.get_word_index()
reverse_word_index = {value:key for key,value in word_index.items()}

# load pretrained model with tanh activation
model = load_model('best_model.h5')


## Function to Decode reviews
def decode_review(encoded_review):
    return " ".join([reverse_word_index.get(i-3,'?') for i in encoded_review])

# function to preprocess input
def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word,2)+3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review],maxlen=500)
    return padded_review




## Streamlit App
import streamlit as st

st.title("IMDB Movie Review Sentiment Analysis")
st.write('Enter a movie review to classify it as positive or negative')

# User input
user_input = st.text_area('Movie Review')
try: 
    if st.button('Classify'):
        preprocess_input = preprocess_text(user_input)

        ## make prediction 
        prediction = model.predict(preprocess_input)
        sentiment = 'Positive' if prediction[0][0]>0.5 else 'Negative'

        ## Display the result
        st.write (f'Sentimen:{sentiment}')
        st.write(f'Prediction Score: {prediction[0][0]}')

    else:
        st.write('Please enter a movie review.' )        
except Exception as e:
    st.error("Sorry, we couldn't analyze the review. Please try a different input with clearer and more descriptive language.")


# Show some example reviews to guide the user
with st.expander("💡 Need inspiration? Click here to see sample reviews"):
    st.markdown("""
    **Sample Positive Reviews:**
    - *"This movie was absolutely fantastic! The performances were top-notch and the story was deeply moving."*
    - *"A brilliant masterpiece. One of the best films I've seen in years!"*

    **Sample Negative Reviews:**
    - *"The plot was weak and the acting was terrible. I wouldn't recommend it."*
    - *"A complete waste of time. The movie lacked depth and originality."*
    """)
