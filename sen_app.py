import streamlit as st

st.set_page_config(page_title="In-Person Internship Program", page_icon="🌍", layout="wide")

# --- HERO SECTION ---
st.markdown("""
<style>
.hero {
    background: linear-gradient(to right, #0f172a, #1e3a8a);
    padding: 60px;
    border-radius: 15px;
    color: white;
    text-align: center;
}
.card {
    padding: 20px;
    border-radius: 12px;
    background: white;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>In-Person Global Internship Program 🌍</h1>
    <p>Gain international experience, travel the world, and grow your career.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# --- OVERVIEW ---
st.header("Boost Your Employability")
st.write("""
Join a global internship experience designed to help you grow professionally and personally
while immersing yourself in a new culture.
""")

st.divider()

# --- BENEFITS ---
st.subheader("Why Join?")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="card">🌍 Global Experience</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="card">💼 Career Growth</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="card">🤝 Networking</div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="card">🏡 Support Provided</div>', unsafe_allow_html=True)

st.divider()

# --- HOW IT WORKS ---
st.subheader("How It Works")
st.markdown("""
1. Apply online  
2. Attend interview  
3. Get matched with internship  
4. Start your global journey 🌏
""")

st.divider()

# --- DESTINATIONS ---
st.subheader("Top Destinations")

dest1, dest2, dest3, dest4 = st.columns(4)

with dest1:
    st.info("📍 London")
with dest2:
    st.info("📍 New York")
with dest3:
    st.info("📍 Melbourne")
with dest4:
    st.info("📍 Tokyo")

st.divider()

# --- CTA ---
st.subheader("Ready to start your journey?")

if st.button("Apply Now 🚀"):
    st.success("Thanks for your interest! We will contact you soon.")
