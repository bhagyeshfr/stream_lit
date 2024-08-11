import streamlit as st

# Function to suggest areas based on input
def suggest_areas(budget, bhk, carpet_area):
    # Sample data for areas (you can replace this with actual data or logic)
    areas = {
        "Area 1": {"price_per_sqft": 5000, "amenities": "Gym, Pool, Park", "types": [1, 2]},
        "Area 2": {"price_per_sqft": 7500, "amenities": "Gym, Pool, Park, Clubhouse", "types": [2, 3]},
        "Area 3": {"price_per_sqft": 10000, "amenities": "Gym, Pool, Park, Clubhouse, Parking", "types": [3, 4]},
        "Area 4": {"price_per_sqft": 15000, "amenities": "Luxury Amenities, Security", "types": [2, 3, 4]},
    }

    suggested_areas = []
    for area, details in areas.items():
        if bhk in details["types"]:
            total_price = details["price_per_sqft"] * carpet_area
            if total_price <= budget:
                suggested_areas.append((area, total_price, details["amenities"]))

    return suggested_areas

# Streamlit UI
st.title("Real Estate Finder")

# User Inputs
budget = st.number_input("Enter your budget (INR):", min_value=100000, step=10000)
bhk = st.selectbox("Select the type of flat (BHK):", [1, 2, 3, 4])
carpet_area = st.number_input("Enter the carpet area required (in sq ft):", min_value=100, step=10)

if st.button("Find Best Areas"):
    suggestions = suggest_areas(budget, bhk, carpet_area)
    if suggestions:
        st.write("Based on your requirements, here are the best areas:")
        for area, price, amenities in suggestions:
            st.write(f"**Area:** {area}")
            st.write(f"**Estimated Price:** {price} INR")
            st.write(f"**Amenities:** {amenities}")
            st.write("---")
    else:
        st.write("No areas found matching your criteria.")
