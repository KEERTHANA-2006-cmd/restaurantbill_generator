import streamlit as st
from datetime import datetime

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Keerthana Restaurant Bill Generator",
    page_icon="🍔",
    layout="wide"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------
st.markdown("""
<style>

.main {
    background-color: #fff8f0;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
}

.menu-card {
    padding: 20px;
    border-radius: 15px;
    background-color: #ffffff;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

.bill-box {
    padding: 25px;
    border-radius: 18px;
    background-color: #ffffff;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.10);
}

.grand-total {
    font-size: 30px;
    font-weight: bold;
    text-align: center;
    padding: 15px;
    border-radius: 12px;
    background-color: #fff0d9;
}

.footer {
    text-align: center;
    margin-top: 30px;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# RESTAURANT MENU
# ---------------------------------------------------------
menu = {
    "🍔 Classic Burger": 120,
    "🍕 Margherita Pizza": 250,
    "🍟 French Fries": 100,
    "🌭 Veg Sandwich": 90,
    "🍝 White Sauce Pasta": 180,
    "🍜 Noodles": 150,
    "🥤 Cold Drink": 60,
    "☕ Coffee": 50,
    "🍦 Ice Cream": 80,
    "🍰 Chocolate Cake": 110
}


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.markdown(
    '<div class="title">🍔 Keerthana Restaurant Bill Generator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Delicious food • Easy billing • Happy customers ❤️</div>',
    unsafe_allow_html=True
)

st.divider()


# ---------------------------------------------------------
# CUSTOMER DETAILS
# ---------------------------------------------------------
st.subheader("👤 Customer Details")

col1, col2, col3 = st.columns(3)

with col1:
    customer_name = st.text_input(
        "Customer Name",
        placeholder="Enter customer name"
    )

with col2:
    table_number = st.text_input(
        "Table Number",
        placeholder="Enter table number"
    )

with col3:
    bill_date = datetime.now().strftime("%d-%m-%Y %I:%M %p")
    st.text_input(
        "Date & Time",
        value=bill_date,
        disabled=True
    )


st.divider()


# ---------------------------------------------------------
# FOOD SELECTION
# ---------------------------------------------------------
st.subheader("🍽️ Select Your Food")

selected_items = []

for item, price in menu.items():

    col1, col2, col3 = st.columns([4, 2, 2])

    with col1:
        st.write(f"**{item}**")

    with col2:
        st.write(f"₹{price}")

    with col3:
        quantity = st.number_input(
            f"Quantity - {item}",
            min_value=0,
            max_value=20,
            value=0,
            step=1,
            key=item,
            label_visibility="collapsed"
        )

    if quantity > 0:
        selected_items.append(
            {
                "item": item,
                "price": price,
                "quantity": quantity,
                "total": price * quantity
            }
        )


st.divider()


# ---------------------------------------------------------
# TAX AND DISCOUNT
# ---------------------------------------------------------
st.subheader("💰 Bill Settings")

col1, col2 = st.columns(2)

with col1:
    tax_percent = st.number_input(
        "GST / Tax (%)",
        min_value=0.0,
        max_value=30.0,
        value=5.0,
        step=0.5
    )

with col2:
    discount_percent = st.number_input(
        "Discount (%)",
        min_value=0.0,
        max_value=50.0,
        value=0.0,
        step=1.0
    )


# ---------------------------------------------------------
# CALCULATIONS
# ---------------------------------------------------------
subtotal = sum(item["total"] for item in selected_items)

discount_amount = subtotal * discount_percent / 100

amount_after_discount = subtotal - discount_amount

tax_amount = amount_after_discount * tax_percent / 100

grand_total = amount_after_discount + tax_amount


# ---------------------------------------------------------
# GENERATE BILL
# ---------------------------------------------------------
st.divider()

st.subheader("🧾 Final Bill")


if selected_items:

    st.markdown('<div class="bill-box">', unsafe_allow_html=True)

    st.markdown("### 🍔 KEERTHANA RESTAURANT")

    if customer_name:
        st.write(f"**Customer:** {customer_name}")

    if table_number:
        st.write(f"**Table:** {table_number}")

    st.write(f"**Date:** {bill_date}")

    st.divider()

    # BILL TABLE
    header1, header2, header3, header4 = st.columns([4, 2, 2, 2])

    with header1:
        st.write("**Item**")

    with header2:
        st.write("**Price**")

    with header3:
        st.write("**Qty**")

    with header4:
        st.write("**Total**")

    st.divider()

    for item in selected_items:

        col1, col2, col3, col4 = st.columns([4, 2, 2, 2])

        with col1:
            st.write(item["item"])

        with col2:
            st.write(f"₹{item['price']:.2f}")

        with col3:
            st.write(item["quantity"])

        with col4:
            st.write(f"₹{item['total']:.2f}")

    st.divider()

    # SUMMARY
    col1, col2 = st.columns([3, 2])

    with col1:
        st.write("### 💳 Payment Summary")

    with col2:
        st.write(f"**Subtotal:** ₹{subtotal:.2f}")
        st.write(
            f"**Discount ({discount_percent:.1f}%):** "
            f"- ₹{discount_amount:.2f}"
        )
        st.write(
            f"**GST ({tax_percent:.1f}%):** "
            f"+ ₹{tax_amount:.2f}"
        )

    st.divider()

    st.markdown(
        f"""
        <div class="grand-total">
            💰 Grand Total: ₹{grand_total:.2f}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="footer">🙏 Thank you for visiting Keerthana Restaurant!<br>'
        '❤️ Have a wonderful day!</div>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

else:

    st.info(
        "🍽️ Please select at least one food item and quantity "
        "to generate the bill."
    )