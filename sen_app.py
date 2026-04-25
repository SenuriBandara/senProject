import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="POS System", layout="wide")

# ---------------- SESSION STATE ----------------
if "cart" not in st.session_state:
    st.session_state.cart = []

# ---------------- PRODUCT DATABASE ----------------
products = {
    "Apple": 2.0,
    "Banana": 1.5,
    "Milk": 3.0,
    "Bread": 2.5,
    "Rice (1kg)": 4.0,
    "Eggs (10)": 5.0,
    "Chicken (1kg)": 8.0
}

# ---------------- TITLE ----------------
st.title("🛒 POS System")
st.write("Select items, add to cart, and generate total bill")

# ---------------- ADD PRODUCT ----------------
col1, col2, col3 = st.columns(3)

with col1:
    product = st.selectbox("Product", list(products.keys()))

with col2:
    qty = st.number_input("Quantity", min_value=1, step=1)

with col3:
    st.write("")
    st.write("")
    add_btn = st.button("➕ Add to Cart")

if add_btn:
    st.session_state.cart.append({
        "Product": product,
        "Quantity": qty,
        "Unit Price": products[product],
        "Total": products[product] * qty
    })
    st.success(f"{product} added to cart!")

# ---------------- CART ----------------
st.subheader("🧾 Cart Items")

if st.session_state.cart:
    df = pd.DataFrame(st.session_state.cart)

    st.dataframe(df, use_container_width=True)

    total = df["Total"].sum()

    st.markdown(f"## 💰 Grand Total: ${total:.2f}")

    # ---------------- REMOVE LAST ITEM ----------------
    col1, col2 = st.columns(2)

    with col1:
        if st.button("❌ Remove Last Item"):
            st.session_state.cart.pop()
            st.rerun()

    with col2:
        if st.button("🗑 Clear Cart"):
            st.session_state.cart = []
            st.rerun()

else:
    st.info("Cart is empty. Add products to start.")
