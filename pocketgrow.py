import streamlit as st
from PIL import Image

# Function to change language (example for English and Spanish)
def change_language():
    lang = st.sidebar.selectbox("Choose Language", ["English", "Spanish"])
    return lang

# Function to send OTP (placeholder function)
def send_otp(phone_number):
    st.success(f"OTP sent to {phone_number}")
    # You can implement the actual OTP sending logic here using an API service

# Function to display products with images
def display_products(products):
    for product in products:
        st.image(product['image'], width=200)
        st.write(f"{product['name']}** - {product['price']}")
        st.writ
        
