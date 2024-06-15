import streamlit as st
import requests

# Streamlit app configuration
st.title("Intelligent Tax Assistant")

# User profile input
st.header("User Profile")
income = st.number_input("Income")
investments = st.number_input("Investments")
expenses = st.number_input("Expenses")
marital_status = st.selectbox("Marital Status", ["Single", "Married"])
dependents = st.number_input("Dependents", min_value=0)
employment_status = st.selectbox("Employment Status", ["Employed", "Self-Employed", "Unemployed"])

profile = {
    "income": income,
    "investments": investments,
    "expenses": expenses,
    "maritalStatus": marital_status,
    "dependents": dependents,
    "employmentStatus": employment_status,
}

if st.button("Submit Profile"):
    response = requests.post("http://backend:5000/profile", json=profile)
    st.write(response.json())

if st.button("Calculate Taxes"):
    response = requests.post("http://backend:5000/calculate-taxes", json=profile)
    st.write("Estimated Taxes:", response.json().get('taxes'))

# Document upload
st.header("Upload Document")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post("http://backend:5000/upload-document", files=files)
    st.write(response.json())

# Ask a question
st.header("Ask a Tax Question")
question = st.text_input("Your Question")
if st.button("Submit Question"):
    response = requests.post("http://backend:5000/ask-question", json={"question": question})
    st.write(response.json())
