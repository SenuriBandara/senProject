import streamlit as st

st.set_page_config(page_title="Cultural Infusion Fellowship", layout="wide")

# =========================
# STYLES (ONLY FIXED COLORS)
# =========================
st.markdown("""
<style>

/* HERO */
.hero {
    padding: 90px 40px;
    background: linear-gradient(120deg, #0b1220, #1e3a8a);
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 40px;
}

.hero h1 {
    font-size: 56px;
    font-weight: 800;
    color: white;
}

.hero p {
    font-size: 20px;
    opacity: 0.95;
    color: #e2e8f0;
}

/* SECTION TITLE */
.section-title {
    font-size: 28px;
    font-weight: 700;
    margin: 25px 0 15px 0;
    color: #0f172a;
}

/* MAIN TEXT FIX (IMPORTANT) */
.text {
    color: #1f2937;   /* FIXED DARK TEXT */
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

    /* FIX TEXT VISIBILITY INSIDE CARDS */
    color: #111827;
}

/* CARD TITLE */
.card b {
    color: #0f172a;
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

    color: #111827;  /* FIXED */
}

.price h3 {
    font-size: 22px;
    margin-bottom: 10px;
    color: #0f172a;
}

.price p {
    margin: 5px 0;
    color: #374151;   /* FIXED VISIBILITY */
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
    color: white;
}

.cta p {
    font-size: 18px;
    opacity: 0.9;
    color: #e2e8f0;
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
# OVERVIEW
# =========================
st.markdown("## Program Overview")

st.markdown("""
<div class="text">
The Cultural Infusion Fellowship is a global experience designed to build future-ready talent through international exposure, cultural immersion, and professional development.
</div>
""", unsafe_allow_html=True)

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
st.markdown("## Learning Experience")

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
st.markdown("## Program Inclusions")

items = [
"Internship Placement",
"Workshops & Training",
"Mentorship Support",
"Visa Guidance",
"Accommodation Support",
"Global Community",
"Cultural Activities",
"Career Support"
]

for i in items:
    st.markdown(f"<div class='card'>{i}</div>", unsafe_allow_html=True)

# =========================
# PRICING
# =========================
st.markdown("## Program Investment")

pricing = [
("4 Weeks","9,340 AUD","5,600 AUD"),
("6 Weeks","9,585 AUD","5,600 AUD"),
("8 Weeks","11,440 AUD","5,600 AUD"),
("10 Weeks","13,295 AUD","5,600 AUD"),
("12 Weeks","15,290 AUD","6,600 AUD"),
("16 Weeks","18,730 AUD","6,600 AUD"),
("20 Weeks","21,460 AUD","6,600 AUD"),
("24 Weeks","24,150 AUD","6,600 AUD"),
]

cols = st.columns(4)

for i, (d,f,w) in enumerate(pricing):
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
    st.success("Application submitted successfully.")
