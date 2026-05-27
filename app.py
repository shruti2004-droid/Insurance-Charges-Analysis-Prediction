import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("insurance_model.pkl", "rb"))

# Title
st.title("Insurance Charges Prediction App")

st.write("Enter customer details below:")

# User Inputs
age = st.number_input("Age", min_value=18, max_value=100)

sex = st.selectbox("Sex", ["Male", "Female"])

bmi = st.number_input("BMI")

children = st.number_input("Children", min_value=0, max_value=10)

smoker = st.selectbox("Smoker", ["Yes", "No"])

region = st.selectbox(
    "Region",
    ["Southwest", "Southeast", "Northwest", "Northeast"]
)

# Encoding
sex = 0 if sex == "Male" else 1

smoker = 1 if smoker == "Yes" else 0

region_dict = {
    "Southwest":0,
    "Southeast":1,
    "Northwest":2,
    "Northeast":3
}

region = region_dict[region]

# Prediction
if st.button("Predict Insurance Charges"):

    input_data = np.array(
        [[age, sex, bmi, children, smoker, region]]
    )

    prediction = model.predict(input_data)

    st.success(
        f"Estimated Insurance Charges: ${prediction[0]:,.2f}"
    )