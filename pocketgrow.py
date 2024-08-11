import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def main():
    st.title("BMI Calculator")

    st.write("This application calculates your Body Mass Index (BMI) based on your weight and height.")

    # BMI Calculation Section
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

    # Subscription Tracking Section
    st.write("### Subscription Tracker")

    # List of common subscriptions
    common_subscriptions = [
        "Netflix",
        "Spotify",
        "Amazon Prime",
        "Disney+",
        "Hulu",
        "YouTube Premium",
        "HBO Max",
        "Apple TV+",
    ]

    # Dropdown for common subscriptions
    selected_subscription = st.selectbox("Select Subscription Name", common_subscriptions)

    # Text input for new subscriptions
    new_subscription = st.text_input("Add a new subscription (if not listed above):")

    # Button to add the new subscription
    if st.button("Add Subscription"):
        if new_subscription and new_subscription not in common_subscriptions:
            common_subscriptions.append(new_subscription)
            st.success(f"'{new_subscription}' has been added to the list.")
        elif new_subscription in common_subscriptions:
            st.warning(f"'{new_subscription}' is already in the list.")
        else:
            st.error("Please enter a subscription name.")

    # Display selected subscription
    st.write(f"Selected Subscription: {selected_subscription}")

if __name__ == "__main__":
    main()

