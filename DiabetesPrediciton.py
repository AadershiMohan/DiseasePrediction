# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""


import pickle
import streamlit as st


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

# sidebar for navigate

# Diabetes Prediction
st.title('Diabetes Prediction using ML')

    # getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:
  Pregnancies = st.text_input('Number of Pregnancies')
with col2:
  Glucose = st.text_input('Glucose level')
with col3:
  BloodPressure = st.text_input('Blood Pressure value')
with col1:
  SkinThickness = st.text_input('Skin Thickness value')
with col2:
  Insulin = st.text_input('Insulin level')
with col3:
  BMI = st.text_input('BMI value')
with col1:
  DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
with col2:
  Age = st.text_input('Age of the Person')

# code for Prediction
diab_diagnosis = ''

# creating a button for prediction
if st.button('Diabetes Test Result'):
  diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure,SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
  if (diab_prediction[0]==1):
      diab_diagnosis = 'The person is Diabetic'
  else:
    diab_diagnosis = 'The person is not Diabetic'
st.success(diab_diagnosis)

