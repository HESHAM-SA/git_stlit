import streamlit as st 
import joblip 

st.title('Model to predict a salary')

model = joblip.load('linear_model.pkl')

x = st.slider('experiance', 0, 40)
y = model.predict([[x]])