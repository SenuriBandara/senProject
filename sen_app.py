import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cultural Infusion Fellowship", layout="wide")

# =========================
# GLOBAL STYLES (CLEAN PROFESSIONAL UI)
# =========================
st.markdown("""
<style>

.hero {
    padding: 85px 50px;
    background: linear-gradient(to right, #0b1220, #1e3a8a);
    color: white;
    border-radius: 18px;
    text-align: center;
}

.hero h1 {
    font-size: 46px;
    font-weight: 700;
    margin-bottom: 10px;
}

.hero p {
    font-size: 18px;
    color: #dbeafe;
    max-width: 800px;
    margin: auto;
}

.section-title {
    font-size: 28px;
    font-weight: 700;
    margin-top: 50px;
    margin-bottom: 15px;
    color: #0f172a;
}

.subtext {
    font-size: 16px;
    color: #475569;
    line-height: 1.8;
}

.card {
    background: #ffffff;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0 6px 18px rgba(15, 23, 42, 0.08);
    border-left: 4px solid #1e3a8a;
    height: 100%;
}

.card-title {
    font-weight: 600;
    font-size: 15px;
    margin-bottom: 8px;
    color: #0f172a;
}

.card-text {
    font-size: 14px;
    color: #475569;
    line-height: 1.6;
}

.highlight-box {
    background: #f1f5f9;
    padding: 26px;
    border-radius: 16px;
    border-left: 5px solid #1e3a8a;
}

.focus-box {
    background: #ffffff;
    padding: 24px;
    border-radius: 16px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.06);
}

</style>
""", unsafe_allow_html=True)

# =========================
# HERO
# =========================
st.markdown("""
<div class="hero">
    <h1>Cultural Infusion Fellowship</h1>
    <p>A structured global development ecosystem enabling young talent to gain international exposure, professional capability, and cross-cultural competence through immersive experiences.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# =========================
# PROGRAM OVERVIEW (PROFESSIONAL TONE)
# =========================
st.markdown("## Program Overview")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
<div class="highlight-box">
    <div class="section-title">Global Talent Development Ecosystem</div>
    <div class="subtext">
        The Cultural Infusion Fellowship is a structured international development initiative designed to prepare young individuals for globally connected careers.<br><br>

        It integrates professional experience, cultural immersion, and skills development into a unified pathway that connects participants with universities, companies, and international opportunities.
    </div>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="focus-box">
    <div class="section-title">Strategic Focus</div>
    <div class="subtext">
        International Mobility<br>
        Professional Skill Development<br>
        Cross-Cultural Competence<br>
        Industry Exposure<br>
        Global Career Pathways
    </div>
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
### Professional Development
- Structured internship placement in real working environments  
- Industry-relevant skill development exposure  
- Career readiness and leadership capability building  
- Practical workplace learning and mentorship  
""")

with col2:
    st.markdown("""
### Global Exposure
- Immersive cultural and social integration  
- Collaboration with international peers  
- Access to global community networks  
- Experiential learning in diverse environments  
""")

st.divider()

# =========================
# PROGRAM INCLUSIONS (PREMIUM CARDS)
# =========================
st.markdown("## Program Inclusions")

included = [
("International Internship Placement",
"Structured in-person professional experience within global organisations."),

("Learning & Workshop Series",
"Curated learning sessions focused on practical and professional growth."),

("Career Development Framework",
"Tools and guidance to enhance long-term employability and career clarity."),

("Employability Training",
"Targeted preparation for global job market readiness."),

("Global Network Access",
"Connection with an international community of peers and professionals."),

("Mentorship Support",
"Guidance from experienced professionals and alumni network."),

("Professional Profile Development",
"Support in CV building and personal branding enhancement."),

("Dedicated Advisory Support",
"One-to-one guidance throughout the program journey."),

("Continuous Program Support",
"Operational and participant support throughout the experience."),

("Visa Advisory Support",
"Structured guidance for visa preparation and compliance."),

("Accommodation Assistance",
"Support in identifying suitable housing options."),

("Arrival Coordination",
"Onboarding and arrival assistance in destination country."),

("Cultural Integration Activities",
"Structured experiences to support adaptation and engagement.")
]

def render_cards(data):
    cols = st.columns(3)
    for i, (title, desc) in enumerate(data):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="card">
                <div class="card-title">{title}</div>
                <div class="card-text">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

render_cards(included)

st.divider()

# =========================
# PRICING TABLE
# =========================
st.markdown("## Program Investment")

data = [
("4 Weeks", 9340, 5600),
("6 Weeks", 9585, 5600),
("8 Weeks", 11440, 5600),
("10 Weeks", 13295, 5600),
("12 Weeks", 15290, 6600),
("16 Weeks", 18730, 6600),
("20 Weeks", 21460, 6600),
("24 Weeks", 24150, 6600),
]

df = pd.DataFrame(data, columns=[
    "Duration",
    "Full Program (AUD)",
    "Without Accommodation (AUD)"
])

st.table(df)

st.divider()

# =========================
# CTA
# =========================
st.markdown("## Application")

st.write("Submit your application to be considered for upcoming program intakes.")

if st.button("Apply Now"):
    st.success("Your application has been received. Our team will be in contact with you shortly.")
