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

.text {
    font-size: 16px;
    color: #333;
    line-height: 1.7;
}

.support-card {
    background: white;
    padding: 15px;
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
### Visa Support
End-to-end guidance for travel documentation
""")

with c2:
    st.markdown("""
### Local Team
On-ground assistance in all destinations
""")

with c3:
    st.markdown("""
### Orientation
Structured onboarding and cultural preparation
""")

with c4:
    st.markdown("""
### 24/7 Support
Continuous assistance throughout the program
""")

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
    "Full Program (Avg AU$)",
    "Without Accommodation (AU$)"
])

st.table(df)

st.divider()

# =========================
# CTA
# =========================
st.markdown("## Ready to Begin Your Journey")

st.write("Submit your application to be considered for upcoming cohorts.")

if st.button("Apply Now"):
    st.success("Application received. Our team will contact you shortly.")
