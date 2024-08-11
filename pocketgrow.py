import streamlit as st
from datetime import datetime, timedelta

# Function to calculate days remaining until the next billing cycle
def days_until_next_billing(renewal_date):
    today = datetime.today().date()
    if renewal_date < today:
        renewal_date = renewal_date + timedelta(days=30)
    return (renewal_date - today).days

# Function to check if the subscription is worth it
def is_worth_it(cost, daily_usage_hours, daily_usage_minutes):
    total_daily_usage = daily_usage_hours + daily_usage_minutes / 60
    if total_daily_usage < 0.5:  # Less than 30 minutes per day
        return False
    weekly_usage = total_daily_usage * 7
    monthly_usage = weekly_usage * 4
    cost_per_hour = cost / monthly_usage
    return cost_per_hour <= 100  # Worth it if cost per hour is less than or equal to INR 100

# Initialize session state to store subscriptions
if "subscriptions" not in st.session_state:
    st.session_state.subscriptions = []

# Streamlit UI
st.title("Subscription Handling App")

st.sidebar.header("Add a New Subscription")

# Inputs for new subscription
name = st.sidebar.text_input("Subscription Name")
cost = st.sidebar.number_input("Monthly Cost (INR)", min_value=0)
renewal_date = st.sidebar.date_input("Next Billing Date", min_value=datetime.today().date())
daily_usage_hours = st.sidebar.slider("Daily Usage Hours", 0, 24, 1)
daily_usage_minutes = st.sidebar.slider("Daily Usage Minutes", 0, 59, 0)

# Check if the subscription name already exists
def name_exists(name):
    return any(sub['name'] == name for sub in st.session_state.subscriptions)

# Button to add subscription
if st.sidebar.button("Add Subscription"):
    if name and cost >= 0 and renewal_date:
        if name_exists(name):
            st.sidebar.error("Subscription with this name already exists!")
        else:
            st.session_state.subscriptions.append({
                "name": name,
                "cost": cost,
                "renewal_date": renewal_date,
                "daily_usage_hours": daily_usage_hours,
                "daily_usage_minutes": daily_usage_minutes
            })
            st.sidebar.success(f"Added {name} subscription!")
    else:
        st.sidebar.error("Please fill all fields!")

# Button to clear all subscriptions
if st.sidebar.button("Clear All Subscriptions"):
    st.session_state.subscriptions = []
    st.sidebar.success("All subscriptions cleared!")

# Display all subscriptions
st.header("Your Subscriptions")
total_cost = 0
suggestions = {"keep": [], "reconsider": []}

if st.session_state.subscriptions:
    for sub in st.session_state.subscriptions:
        # Ensure that all required keys are present
        if all(key in sub for key in ["name", "cost", "renewal_date", "daily_usage_hours", "daily_usage_minutes"]):
            st.write(f"**{sub['name']}**")
            st.write(f"Cost: INR {sub['cost']}")
            st.write(f"Next Billing Date: {sub['renewal_date'].strftime('%d %B, %Y')}")
            days_left = days_until_next_billing(sub['renewal_date'])
            st.write(f"Days until next billing: {days_left} days")
            
            # Calculate usage
            daily_usage_hours = sub['daily_usage_hours']
            daily_usage_minutes = sub['daily_usage_minutes']
            total_daily_usage = daily_usage_hours + daily_usage_minutes / 60
            weekly_usage = total_daily_usage * 7
            monthly_usage = weekly_usage * 4
            cost_per_hour = sub['cost'] / monthly_usage
            
            st.write(f"Daily Usage: {daily_usage_hours} hours {daily_usage_minutes} minutes")
            st.write(f"Weekly Usage: {weekly_usage} hours")
            st.write(f"Monthly Usage: {monthly_usage} hours")
            st.write(f"Cost per Hour: INR {cost_per_hour:.2f}")
            
            # Suggest whether to keep or reconsider
            if total_daily_usage < 0.5:
                st.write("❌ **You might want to reconsider this subscription as it's used less than 30 minutes per day.**")
                suggestions["reconsider"].append(sub['name'])
            elif is_worth_it(sub['cost'], daily_usage_hours, daily_usage_minutes):
                st.write("✅ **This subscription is worth it based on your usage.**")
                suggestions["keep"].append(sub['name'])
            else:
                st.write("❌ **You might want to reconsider this subscription.**")
                suggestions["reconsider"].append(sub['name'])
            
            st.write("---")
            total_cost += sub['cost']
        else:
            st.write("**Error: Missing data in subscription entry**")
    
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
