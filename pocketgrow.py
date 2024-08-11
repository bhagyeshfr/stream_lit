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
    basic_expenses = st.number_input("Monthly Expenses (in INR)", min_value=0.0, step=
