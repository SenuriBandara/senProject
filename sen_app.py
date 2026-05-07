import streamlit as st
import pandas as pd

st.set_page_config(page_title="Program Pricing", layout="wide")

# ---------- STYLES ----------
st.markdown("""
<style>
.title {
    text-align: center;
    font-size: 38px;
    font-weight: 700;
    margin-top: 20px;
}

.subtitle {
    text-align: center;
    color: #666;
    margin-bottom: 40px;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    text-align: center;
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.12);
}

.price {
    font-size: 26px;
    font-weight: bold;
    color: #1e3a8a;
    margin-top: 10px;
}

.duration {
    font-size: 18px;
    font-weight: 600;
    color: #111;
}

.note {
    font-size: 13px;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown('<div class="title">Program Pricing</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Choose the duration that fits your global journey</div>', unsafe_allow_html=True)

# ---------- DATA ----------
pricing = [
    ("4 Weeks", 9340),
    ("6 Weeks", 9585),
    ("8 Weeks", 11440),
    ("10 Weeks", 13295),
    ("12 Weeks", 15290),
    ("16 Weeks", 18730),
    ("20 Weeks", 21460),
    ("24 Weeks", 24150),
]

no_accommodation = {
    "4 Weeks": 5600,
    "6 Weeks": 5600,
    "8 Weeks": 5600,
    "10 Weeks": 5600,
    "12 Weeks": 6600,
    "16 Weeks": 6600,
    "20 Weeks": 6600,
    "24 Weeks": 6600,
}

# ---------- CARDS ----------
cols = st.columns(4)

for i, (duration, price) in enumerate(pricing):
    with cols[i % 4]:
        st.markdown(f"""
        <div class="card">
            <div class="duration">{duration}</div>
            <div class="price">AU$ {price:,}</div>
            <div class="note">Without Accommodation: AU$ {no_accommodation[duration]:,}</div>
        </div>
        """, unsafe_allow_html=True)

st.write("")

# ---------- CLEAN TABLE VIEW (optional backup) ----------
st.markdown("### 📊 Summary Table")

df = pd.DataFrame({
    "Duration": [d[0] for d in pricing],
    "Full Program (Avg AU$)": [d[1] for d in pricing],
    "Without Accommodation (AU$)": [no_accommodation[d[0]] for d in pricing]
})

st.table(df)
