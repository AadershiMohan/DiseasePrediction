# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 10:52:53 2023

@author: AADERSHI MOHAN
"""


import pickle
import streamlit as st

# loading the saved models
heart_model = pickle.load(open('heart_model.sav', 'rb'))

# Heart Disease

st.title('Heart Disease Prediciton using ML')
 # getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:
  Sex = st.text_input('1 = male, 0 = female')
with col2:
  Cp = st.text_input('Chest Pain Type')
with col3:
  Trestbps = st.text_input('Resting Bp in mm Hg')
with col1:
  Chol = st.text_input('Serum Cholestoral in mg/dl')
with col2:
  Fbs = st.text_input('Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)')
with col3:
  Restecg = st.text_input('Resting electrocardigraphic ')
with col1:
  Thalach = st.text_input('Maximum heart rate achieved')
with col2:
  Exang = st.text_input('Exercisee induced angina (1 = yes, 0 = no)')
with col3:
  Oldpeak = st.text_input('ST depression induced by exercise relative to rest')
with col1:
  Slope = st.text_input('The slope of the peak exercise ST segment')
with col2:
  Ca = st.text_input('number of major vessels (0-3) colored by flourosopy')
with col3:
  Thal = st.text_input('3 = normal; 6 = fixed defect; 7 = reversable defect')
with col1:
  Age = st.text_input('Age of the Person')

# code for Prediction
heart_diagnosis = ''

# creating a button for prediction
if st.button('Heart Test Result'):
  heart_prediction = heart_model.predict([[ Sex, Cp, Trestbps, Chol, Fbs, Restecg, Thalach, Exang, Oldpeak, Slope, Ca, Thal, Age ]])
  if (heart_prediction[0]==1):
    heart_diagnosis = 'The person has a Heart Disease.'
  else:
    heart_diagnosis = 'The person does not have a Heart Disease.'
st.success(heart_diagnosis)

