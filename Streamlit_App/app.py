import streamlit as st
import pandas as pd
import pickle

# Load Model
model = pickle.load(open("loan_model.pkl", "rb"))

st.set_page_config(page_title="Loan Approval Prediction", page_icon="🏦")

st.title("Loan Approval Prediction System")

gender = st.selectbox("Gender", ["Male", "Female"])

married = st.selectbox("Married", ["No", "Yes"])

dependents = st.selectbox("Dependents", [0, 1, 2, 3])

education = st.selectbox("Education", ["Graduate", "Not Graduate"])

self_employed = st.selectbox("Self Employed", ["No", "Yes"])

applicant_income = st.number_input(
    "Applicant Income",
    min_value=0,
    value=5000,
    step=100
)

coapplicant_income = st.number_input(
    "Coapplicant Income",
    min_value=0,
    value=0,
    step=100
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0,
    value=120
)

loan_amount_term = st.number_input(
    "Loan Amount Term",
    min_value=0,
    value=360
)

credit_history = st.selectbox("Credit History", [1, 0])

property_area = st.selectbox(
    "Property Area",
    ["Rural", "Semiurban", "Urban"]
)

if st.button("Predict Loan Status"):

    total_income = applicant_income + coapplicant_income

    gender = 1 if gender == "Male" else 0
    married = 1 if married == "Yes" else 0
    education = 0 if education == "Graduate" else 1
    self_employed = 1 if self_employed == "Yes" else 0

    property_dict = {
        "Rural": 0,
        "Semiurban": 1,
        "Urban": 2
    }

    property_area = property_dict[property_area]

    data = pd.DataFrame([[
        gender,
        married,
        dependents,
        education,
        self_employed,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_amount_term,
        credit_history,
        property_area,
        total_income
    ]], columns=[
        "Gender",
        "Married",
        "Dependents",
        "Education",
        "Self_Employed",
        "ApplicantIncome",
        "CoapplicantIncome",
        "LoanAmount",
        "Loan_Amount_Term",
        "Credit_History",
        "Property_Area",
        "TotalIncome"
    ])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")