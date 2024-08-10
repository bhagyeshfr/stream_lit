import streamlit as st

# Café menu
menu = {
    "Coffee": {"Espresso": 3.00, "Latte": 4.00, "Cappuccino": 4.50},
    "Tea": {"Green Tea": 2.50, "Black Tea": 2.50, "Herbal Tea": 3.00},
    "Pastries": {"Croissant": 3.00, "Muffin": 2.50, "Scone": 3.50},
    "Sandwiches": {"Ham & Cheese": 5.50, "Chicken Salad": 6.00, "Veggie": 5.00},
}

# Set up Streamlit app
st.title("Café Ordering System")

# User can select items from the menu
st.subheader("Menu")
order = {}

for category, items in menu.items():
    st.write(f"**{category}**")
    for item, price in items.items():
        quantity = st.number_input(f"{item} (${price})", min_value=0, max_value=10, step=1)
        if quantity > 0:
            order[item] = {"quantity": quantity, "price": price}

# Calculate total
if st.button("Place Order"):
    if order:
        st.subheader("Order Summary")
        total = 0
        for item, details in order.items():
            item_total = details["quantity"] * details["price"]
            st.write(f"{item} x {details['quantity']} = ${item_total:.2f}")
            total += item_total
        st.write(f"**Total: ${total:.2f}**")
        st.success("Thank you for your order!")
    else:
        st.error("No items selected. Please add items to your order.")


