import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cultural Infusion Fellowship", layout="wide")

# =========================
# GLOBAL STYLES
# =========================
st.markdown("""
<style>

.hero {
    padding: 75px 40px;
    background: linear-gradient(to right, #0f172a, #1e3a8a);
    color: white;
    border-radius: 18px;
    text-align: center;
}

.hero h1 {
    font-size: 44px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 18px;
    color: #e5e7eb;
}

.section-title {
    font-size: 28px;
    font-weight: 700;
    margin-top: 50px;
    margin-bottom: 10px;
}

.card {
    background: #ffffff;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    border-left: 4px solid #1e3a8a;
    height: 100%;
}

.card-title {
    font-weight: 600;
    margin-bottom: 6px;
    color: #111;
}

.card-text {
    font-size: 14px;
    color: #555;
    line-height: 1.6;
}

.overview-card {
    background: #f8f9fa;
    padding: 26px;
    border-radius: 16px;
    border-left: 5px solid #1e3a8a;
    box-shadow: 0 4px 14px rgba(0,0,0,0.06);
}

.overview-title {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 12px;
}

.overview-text {
    font-size: 15px;
    color: #444;
    line-height: 1.7;
}

.focus-box {
    background: white;
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
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

st.write("")

# =========================
# ULTRA PREMIUM PROGRAM OVERVIEW
# =========================
st.markdown("## Program Overview")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
<div class="overview-card">
    <div class="overview-title">Global Talent Development Ecosystem</div>
    <div class="overview-text">
        A youth-focused global ecosystem designed to develop globally competent talent through structured development experiences and international mobility pathways.<br><br>

        The initiative connects youth, universities, companies, and institutions through an integrated system that links engagement with skill development and real-world global exposure.
    </div>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="focus-box">
    <div class="overview-title">Focus Areas</div>
    <div class="overview-text">
        International Mobility<br>
        Skill Development<br>
        Industry Exposure<br>
        Cross-cultural Learning<br>
        Global Career Pathways
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# =========================
# EXPERIENCE
# =========================
st.markdown("## Experience Overview")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
### Professional Development
- Real-world internship exposure  
- Industry-based learning environments  
- Skill and career development  
- Leadership growth opportunities  
""")

with col2:
    st.markdown("""
### Global Exposure
- Cultural immersion in new environments  
- International peer engagement  
- Community and networking opportunities  
- Cross-cultural collaboration  
""")

st.divider()

# =========================
# PROGRAM INCLUSIONS (PREMIUM CARDS)
# =========================
st.markdown("## Program Inclusions")

included = [
("International Internship Placement",
"Real-world in-person internship experience in a global environment."),

("Workshop & Learning Series",
"Structured sessions designed to build practical and professional skills."),

("Professional Development Resources",
"Tools and materials to support continuous career growth."),

("Career Acceleration Training",
"Focused training to improve employability and job readiness."),

("Global Community Access",
"Connect and collaborate with a diverse international network."),

("Alumni Mentorship & Guidance",
"Ongoing support from experienced mentors and alumni."),

("CV & Profile Enhancement",
"Professional support to improve employability documents."),

("1-1 Advisory Support",
"Dedicated personal guidance throughout the program journey."),

("24/7 Support",
"Continuous assistance across the full program duration."),

("Visa Guidance",
"Structured support for visa preparation and documentation."),

("Accommodation Assistance",
"Support in securing housing where applicable."),

("Airport Arrival Support",
"Arrival coordination and onboarding assistance."),

("Cultural & Social Integration",
"Activities and events for immersion and networking.")
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
st.markdown("## Program Pricing")

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
    "Full Program (AU$)",
    "Without Accommodation (AU$)"
])

st.table(df)

st.divider()

# =========================
# CTA
# =========================
st.markdown("## Ready to Begin Your Journey")

st.write("Submit your application to join the Cultural Infusion Fellowship program.")

if st.button("Apply Now"):
    st.success("Application received. Our team will contact you shortly.")
