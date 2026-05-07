import streamlit as st

st.set_page_config(page_title="Cultural Infusion Fellowship", layout="wide")

# =========================
# CSS
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
    color: #e2e8f0;
}

/* SECTION TITLE */
.section-title {
    font-size: 28px;
    font-weight: 700;
    color: #0f172a;
    margin: 20px 0;
}

/* SUBTEXT */
.subtext {
    color: #1f2937;
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
    color: #111827;
}

/* PRICE BOX */
.price-box {
    background: white;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    border: 1px solid #e5e7eb;
    margin-bottom: 20px;
    text-align: center;
    color: #111827;
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

.cta p {
    color: #e2e8f0;
}

/* SMALL INCLUSION BOX */
.small-card {
    background: white;
    padding: 16px;
    border-radius: 14px;
    box-shadow: 0 6px 16px rgba(0,0,0,0.06);
    border-left: 4px solid #1e3a8a;
    margin-bottom: 12px;
    color: #111827;
}

.small-card b {
    font-size: 15px;
}

.small-card p {
    font-size: 13px;
    color: #374151;
    margin-top: 5px;
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
<div class="section-title">Building Future Global Leaders</div>

<div class="subtext">
The Cultural Infusion Fellowship combines international experience, professional development, and cultural learning into one immersive journey.<br><br>

Designed for ambitious young individuals, the program provides opportunities to gain practical industry exposure, develop globally relevant skills, and build meaningful international connections.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">Key Areas</div>

<div class="subtext">
Global Internships<br>
Professional Growth<br>
Cultural Immersion<br>
International Networking<br>
Career Development
</div>
""", unsafe_allow_html=True)

st.divider()

# =========================
# EXPERIENCE
# =========================
st.markdown("## Learning & Experience Pathway")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <b>Professional Development</b><br><br>
        Structured international internship experience<br>
        Industry-relevant skill building<br>
        Career readiness development<br>
        Leadership capability enhancement
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <b>Global Exposure</b><br><br>
        Immersive cultural integration<br>
        International collaboration opportunities<br>
        Global peer networking<br>
        Cross-cultural real-world experience
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =========================
# PROGRAM INCLUSIONS (IMPROVED UI)
# =========================
st.markdown("## Program Inclusions")

included = [

("International Internship Placement",
"Structured global internship aligned to your career path."),
("Learning & Development Workshops",
"Expert-led sessions for professional growth."),
("Career Acceleration Support",
"Tools to strengthen employability."),
("Global Talent Network Access",
"Connect with international peers and mentors."),
("1:1 Mentorship & Advisory",
"Guidance from experienced professionals."),
("Professional Branding & CV Development",
"Build a strong global-ready profile."),
("Visa & Documentation Support",
"Assistance throughout visa process."),
("Accommodation Guidance",
"Support in finding safe housing."),
("Arrival & Transition Support",
"Smooth onboarding support."),
("Cultural Immersion Experiences",
"Activities for real cultural engagement.")

]

cols = st.columns(2)

for i, (title, desc) in enumerate(included):

    with cols[i % 2]:

        st.markdown(f"""
<div class="small-card">
<b>{title}</b><br>
<p>{desc}</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# =========================
# PROGRAM INVESTMENT
# =========================
st.markdown("## Program Investment")

pricing = [
("4 Weeks", "9,340 AUD", "5,600 AUD"),
("6 Weeks", "9,585 AUD", "5,600 AUD"),
("8 Weeks", "11,440 AUD", "5,600 AUD"),
("10 Weeks", "13,295 AUD", "5,600 AUD"),
("12 Weeks", "15,290 AUD", "6,600 AUD"),
("16 Weeks", "18,730 AUD", "6,600 AUD"),
("20 Weeks", "21,460 AUD", "6,600 AUD"),
("24 Weeks", "24,150 AUD", "6,600 AUD"),
]

cols = st.columns(4)

for i, (duration, full, without) in enumerate(pricing):

    with cols[i % 4]:

        st.markdown(f"""
<div class="price-box">

<b>{duration}</b><br><br>

Full Program<br>
{full}<br><br>

Without Accommodation<br>
{without}

</div>
""", unsafe_allow_html=True)

# =========================
# CTA
# =========================
st.markdown("""
<div class="cta">
    <h2>Begin Your Global Journey</h2>
    <p>Join Cultural Infusion Fellowship and unlock global opportunities.</p>
</div>
""", unsafe_allow_html=True)

if st.button("Apply Now"):
    st.success("Application received. We'll contact you soon.")
