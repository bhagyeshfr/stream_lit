import streamlit as st

# App title
st.title("Student Investment and Savings Tracker")

# Input fields for pocket money, basic expenses, and investment
st.header("Enter Your Monthly Financial Details")

pocket_money = st.number_input("Monthly Pocket Money (in $)", min_value=0.0, step=1.0)
basic_expenses = st.number_input("Basic Monthly Expenses (in $)", min_value=0.0, step=1.0)
investment = st.number_input("Monthly Investment (in $)", min_value=0.0, step=1.0)

# Calculate remaining savings
remaining_savings = pocket_money - (basic_expenses + investment)

# Display the results
st.subheader("Summary")
st.write(f"Pocket Money: ${pocket_money}")
st.write(f"Basic Expenses: ${basic_expenses}")
st.write(f"Monthly Investment: ${investment}")
st.write(f"Remaining Savings: ${remaining_savings}")

# Visualize the breakdown
st.subheader("Monthly Financial Breakdown")

# Pie chart data
labels = ['Basic Expenses', 'Investment', 'Remaining Savings']
sizes = [basic_expenses, investment, remaining_savings]

# Check if the total is positive before showing the pie chart
if remaining_savings >= 0:
    st.pie_chart(sizes, labels=labels)
else:
    st.write("Your expenses and investments exceed your pocket money. Please adjust your budget.")

# Tips for students
st.subheader("Financial Tips for Students")
st.write("""
- Always try to save at least 20% of your pocket money.
- Invest wisely; even small amounts can grow over time.
- Keep track of your expenses to avoid overspending.
- Consider using a budgeting app for better financial management.
""")
