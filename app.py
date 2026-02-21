import streamlit as st
import pandas as pd
import numpy as np
import joblib


model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("Employee Performance Prediction")

st.markdown("""
This app predicts employee performance rating based on various factors.
Adjust the inputs below and click **Predict Performance** to get the result.
""")

st.write("Please enter the employee details below:")

age = st.number_input("Age", 18, 100, 35)

EmpEnvironmentSatisfaction = st.selectbox("Employee Environment Satisfaction (1=Low, 2=Medium, 3=High, 4=Very High)", [1, 2, 3, 4], index=2)
job_level = st.slider("Job Level", 1, 5, 3)
job_sat = st.slider("Job Satisfaction", 1, 4, 3)

EmpLastSalaryHikePercent = st.number_input("Last Salary Hike Percent", 0, 50, 15)
EmpWorkLifeBalance = st.selectbox("Work-Life Balance (1=Bad, 2=Average, 3=Good, 4=Best)", [1, 2, 3, 4], index=2)

years_company = st.number_input("Years at Company", 0, 40, 5)
years_role = st.number_input("Years in Current Role", 0, 40, 3)
years_promo = st.number_input("Years Since Last Promotion", 0, 40, 1)
years_manager = st.number_input("Years with Current Manager", 0, 40, 2)
years_manager = st.number_input("Years With Current Manager", 0,40)


input_df = pd.DataFrame({
    'Age': [age],
    'EmpEnvironmentSatisfaction': [EmpEnvironmentSatisfaction],
    'EmpJobLevel': [job_level],
    'EmpJobSatisfaction': [job_sat],
    'EmpLastSalaryHikePercent': [EmpLastSalaryHikePercent],
    'EmpWorkLifeBalance': [EmpWorkLifeBalance ],
    'ExperienceYearsAtThisCompany': [years_company],
    'ExperienceYearsInCurrentRole': [years_role],
    'YearsSinceLastPromotion': [years_promo],
    'YearsWithCurrManager': [years_manager]
})


input_data_scaled = pd.DataFrame(scaler.transform(input_df), columns=input_df.columns)
prediction = model.predict(input_data_scaled)[0]
probability = np.max(model.predict_proba(input_data_scaled)[0])


if st.button("Predict Performance"):

    PerformanceRating = {1: "Low", 2: "Good", 3: "Excellent", 4: "Outstanding"}
    Predicted_Performance = PerformanceRating[prediction]
    st.success(f"Predicted Performance: **{Predicted_Performance}**")
    st.info(f"Confidence: {probability:.2%}")

    # Optional: Show input summary
    st.subheader("Input Summary")
    st.write(f"Age: {age}, Job Level: {job_level}, Job Satisfaction: {job_sat}")
    st.write(f"Environment Satisfaction: {EmpEnvironmentSatisfaction}, Work-Life Balance: {EmpWorkLifeBalance}")
    st.write(f"Last Salary Hike: {EmpLastSalaryHikePercent}%, Years at Company: {years_company}")