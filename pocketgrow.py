import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Student Savings and Investment Guide")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["Home", "Track Savings", "Investment Options", "Learning Resources"])

# Home Page
if options == "Home":
    st.header("Welcome to the Student Savings and Investment Guide!")
    st.write("""
    This app will help you learn how to save and grow your pocket money by making smart investment choices.
    Navigate through the different sections to explore features that will assist you in your financial journey.
    """)

# Track Savings
elif options == "Track Savings":
    st.header("Track Your Savings")
    
    # Input fields for pocket money, expenses, and savings
    pocket_money = st.number_input("Monthly Pocket Money (in INR)", min_value=0.0, step=100.0)
    basic_expenses = st.number_input("Monthly Expenses (in INR)", min_value=0.0, step=100.0)
    
    # Calculate savings
    savings = pocket_money - basic_expenses
    st.write(f"Your monthly savings: ₹{savings}")
    
    # DataFrame to track savings over time
    if 'savings_data' not in st.session_state:
        st.session_state['savings_data'] = pd.DataFrame(columns=["Month", "Savings"])
    
    month = st.text_input("Month")
    if st.button("Add Savings"):
        new_data = {"Month": month, "Savings": savings}
        st.session_state['savings_data'] = st.session_state['savings_data'].append(new_data, ignore_index=True)
    
    # Display the savings DataFrame
    st.write(st.session_state['savings_data'])
    
    # Plot savings over time
    st.subheader("Savings Over Time")
    plt.plot(st.session_state['savings_data']["Month"], st.session_state['savings_data']["Savings"], marker='o')
    plt.xlabel("Month")
    plt.ylabel("Savings (INR)")
    st.pyplot(plt)

# Investment Options
elif options == "Investment Options":
    st.header("Explore Basic Investment Options")
    
    st.write("""
    Here are some simple investment options you can start with:
    1. **Recurring Deposits (RD):** A safe option to earn interest on your savings.
    2. **Systematic Investment Plan (SIP):** Invest small amounts regularly in mutual funds.
    3. **Fixed Deposits (FD):** A low-risk investment with guaranteed returns.
    4. **Stocks or ETFs:** Higher risk but potentially higher returns.
    """)
    
    # Add a simple ROI calculator
    st.subheader("Calculate Potential Returns")
    investment_amount = st.number_input("Investment Amount (in INR)", min_value=0.0, step=100.0)
    interest_rate = st.slider("Estimated Interest Rate (%)", min_value=0.0, max_value=20.0, step=0.5)
    years = st.slider("Investment Duration (Years)", min_value=1, max_value=10, step=1)
    
    # Calculate returns
    returns = investment_amount * ((1 + interest_rate/100) ** years)
    st.write(f"Estimated returns after {years} years: ₹{returns:.2f}")

# Learning Resources
elif options == "Learning Resources":
    st.header("Learn About Finance and Investing")
    
    st.write("""
    Here are some resources to help you get started with financial literacy:
    - **Books:** "Rich Dad Poor Dad" by Robert Kiyosaki, "The Little Book of Common Sense Investing" by John C. Bogle.
    - **YouTube Channels:** "The Financial Diet", "Graham Stephan", "Investing with Rose".
    - **Websites:** [Investopedia](https://www.investopedia.com), [Moneycontrol](https://www.moneycontrol.com).
    - **Online Courses:** "Personal Finance 101" on Coursera, "Introduction to Investing" on Udemy.
    """)

