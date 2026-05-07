import streamlit as st

st.set_page_config(page_title="Cultural Infusion Fellowship", layout="wide")

# =========================
# HERO SECTION
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
The Cultural Infusion Fellowship combines international experience, 
professional development, and cultural learning into one immersive journey.

Designed for ambitious young individuals, the program provides opportunities 
to gain practical industry exposure, develop globally relevant skills, 
and build meaningful international connections in diverse environments.
"""
)

st.markdown("### Key Areas")
st.write("- Global Internships")
st.write("- Professional Growth")
st.write("- Cultural Immersion")
st.write("- International Networking")
st.write("- Career Development")

st.divider()

# =========================
# EXPERIENCE PATHWAY
# =========================
st.markdown("## Learning & Experience Pathway")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Professional Development")
    st.write("- Structured international internship experience")
    st.write("- Industry-relevant skill building")
    st.write("- Career readiness development")
    st.write("- Leadership capability enhancement")

with col2:
    st.markdown("### Global Exposure")
    st.write("- Immersive cultural integration")
    st.write("- International collaboration opportunities")
    st.write("- Global peer networking")
    st.write("- Real-world cross-cultural experience")

st.divider()

# =========================
# PROGRAM INCLUSIONS
# =========================
st.markdown("## Program Inclusions")

inclusions = [
"International Internship Placement",
"Global Community Access",
"Visa Guidance",
"Cultural Integration Activities",
"Learning & Workshop Series",
"Mentorship & Advisory Support",
"Accommodation Assistance",
"Career Development Support",
"Professional Profile Development",
"Arrival & Onboarding Support"
]

for item in inclusions:
    st.success(item)

st.divider()

# =========================
# PROGRAM INVESTMENT
# =========================
st.markdown("## Program Investment")

pricing = [
("4 Weeks", "AUD 9,340", "AUD 5,600"),
("6 Weeks", "AUD 9,585", "AUD 5,600"),
("8 Weeks", "AUD 11,440", "AUD 5,600"),
("10 Weeks", "AUD 13,295", "AUD 5,600"),
("12 Weeks", "AUD 15,290", "AUD 6,600"),
("16 Weeks", "AUD 18,730", "AUD 6,600"),
("20 Weeks", "AUD 21,460", "AUD 6,600"),
("24 Weeks", "AUD 24,150", "AUD 6,600"),
]

cols = st.columns(4)

for i, (duration, full, without) in enumerate(pricing):
    with cols[i % 4]:
        st.info(f"""
**{duration}**

Full Program  
{full}

Without Accommodation  
{without}
""")

st.divider()

# =========================
# CTA
# =========================
st.markdown("## Begin Your Global Journey")

st.write(
"""
Take the next step toward international experience, professional growth, 
and global exposure through the Cultural Infusion Fellowship.
"""
)

if st.button("Apply Now"):
    st.success("Application received. Our team will contact you shortly.")
