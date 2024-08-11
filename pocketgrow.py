import streamlit as st
from datetime import datetime, timedelta

# Function to calculate days remaining until the next billing cycle
def days_until_next_billing(renewal_date):
    today = datetime.today().date()
    if renewal_date < today:
        renewal_date = renewal_date + timedelta(days=30)
    return (renewal_date - today).days

# Function to display subscription details
def display_subscription(name, cost, renewal_date):
    st.write(f"**{name}**")
    st.write(f"Cost: INR {cost}")
    st.write(f"Next Billing Date: {renewal_date.strftime('%d %B, %Y')}")
    days_left = days_until_next_billing(renewal_date)
    st.write(f"Days until next billing: {days_left} days")
    st.write("---")

# Streamlit UI
st.title("Media Subscription Manager")

st.sidebar.header("Add a New Subscription")

# Inputs for new subscription
name = st.sidebar.text_input("Subscription Name")
cost = st.sidebar.number_input("Monthly Cost (INR)", min_value=0)
renewal_date = st.sidebar.date_input("Next Billing Date")

# List to hold subscription details
if "subscriptions" not in st.session_state:
    st.session_state.subscriptions = []

# Button to add subscription
if st.sidebar.button("Add Subscription"):
    if name and cost > 0 and renewal_date:
        st.session_state.subscriptions.append({
            "name": name,
            "cost": cost,
            "renewal_date": renewal_date
        })
        st.sidebar.success(f"Added {name} subscription!")
    else:
        st.sidebar.error("Please fill all fields!")

# Display all subscriptions
st.header("Your Subscriptions")
total_cost = 0
if st.session_state.subscriptions:
    for sub in st.session_state.subscriptions:
        display_subscription(sub["name"], sub["cost"], sub["renewal_date"])
        total_cost += sub["cost"]

    st.write(f"**Total Monthly Cost: INR {total_cost}**")
else:
    st.write("No subscriptions added yet.")

