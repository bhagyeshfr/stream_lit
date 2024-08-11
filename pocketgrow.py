import streamlit as st

# App title
st.title("Student Investment and Savings Tracker (INR)")

# Input fields for pocket money, basic expenses, and investment
st.header("Enter Your Monthly Financial Details")

pocket_money = st.number_input("Monthly Pocket Money (in INR)", min_value=0.0, step=100.0)
basic_expenses = st.number_input("Basic Monthly Expenses (in INR)", min_value=0.0, step=100.0)
investment = st.number_input("Monthly Investment (in INR)", min_value=0.0, step=100.0)

# Calculate remaining savings
remaining_savings = pocket_money - (basic_expenses + investment)

# Display the results
st.subheader("Summary")
st.write(f"Pocket Money: ₹{pocket_money}")
st.write(f"Basic Expenses: ₹{basic_expenses}")
st.write(f"Monthly Investment: ₹{investment}")
st.write(f"Remaining Savings: ₹{remaining_savings}")

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

# Suggestions for investments and savings
st.subheader("Investment and Savings Suggestions")

if remaining_savings > 0:
    st.write("Here are some suggestions on how to use your remaining savings wisely:")
    
    st.write("1. **Invest in a Recurring Deposit (RD):** Consider putting your savings in an RD to earn interest while keeping your money safe.")
    st.write("2. **Mutual Funds:** You can start investing in mutual funds with as little as ₹500. Consider low-risk funds like debt funds for short-term goals.")
    st.write("3. **Stock Market:** If you're willing to take on more risk, you can invest in the stock market. Start with blue-chip stocks or Exchange Traded Funds (ETFs).")
    st.write("4. **Emergency Fund:** Keep a portion of your savings as an emergency fund for unforeseen expenses.")
    st.write("5. **Education:** Invest in online courses or certifications that can enhance your skills and increase future earning potential.")
    st.write("6. **Charity:** Consider donating a portion of your savings to a cause you care about.")

else:
    st.write("Your expenses and investments exceed your pocket money. Try to reduce your expenses or investment amount to save some money.")

# Tips for students
st.subheader("Financial Tips for Students")
st.write("""
- Try to save at least 20% of your pocket money each month.
- Review your expenses regularly and cut down on non-essential spending.
- Start investing early to take advantage of compounding.
- Set financial goals and track your progress.
- Consider using budgeting apps to manage your finances more effectively.
""")
