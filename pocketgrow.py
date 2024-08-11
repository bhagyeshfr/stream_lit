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
        
        # Append data for display
        subscription_data.append({
            "Name": sub['name'],
            "Cost (INR)": sub['cost'],
            "Next Billing Date": sub['renewal_date'].strftime('%d %B, %Y'),
            "Daily Usage": f"{daily_usage_hours} hours {daily_usage_minutes} minutes",
            "Weekly Usage (hours)": f"{weekly_usage:.2f}",
            "Monthly Usage (hours)": f"{monthly_usage:.2f}",
            "Cost per Hour (INR)": f"{cost_per_hour:.2f}"
        })
        
        # Suggest whether to keep or reconsider
        if total_daily_usage < 0.5:
            suggestions["reconsider"].append(sub['name'])
        elif is_worth_it(sub['cost'], daily_usage_hours, daily_usage_minutes):
            suggestions["keep"].append(sub['name'])
        else:
            suggestions["reconsider"].append(sub['name'])
        
        total_cost += sub['cost']
    
    # Display data in a DataFrame
    st.dataframe(pd.DataFrame(subscription_data))
    
    st.write(f"*Total Monthly Cost: INR {total_cost}*")

    st.header("Monthly Recommendations")
    
    if suggestions["keep"]:
        st.markdown("### ✅ Subscriptions to Keep:")
        for item in suggestions["keep"]:
            st.write(f"- {item}")

    if suggestions["reconsider"]:
        st.markdown("### ❌ Subscriptions to Reconsider:")
        for item in suggestions["reconsider"]:
            st.write(f"- {item}")
else:
    st.write("No subscriptions added yet.")

# Visualization
if st.session_state.subscriptions:
    # Create a DataFrame for charting
    chart_data = pd.DataFrame({
        "Subscription": [sub['name'] for sub in st.session_state.subscriptions],
        "Cost per Hour (INR)": [sub['cost'] / ((sub['daily_usage_hours'] * 7 * 4) + (sub['daily_usage_minutes'] / 60 * 7 * 4)) for sub in st.session_state.subscriptions]
    })

    # Display the bar chart using Streamlit's built-in function
    st.bar_chart(chart_data.set_index("Subscription"))

