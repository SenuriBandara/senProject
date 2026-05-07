import streamlit as st

st.set_page_config(page_title="Cultural Infusion Fellowship", layout="wide")

# =========================
# STYLES (clean + modern)
# =========================
st.markdown("""
<style>

html, body, [class*="css"]  {
    font-family: 'Arial';
}

/* HERO */
.hero {
    background: linear-gradient(120deg, #0b1220, #1e3a8a);
    padding: 100px 40px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 40px;
}

.hero h1 {
    font-size: 56px;
    font-weight: 800;
}

.hero p {
    font-size: 20px;
    opacity: 0.9;
}

/* SECTION TITLE */
.section-title {
    font-size: 28px;
    font-weight: 700;
    margin: 25px 0 15px 0;
    color: #0f172a;
}

/* TEXT */
.text {
    color: #475569;
    font-size: 16px;
    line-height: 1.8;
}

/* CARD */
.card {
    background: white;
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    border-top: 4px solid #1e3a8a;
    margin-bottom: 18px;
}

/* PRICE CARD */
.price {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    border-top: 4px solid #1e3a8a;
    text-align: center;
    margin-bottom: 20px;
}

.price h3 {
    font-size: 22px;
    margin-bottom: 10px;
}

.price p {
    margin: 5px 0;
    color: #334155;
}

/* CTA */
.cta {
    background: linear-gradient(120deg, #0b1220, #1e3a8a);
    color: white;
    padding: 70px;
    border-radius: 20px;
    text-align: center;
    margin-top: 40px;
}

.cta h2 {
    font-size: 36px;
}

.cta p {
    font-size: 18px;
    opacity: 0.9;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HERO
# =========================
st.markdown("""
<div class="hero">
    <h1>Cultural Infusion Fellowship</h1>
    <p>Where Talent, Opportunity, and Culture Converge</p>
</div>
""", unsafe_allow_html=True)

# =========================
# PROGRAM OVERVIEW
# =========================
st.markdown('<div class="section-title">Program Overview</div>', unsafe_allow_html=True)

st.markdown("""
<div class="text">
The Cultural Infusion Fellowship is a global experience designed to build future-ready talent through international exposure, cultural immersion, and professional development.
</div>
""", unsafe_allow_html=True)

st.write("")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <b>What you get</b><br><br>
        Global internships<br>
        Industry exposure<br>
        Cultural learning<br>
        Career development
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <b>Outcome</b><br><br>
        Global mindset<br>
        Professional growth<br>
        Cross-cultural skills<br>
        International network
    </div>
    """, unsafe_allow_html=True)

# =========================
# EXPERIENCE
# =========================
st.markdown('<div class="section-title">Learning Experience</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <b>Professional Development</b><br><br>
        Internship experience<br>
        Skill building<br>
        Career readiness<br>
        Leadership growth
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <b>Global Exposure</b><br><br>
        Cultural immersion<br>
        Networking<br>
        Real-world experience<br>
        International collaboration
    </div>
    """, unsafe_allow_html=True)

# =========================
# INCLUSIONS
# =========================
st.markdown('<div class="section-title">What’s Included</div>', unsafe_allow_html=True)

inclusions = [
"Internship Placement",
"Workshops & Training",
"Mentorship Support",
"Visa Guidance",
"Accommodation Support",
"Global Community",
"Cultural Activities",
"Career Support"
]

cols = st.columns(2)

for i, item in enumerate(inclusions):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="card">
            {item}
        </div>
        """, unsafe_allow_html=True)

# =========================
# PRICING
# =========================
st.markdown('<div class="section-title">Program Investment</div>', unsafe_allow_html=True)

pricing = [
("4 Weeks", "9,340 AUD", "5,600 AUD"),
("6 Weeks", "9,585 AUD", "5,600 AUD"),
("8 Weeks", "11,440 AUD", "5,600 AUD"),
("10 Weeks", "13,295 AUD", "5,600 AUD"),
("12 Weeks", "15,290 AUD", "6,600 AUD"),
("16 Weeks", "18,730 AUD", "6,600 AUD"),
("20 Weeks", "21,460 AUD", "6,600 AUD"),
("24 Weeks", "24,150 AUD", "6,600 AUD")
]

cols = st.columns(4)

for i, (d, f, w) in enumerate(pricing):
    with cols[i % 4]:
        st.markdown(f"""
        <div class="price">
            <h3>{d}</h3>
            <p><b>Full Program</b><br>{f}</p>
            <p><b>Without Accommodation</b><br>{w}</p>
        </div>
        """, unsafe_allow_html=True)

# =========================
# CTA
# =========================
st.markdown("""
<div class="cta">
    <h2>Begin Your Global Journey</h2>
    <p>Join the Cultural Infusion Fellowship and unlock international opportunities.</p>
</div>
""", unsafe_allow_html=True)

if st.button("Apply Now"):
    st.success("Application submitted. We will contact you soon.")
