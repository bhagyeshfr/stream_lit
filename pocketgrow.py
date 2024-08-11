import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

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

# Inp
