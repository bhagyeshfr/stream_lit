import streamlit as st
import pandas as pd
from datetime import datetime

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

# List of inappropriate terms
inappropriate_terms = ["porn", "pornhub", "nudes", "sex", "xxx", "brazzers"]

# Streamlit UI
st.title("Subscription Handling App")

st.sidebar.header("Add a New Subscription")

# Inputs for new subscription
name = st.sidebar.text_input("Subscription Name")
cost = st.sidebar.number_input("Monthly Cost (INR)", min_value=0)
renewal_date = st.sidebar.date_input("Next Billing Date", min_value=datetime.today().date())

col1, col2 = st.sidebar.columns([4, 1])
with col1:
    daily_usage_hours = st.slider("Daily Usage Hours", 0, 24, 1)
with col2:
    if st.button("Info", key="usage_info"):
        st.info("### Finding Daily Usage on Your Phone\n\n"
                "*For Android Users:*\n"
                "1. Open the Settings app.\n"
                "2. Go to 'Digital Wellbeing & Parental Controls'.\n"
                "3. Tap on 'Dashboard' or 'Screen Time' to view your daily app usage.\n\n"
                "*For iOS Users:*\n"
                "1. Open the Settings app.\n"
                "2. Tap 'Screen Time'.\n"
                "3. Go to 'See All Activity' to view your daily app usage.")

daily_usage_minutes = st.slider("Daily Usage Minutes", 0, 59, 0)

# Check if the subscription name already exists
def name_exists(name):
    return any(sub['name'] == name for sub in st.session_state.subscriptions)

# Button to add subscription
if st.sidebar.button("Add Subscription"):
    if name and cost >= 0 and renewal_date:
        # Check for inappropriate terms
        if any(term in name.lower() for term in inappropriate_terms):
            st.sidebar.error("Don't waste your money on this subscription!")
        elif name_exists(name):
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

if st.session_state.subscriptions:
    total_cost = 0
    suggestions = {"keep": [], "reconsider": []}
    
    subscription_data = []
    
    for sub in st.session_state.subscriptions:
        daily_usage_hours = sub['daily_usage_hours']
        daily_usage_minutes = sub['daily_usage_minutes']
        total_daily_usage = daily_usage_hours + daily_usage_minutes / 60
        weekly_usage = total_daily_usage * 7
        monthly_usage = weekly_usage * 4
        cost_per_hour = sub['cost'] / monthly_usage
        
        #
