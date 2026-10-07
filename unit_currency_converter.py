import streamlit as st

st.title("💱 Rabia's Live Currency & Unit Converter")
st.write("Convert international currencies and core physical metrics instantly.")

conversion_type = st.selectbox("Select Conversion Utility", ["Currency (USD to INR)", "Length (Meters to Feet)", "Weight (Kg to Pounds)"])

input_val = st.number_input("Enter value to convert:", value=1.0)

if conversion_type == "Currency (USD to INR)":
    result = input_val * 83.5
    st.success(f"Converted Value: ₹ {result:.2f}")
elif conversion_type == "Length (Meters to Feet)":
    result = input_val * 3.28084
    st.success(f"Converted Value: {result:.2f} Feet")
else:
    result = input_val * 2.20462
    st.success(f"Converted Value: {result:.2f} lbs")
