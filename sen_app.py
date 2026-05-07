import streamlit as st

st.set_page_config(page_title="Cultural Infusion Fellowship", layout="wide")

# =========================
# HEADER
# =========================
st.title("Cultural Infusion Fellowship")
st.subheader("Where Talent, Opportunity, and Culture Converge")

st.divider()

# =========================
# PROGRAM OVERVIEW
# =========================
st.markdown("## Program Overview")

st.markdown("### Building Future Global Leaders")

st.write(
"""
The Cultural Infusion Fellowship combines international experience, professional development, and cultural learning into one immersive journey.

Designed for ambitious young individuals, the program provides opportunities to gain practical industry exposure, develop globally relevant skills, and build meaningful international connections.
"""
)

st.markdown("### Key Areas")
st.write("""
- Global Internships  
- Professional Growth  
- Cultural Immersion  
- International Networking  
- Career Development  
""")

st.divider()

# =========================
# LEARNING PATHWAY
# =========================
st.markdown("## Learning & Experience Pathway")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Professional Development")
    st.write("""
    - Structured international internship experience  
    - Industry-relevant skill building  
    - Career readiness development  
    - Leadership capability enhancement  
    """)

with col2:
    st.markdown("### Global Exposure")
    st.write("""
    - Immersive cultural integration  
    - International collaboration opportunities  
    - Global peer networking  
    - Cross-cultural real-world experience  
    """)

st.divider()

# =========================
# PROGRAM INCLUSIONS
# =========================
st.markdown("## Program Inclusions")

st.write("""
- International Internship Placement: High-quality structured internship with global organisations aligned to your career path  
- Learning & Development Workshops: Expert-led sessions focused on professional skills and global employability  
- Career Acceleration Support: Tools and guidance to strengthen long-term career growth  
- Global Talent Network Access: Connect with international peers, mentors, and professionals  
- 1:1 Mentorship & Advisory: Ongoing guidance from experienced industry mentors  
- Professional Branding & CV Development: Support to build a strong global-ready profile  
- Visa & Documentation Support: Structured assistance throughout visa processing  
- Accommodation Guidance: Support in finding safe and suitable housing  
- Arrival & Transition Support: On-ground support for smooth onboarding  
- Cultural Immersion Experiences: Curated activities for deep cultural engagement  
""")

st.divider()

# =========================
# PRICING
# =========================
st.markdown("## Program Investment")

pricing_data = {
    "Duration": [
        "4 Weeks", "6 Weeks", "8 Weeks", "10 Weeks",
        "12 Weeks", "16 Weeks", "20 Weeks", "24 Weeks"
    ],
    "Full Program (AUD)": [
        "9,340", "9,585", "11,440", "13,295",
        "15,290", "18,730", "21,460", "24,150"
    ],
    "Without Accommodation (AUD)": [
        "5,600", "5,600", "5,600", "5,600",
        "6,600", "6,600", "6,600", "6,600"
    ]
}

st.table(pricing_data)

st.divider()

# =========================
# CTA
# =========================
st.markdown("## Begin Your Global Journey")

st.write(
"""
Join Cultural Infusion Fellowship and unlock global opportunities, professional growth, and cultural exposure.
"""
)

if st.button("Apply Now"):
    st.success("Application received. Our team will contact you soon.")
