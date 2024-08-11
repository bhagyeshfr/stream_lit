import streamlit as st

# Function to suggest areas based on input
def suggest_areas(budget, bhk, carpet_area):
    # Mumbai areas data with images
    areas = {
        "Andheri West": {
            "price_per_sqft": 25000,
            "amenities": "Gym, Pool, Park, Clubhouse, Parking",
            "types": [2, 3, 4],
            "image_url": "https://example.com/andheri_west.jpg"
        },
        "Bandra West": {
            "price_per_sqft": 35000,
            "amenities": "Luxury Amenities, Security, Sea View",
            "types": [2, 3, 4],
            "image_url": "https://example.com/bandra_west.jpg"
        },
        "Powai": {
            "price_per_sqft": 20000,
            "amenities": "Gym, Pool, Park, Lake View, Clubhouse",
            "types": [1, 2, 3],
            "image_url": "https://example.com/powai.jpg"
        },
        "Thane": {
            "price_per_sqft": 15000,
            "amenities": "Gym, Pool, Park, Clubhouse",
            "types": [1, 2, 3],
            "image_url": "https://example.com/thane.jpg"
        },
        "Borivali East": {
            "price_per_sqft": 18000,
            "amenities": "Gym, Park, Clubhouse, Parking",
            "types": [1, 2, 3],
            "image_url": "https://example.com/borivali_east.jpg"
        },
        "Lower Parel": {
            "price_per_sqft": 30000,
            "amenities": "Luxury Amenities, Gym, Pool, Clubhouse, Parking",
            "types": [2, 3, 4],
            "image_url": "https://example.com/lower_parel.jpg"
        },
        "Dadar": {
            "price_per_sqft": 28000,
            "amenities": "Gym, Pool, Park, Clubhouse, Parking",
            "types": [2, 3],
            "image_url": "https://example.com/dadar.jpg"
        },
        "Navi Mumbai": {
            "price_per_sqft": 12000,
            "amenities": "Gym, Park, Clubhouse",
            "types": [1, 2],
            "image_url": "https://example.com/navi_mumbai.jpg"
        }
    }

    suggested_areas = []
    for area, details in areas.items():
        if bhk in details["types"]:
            total_price = details["price_per_sqft"] * carpet_area
            if total_price <= budget:
                suggested_areas.append((area, total_price, details["amenities"], details["image_url"]))

    return suggested_areas

# Streamlit UI
st.title("Mumbai Real Estate Finder")

# User Inputs
budget = st.number_input("Enter your budget (INR):", min_value=100000, step=10000)
bhk = st.selectbox("Select the type of flat (BHK):", [1, 2, 3, 4])
carpet_area = st.number_input("Enter the carpet area required (in sq ft):", min_value=100, step=10)

if st.button("Find Best Areas"):
    suggestions = suggest_areas(budget, bhk, carpet_area)
    if suggestions:
        st.write("Based on your requirements, here are the best areas in Mumbai:")
        for area, price, amenities, image_url in suggestions:
            st.write(f"**Area:** {area}")
            st.write(f"**Estimated Price:** {price} INR")
            st.write(f"**Amenities:** {amenities}")
            st.image(image_url, caption=area, use_column_width=True)
            st.write("---")
    else:
        st.write("No areas found matching your criteria.")
