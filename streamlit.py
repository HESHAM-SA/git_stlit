import streamlit as st 
import joblib

st.title('Model to predict a salary')

model = joblib.load('linear_model.pkl')

x = st.slider('experiance', 0, 40)
y = model.predict([[x]])

st.write('Salary : ',y )
