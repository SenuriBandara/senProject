import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="POS System", layout="wide")

# ---------------- SESSION STATE ----------------
if "cart" not in st.session_state:
    st.session_state.cart = []

if "sales" not in st.session_state:
    st.session_state.sales = []

# ---------------- INVENTORY ----------------
products = {
    "Apple": {"price": 2.0, "stock": 10},
    "Banana": {"price": 1.5, "stock": 15},
    "Milk": {"price": 3.0, "stock": 8},
    "Bread": {"price": 2.5, "stock": 12},
    "Rice (1kg)": {"price": 4.0, "stock": 20},
}

# ---------------- TITLE ----------------
st.title("🛒 Smart POS System")
st.write("Professional Streamlit-based billing system")

# ---------------- CUSTOMER ----------------
customer = st.text_input("👤 Customer Name")

st.divider()

# ---------------- PRODUCT SELECTION ----------------
col1, col2, col3 = st.columns(3)

with col1:
    product = st.selectbox("Product", list(products.keys()))

with col2:
    qty = st.number_input("Quantity", min_value=1, step=1)

with col3:
    st.write("")
    add = st.button("➕ Add to Cart")

# ---------------- ADD TO CART ----------------
if add:
    available_stock = products[product]["stock"]

    if qty > available_stock:
        st.error(f"Only {available_stock} items available in stock!")
    else:
        st.session_state.cart.append({
            "Product": product,
            "Qty": qty,
            "Price": products[product]["price"],
            "Total": products[product]["price"] * qty
        })
        st.success(f"{product} added to cart!")

# ---------------- CART ----------------
st.subheader("🧾 Cart")

if st.session_state.cart:
    df = pd.DataFrame(st.session_state.cart)
    st.dataframe(df, use_container_width=True)

    total = df["Total"].sum()

    # ---------------- DISCOUNT ----------------
    discount = st.number_input("Discount (%)", 0, 100, 0)
    discount_value = (discount / 100) * total
    final_total = total - discount_value

    st.markdown(f"### 💰 Subtotal: ${total:.2f}")
    st.markdown(f"### 🎁 Discount: -${discount_value:.2f}")
    st.markdown(f"## 🧾 Grand Total: ${final_total:.2f}")

    # ---------------- REMOVE ITEM ----------------
    remove_index = st.number_input("Remove Item Index (0,1,2...)", min_value=0, step=1)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("❌ Remove Item"):
            if len(st.session_state.cart) > remove_index:
                st.session_state.cart.pop(remove_index)
                st.rerun()
            else:
                st.error("Invalid index")

    # ---------------- CHECKOUT ----------------
    with col2:
        if st.button("✅ Checkout"):

            # reduce stock
            for item in st.session_state.cart:
                products[item["Product"]]["stock"] -= item["Qty"]

            sale = {
                "customer": customer,
                "items": st.session_state.cart,
                "total": final_total,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            st.session_state.sales.append(sale)
            st.session_state.cart = []

            st.success("Payment successful! 🎉")

else:
    st.info("Cart is empty")

# ---------------- SALES HISTORY ----------------
st.divider()
st.subheader("📊 Sales History")

if st.session_state.sales:
    for i, sale in enumerate(st.session_state.sales[::-1]):
        st.write(f"**Customer:** {sale['customer']}")
        st.write(f"**Time:** {sale['time']}")
        st.write(f"**Total:** ${sale['total']:.2f}")
        st.write("---")
else:
    st.info("No sales yet")
