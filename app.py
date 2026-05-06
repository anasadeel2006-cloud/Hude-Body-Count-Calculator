import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")

st.title("⚖️ Body Mass Index (BMI) Calculator")

st.write("Enter your details below:")

# Inputs
weight = st.number_input("Weight (kg)", min_value=1.0)
height = st.number_input("Height (meters)", min_value=0.5)

# Button
if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)

        st.success(f"Your BMI is: {bmi:.2f}")

        # Category
        if bmi < 18.5:
            st.warning("Underweight")
        elif 18.5 <= bmi < 25:
            st.info("Normal weight")
        elif 25 <= bmi < 30:
            st.warning("Overweight")
        else:
            st.error("Obese")
    else:
        st.error("Height must be greater than zero")
    
