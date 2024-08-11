import streamlit as st

# Sample data for real estate suggestions
real_estate_data = {
    "1BHK": {
        "low_budget": {
            "area": "Area A",
            "features": ["Close to public transport", "Near market", "Affordable housing"]
        },
        "mid_budget": {
            "area": "Area B",
            "features": ["Gated community", "Near schools and hospitals", "Moderate pricing"]
        },
        "high_budget": {
            "area": "Area C",
            "features": ["Luxury amenities", "Prime location", "High-end security"]
        }
    },
    "2BHK": {
        "low_budget": {
            "area": "Area D",
            "features": ["Affordable housing", "Close to public transport", "Developing area"]
        },
        "mid_budget": {
            "area": "Area E",
            "features": ["Gated community", "Near schools", "Modern amenities"]
        },
        "high_budget": {
            "area": "Area F",
            "features": ["Luxury apartments", "Prime location", "High-end amenities"]
        }
    },
    # Add similar data for 3BHK, 4BHK, etc.
}

# Title of the app
st.title("Real Estate Recommendation App")

# Input fields for budget and flat size
budget = st.number_input("Enter your budget (in INR)", min_value=0, step=100000)
flat_type = st.selectbox("Select the flat size", ["1BHK", "2BHK", "3BHK", "4BHK"])

# Determine budget category
if budget < 3000000:
    budget_category = "low_budget"
elif 3000000 <= budget <= 7000000:
    budget_category = "mid_budget"
else:
    budget_category = "high_budget"

# Provide suggestions based on inputs
if flat_type in real_estate_data:
    suggestion = real_estate_data[flat_type][budget_category]
    st.header(f"Best Area for {flat_type} in your Budget")
    st.write(f"**Area:** {suggestion['area']}")
    st.write("**Features:**")
    for feature in suggestion["features"]:
        st.write(f"- {feature}")
else:
    st.write("We currently don't have suggestions for this flat size.")

# Additional options or details can be added here
