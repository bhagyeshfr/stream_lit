import streamlit as st

# Title of the app
st.title('Cafe Ordering App')

# Menu items and prices in INR
menu = {
    'Coffee': 50,
    'Tea': 30,
    'Sandwich': 100,
    'Cake': 150,
    'Juice': 80
}

# Select items from the menu
st.subheader('Menu')
selected_items = {}
for item, price in menu.items():
    quantity = st.number_input(f'{item} (₹{price} each)', min_value=0, max_value=10, step=1)
    if quantity > 0:
        selected_items[item] = quantity

# Calculate the total cost
if selected_items:
    total_cost = sum(menu[item] * quantity for item, quantity in selected_items.items())
    st.write('### Selected Items:')
    for item, quantity in selected_items.items():
        st.write(f'{item}: {quantity} x ₹{menu[item]} = ₹{menu[item] * quantity}')
    
    st.write(f'## Total Cost: ₹{total_cost}')
else:
    st.write('Please select at least one item from the menu.')

# Thank you message
if selected_items:
    st.write('### Thank you for your order!')
