import streamlit as st
from datetime import datetime, timedelta

# Function to calculate days remaining until the next billing cycle
def days_until_next_billing(renewal_date):
    today = datetime.today().date()
    if renewal_date < today:
        renewal_date = renewal_date + timedelta(days=30)
    return (renewal_date - today).days

# Function to check if the subscription is worth it
def is_worth_it(cost, usage_per_week):
    if usage_per_week == 0:
        return False  # If usage is 0, it's not worth it
    cost_per_use = cost / (usage_per_week * 4)  # Monthly usage
    return cost_per_use <= 100  # Worth it if cost per hour is less than or equal to INR 100

# Streamlit UI
st.title("Subscription Handling App")

st.sidebar.header("Add a New Subscription")

# Inputs for new subscription
name = st.sidebar.text_input("Subscription Name")
cost = st.sidebar.number_input("Monthly Cost (INR)", min_value=0)
renewal_date = st.sidebar.date_input("Next Billing Date", min_value=datetime.today().date())
usage_per_week = st.sidebar.slider("Usage per Week (in hours)", 0, 40, 5)

# Initialize session state to store subscriptions
if "subscriptions" not in st.session_state:
    st.session_state.subscriptions = []

# Button to add subscription
if st.sidebar.button("Add Subscription"):
    if name and cost > 0 and renewal_date:
        st.session_state.subscriptions.append({
            "name": name,
            "cost": cost,
            "renewal_date": renewal_date,
            "usage_per_week": usage_per_week
        })
        st.sidebar.success(f"Added {name} subscription!")
    else:
        st.sidebar.error("Please fill all fields!")

# Display all subscriptions
st.header("Your Subscriptions")
total_cost = 0
suggestions = {"keep": [], "reconsider": []}

if st.session_state.subscriptions:
    for sub in st.session_state.subscriptions:
        st.write(f"**{sub['name']}**")
        st.write(f"Cost: INR {sub['cost']}")
        st.write(f"Next Billing Date: {sub['renewal_date'].strftime('%d %B, %Y')}")
        days_left = days_until_next_billing(sub['renewal_date'])
        st.write(f"Days until next billing: {days_left} days")
        
        # Suggest whether to keep or reconsider
        if is_worth_it(sub['cost'], sub['usage_per_week']):
            st.write("✅ **This subscription is worth it based on your usage.**")
            suggestions["keep"].append(sub['name'])
        else:
            st.write("❌ **You might want to reconsider this subscription.**")
            suggestions["reconsider"].append(sub['name'])
        
        st.write("---")
        total_cost += sub['cost']

    st.write(f"**Total Monthly Cost: INR {total_cost}**")

    st.header("Monthly Recommendations")
    if suggestions["keep"]:
        st.write("### Subscriptions to Keep:")
        for item in suggestions["keep"]:
            st.write(f"- {item}")

    if suggestions["reconsider"]:
        st.write("### Subscriptions to Reconsider:")
        for item in suggestions["reconsider"]:
            st.write(f"- {item}")
else:
    st.write("No subscriptions added yet.")
