import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cultural Infusion Fellowship", layout="wide")

# =========================
# STYLES
# =========================
st.markdown("""
<style>

.hero {
    padding: 70px 40px;
    background: linear-gradient(to right, #0f172a, #1e3a8a);
    color: white;
    border-radius: 18px;
    text-align: center;
}

.hero h1 {
    font-size: 42px;
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

.text {
    font-size: 16px;
    color: #333;
    line-height: 1.7;
}

.block {
    background: #f8f9fa;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 10px;
    border-left: 4px solid #1e3a8a;
}

.support-box {
    background: #ffffff;
    padding: 18px;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    text-align: center;
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
# PROGRAM OVERVIEW
# =========================
st.markdown("## Program Overview")

st.markdown("""
<div class="text">
A youth-focused global ecosystem designed to develop globally competent talent through structured development experiences and international mobility pathways.

The initiative connects youth, universities, companies, and institutions through an integrated system that links engagement with skill development and real-world global exposure.
</div>
""", unsafe_allow_html=True)

st.divider()

# =========================
# OBJECTIVES
# =========================
st.markdown("## Primary Objectives")

objectives = [
"Establish a scalable global youth platform extending impact beyond programs",
"Strengthen intercultural development and global mobility pathways",
"Create sustainable revenue through structured programs and partnerships",
"Build a strong global talent pipeline and community",
"Expand partnerships with universities and companies",
"Convert demand into structured and repeatable programs",
"Enhance global brand visibility",
"Develop scalable systems across regions and markets"
]

for i, obj in enumerate(objectives, 1):
    st.markdown(f"{i}. {obj}")

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
# SUPPORT
# =========================
st.markdown("## Support Structure")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
<div class="support-box">
Visa Support<br>
End-to-end guidance for travel documentation
</div>
""", unsafe_allow_html=True)

with c2:
    st.markdown("""
<div class="support-box">
Local Team<br>
On-ground assistance in all destinations
</div>
""", unsafe_allow_html=True)

with c3:
    st.markdown("""
<div class="support-box">
Orientation<br>
Structured onboarding and cultural preparation
</div>
""", unsafe_allow_html=True)

with c4:
    st.markdown("""
<div class="support-box">
24/7 Support<br>
Continuous assistance throughout the program
</div>
""", unsafe_allow_html=True)

st.divider()

# =========================
# PRICING TABLE (KEPT)
# =========================
st.markdown("## Program Pricing")

pricing = [
("4 Weeks", 9340, 5600),
("6 Weeks", 9585, 5600),
("8 Weeks", 11440, 5600),
("10 Weeks", 13295, 5600),
("12 Weeks", 15290, 6600),
("16 Weeks", 18730, 6600),
("20 Weeks", 21460, 6600),
("24 Weeks", 24150, 6600),
]

df = pd.DataFrame(pricing, columns=[
    "Duration",
    "Full Program (Avg AU$)",
    "Without Accommodation (AU$)"
])

st.table(df)

# =========================
# CTA
# =========================
st.markdown("## Ready to Begin Your Journey")

st.write("Submit your application to be considered for upcoming cohorts.")

if st.button("Apply Now"):
    st.success("Application received. Our team will contact you shortly.")
