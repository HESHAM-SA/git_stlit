import streamlit as st
import pickle


st.title('STREAMLIT TITLE')
st.write('## Mark down')

import streamlit as st

# Function to load the model
def load_model():
    with open('linear_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Load the model
model = load_model()