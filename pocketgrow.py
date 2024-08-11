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
        st.write(product['description'])
        st.button("Add to Cart", key=product['id'])

# Function to suggest products based on user preferences
def suggest_products(fashion_sense, products):
    st.subheader(f"Suggestions based on your style: {fashion_sense}")
    filtered_products = [p for p in products if fashion_sense.lower() in p['tags']]
    display_products(filtered_products)

# Sample product data
products = [
    {
        'id': 1,
        'name': 'Stylish T-shirt',
        'price': '$20',
        'description': 'A cool and comfortable t-shirt.',
        'image': 'tshirt.jpg',
        'tags': 'casual'
    },
    {
        'id': 2,
        'name': 'Elegant Sandals',
        'price': '$50',
        'description': 'Elegant sandals perfect for summer.',
        'image': 'sandals.jpg',
        'tags': 'summer'
    },
    {
        'id': 3,
        'name': 'Smart Watch',
        'price': '$150',
        'description': 'A digital gadget to keep you connected.',
        'image': 'watch.jpg',
        'tags': 'digital'
    },
]

# Main App
def main():
    st.title("Domain Fashion Online Store")

    # Change Language
    lang = change_language()

    # User Input
    name = st.text_input("Name")
    phone_number = st.text_input("Phone Number")
    address = st.text_area("Address")

    if st.button("Send OTP"):
        send_otp(phone_number)

    # Fashion sense input
    fashion_sense = st.selectbox("Select your fashion sense", ["Casual", "Formal", "Summer", "Digital"])

    # Suggest products
    suggest_products(fashion_sense, products)

    # Display all products
    st.subheader("Available Products")
    display_products(products)

if _name_ == "_main_":
    main()
