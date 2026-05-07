import streamlit as st

st.set_page_config(page_title="Cultural Infusion Fellowship", layout="wide")

# =========================
# GLOBAL STYLES
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
    max-width: 900px;
    margin: auto;
}

.section-title {
    font-size: 28px;
    font-weight: 700;
    margin-top: 40px;
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
}

.card-title {
    font-weight: 600;
    font-size: 15px;
    margin-bottom: 6px;
    color: #0f172a;
}

.card-text {
    font-size: 14px;
    color: #475569;
    line-height: 1.6;
}

.overview-box {
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

.price-card {
    background: #ffffff;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0 6px 18px rgba(15, 23, 42, 0.08);
    border-left: 4px solid #1e3a8a;
    text-align: center;
    height: 100%;
}

.price-duration {
    font-size: 16px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 10px;
}

.price-value {
    font-size: 14px;
    color: #334155;
    margin-bottom: 6px;
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
# PROGRAM OVERVIEW (ULTRA PROFESSIONAL)
# =========================
st.markdown("## Program Overview")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
<div class="overview-box">
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
    <div class="section-title">Focus Areas</div>
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
- Structured international internship experience  
- Industry-relevant skill building  
- Career readiness development  
- Leadership capability enhancement  
""")

with col2:
    st.markdown("""
### Global Exposure
- Immersive cultural integration  
- International collaboration opportunities  
- Global peer networking  
- Real-world cross-cultural experience  
""")

st.divider()

# =========================
# PROGRAM INCLUSIONS (CARDS)
# =========================
st.markdown("## Program Inclusions")

included = [
("International Internship Placement","Structured professional experience in global organisations."),
("Learning & Workshop Series","Practical skill-building sessions and guided workshops."),
("Career Development Framework","Long-term employability and career progression support."),
("Employability Training","Preparation for global job market success."),
("Global Network Access","Connection to international peers and professionals."),
("Mentorship Support","Guidance from experienced mentors and alumni."),
("CV & Profile Development","Support in professional branding and documentation."),
("1-1 Advisory Support","Personalised guidance throughout the program."),
("Continuous Support","Operational support during the full experience."),
("Visa Guidance","Structured assistance for visa preparation."),
("Accommodation Support","Guidance for housing arrangements."),
("Arrival Assistance","Onboarding and arrival coordination."),
("Cultural Integration","Activities for cultural immersion and engagement.")
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
# PRICING (ULTRA CLEAN CARD DESIGN)
# =========================
st.markdown("## Program Investment")

pricing = [
("4 Weeks","AUD 9,340","AUD 5,600"),
("6 Weeks","AUD 9,585","AUD 5,600"),
("8 Weeks","AUD 11,440","AUD 5,600"),
("10 Weeks","AUD 13,295","AUD 5,600"),
("12 Weeks","AUD 15,290","AUD 6,600"),
("16 Weeks","AUD 18,730","AUD 6,600"),
("20 Weeks","AUD 21,460","AUD 6,600"),
("24 Weeks","AUD 24,150","AUD 6,600")
]

cols = st.columns(4)

for i, (duration, full, without) in enumerate(pricing):
    with cols[i % 4]:
        st.markdown(f"""
        <div class="price-card">
            <div class="price-duration">{duration}</div>
            <div class="price-value"><b>Full Program</b><br>{full}</div>
            <div class="price-value"><b>Without Accommodation</b><br>{without}</div>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# =========================
# CTA
# =========================
st.markdown("## Application")

st.write("Submit your application to join the Cultural Infusion Fellowship.")

if st.button("Apply Now"):
    st.success("Application received. Our team will contact you shortly.")
