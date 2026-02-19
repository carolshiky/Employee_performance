import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load('model (2).pkl')
scaler = joblib.load('scaler (2).pkl')

st.title("Employee Performance Prediction")

st.write ("Please select the details below:")   
sex=st.selectbox('Sex', ['male', 'female'])
maritalstatus=st.selectbox('marital_status', ['single', 'married', 'divorced'])
overtime=st.selectbox('overtime', ['Yes', 'No'])
Attrition=st.selectbox('attrition', ['Yes', 'No'])
age = st.slider("Age",0,100,25)
education_background = st.selectbox('education_background', ['life_science', 'medical', 'marketing', 'technical_degree','Human_resource', 'other'])
employee_department = st.selectbox('employee_department', ['Sales','Development','Research&Development','Human_Resource','Finance','Data_Science'])
emp_enviroment_satisfaction = st.selectbox ("employee_enviroment_satisfaction (1 = 1st),2 = 2nd, 3 = 3rd, 4 =4th, 5 =5th)",[1,2,3,4,5])
emp_job_satisfaction = st.selectbox ("employee_job_satisfaction (1 = 1st),2 = 2nd, 3 = 3rd, 4 =4th)",[1,2,3,4,])




