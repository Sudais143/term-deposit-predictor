
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("term_deposit_model.pkl")

st.title("Term Deposit Subscription Predictor")

st.markdown("Enter client information below to predict the likelihood of subscribing to a term deposit.")

# User inputs
age = st.slider("Age", 18, 95, 30)
job = st.selectbox("Job", ['admin.', 'technician', 'services', 'blue-collar', 'retired', 'management', 'self-employed', 'unemployed', 'entrepreneur', 'student', 'housemaid', 'unknown'])
marital = st.selectbox("Marital Status", ['married', 'single', 'divorced'])
education = st.selectbox("Education", ['basic.4y', 'basic.6y', 'basic.9y', 'high.school', 'university.degree', 'professional.course', 'illiterate', 'unknown'])
housing = st.radio("Housing Loan", ['yes', 'no'])
loan = st.radio("Personal Loan", ['yes', 'no'])
contact = st.selectbox("Contact Type", ['cellular', 'telephone'])
month = st.selectbox("Last Contact Month", ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
campaign = st.slider("Number of Contacts During Campaign", 1, 50, 1)
pdays = st.slider("Days Since Last Contact", -1, 999, -1)
previous = st.slider("Previous Contacts", 0, 50, 0)
poutcome = st.selectbox("Outcome of Previous Campaign", ['unknown', 'other', 'failure', 'success'])

# Construct input data
input_dict = {
    'age': age,
    'campaign': campaign,
    'pdays': pdays,
    'previous': previous,
    'job_' + job: 1,
    'marital_' + marital: 1,
    'education_' + education: 1,
    'housing_yes' if housing == 'yes' else 'housing_no': 1,
    'loan_yes' if loan == 'yes' else 'loan_no': 1,
    'contact_' + contact: 1,
    'month_' + month: 1,
    'poutcome_' + poutcome: 1
}

# Generate full feature vector with 0s and override with input_dict
all_features = model.feature_names_in_
input_data = pd.DataFrame([{feat: 0 for feat in all_features}])
for key in input_dict:
    if key in input_data.columns:
        input_data[key] = input_dict[key]

# Prediction
if st.button("Predict"):
    proba = model.predict_proba(input_data)[0, 1]
    prediction = model.predict(input_data)[0]
    st.success(f"Prediction: {'Subscribed' if prediction else 'Not Subscribed'}")
    st.info(f"Probability of Subscription: {proba:.2%}")
