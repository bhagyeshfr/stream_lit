import streamlit as st

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

def main():
    st.title("Subscription Tracker")

    st.write("Select a subscription from the dropdown or add a new one.")

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

