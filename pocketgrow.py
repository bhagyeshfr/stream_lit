import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def main():
    st.title("BMI Calculator")

    st.write("This application calculates your Body Mass Index (BMI) based on your weight and height.")

    weight = st.number_input("Enter your weight (in kilograms):", min_value=0.0, step=0.1)
    height = st.number_input("Enter your height (in meters):", min_value=0.0, step=0.01)

    if st.button("Calculate BMI"):
        if weight > 0 and height > 0:
            bmi = calculate_bmi(weight, height)
            st.success(f"Your BMI is: {bmi:.2f}")

            if bmi < 18.5:
                st.info("You are underweight.")
            elif 18.5 <= bmi < 24.9:
                st.info("You have a normal weight.")
            elif 25 <= bmi < 29.9:
                st.info("You are overweight.")
            else:
                st.info("You are obese.")
        else:
            st.error("Please enter valid values for weight and height.")

if __name__ == "__main__":
    main()

