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
# INCLUSIONS
# =========================
st.markdown("## Program Inclusions")

included = [

("International Internship Placement",
"High-quality structured internship with global organisations aligned to your career path."),

("Learning & Development Workshops",
"Expert-led sessions focused on professional skills and global employability."),

("Career Acceleration Support",
"Tools and guidance to strengthen long-term career growth."),

("Global Talent Network Access",
"Connect with international peers, mentors, and professionals."),

("1:1 Mentorship & Advisory",
"Ongoing guidance from experienced industry mentors."),

("Professional Branding & CV Development",
"Support to build a strong global-ready profile."),

("Visa & Documentation Support",
"Structured assistance throughout visa processing."),

("Accommodation Guidance",
"Support in finding safe and suitable housing."),

("Arrival & Transition Support",
"On-ground support for smooth onboarding."),

("Cultural Immersion Experiences",
"Curated activities for deep cultural engagement.")

]

for title, desc in included:
    st.markdown(f"""
    <div class="card">
        <b>{title}</b><br><br>
        {desc}
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =========================
# PROGRAM INVESTMENT (FIXED - NO DIV)
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
### {duration}

**Full Program**  
💰 {full}

**Without Accommodation**  
🏠 {without}

---
""")

st.divider()

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
