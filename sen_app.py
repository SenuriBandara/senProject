import streamlit as st

st.set_page_config(page_title="Cultural Infusion Fellowship", layout="wide")

# =========================
# HERO
# =========================
st.title("Cultural Infusion Fellowship")
st.subheader("Where Talent, Opportunity, and Culture Converge")

st.divider()

# =========================
# PROGRAM OVERVIEW
# =========================
st.markdown("## Program Overview")

st.write(
"""
The Cultural Infusion Fellowship is a global experience designed to build future-ready talent through international exposure, cultural immersion, and professional development.
"""
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### What You Get")
    st.write("✔ Global Internship Experience")
    st.write("✔ Professional Skill Development")
    st.write("✔ Cultural Immersion")
    st.write("✔ International Networking")

with col2:
    st.markdown("### Outcomes")
    st.write("✔ Global mindset")
    st.write("✔ Career readiness")
    st.write("✔ Cross-cultural communication")
    st.write("✔ Industry exposure")

st.divider()

# =========================
# EXPERIENCE
# =========================
st.markdown("## Learning & Experience Pathway")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Professional Development")
    st.write("• Internship experience")
    st.write("• Skill development")
    st.write("• Career readiness")
    st.write("• Leadership growth")

with col2:
    st.markdown("### Global Exposure")
    st.write("• Cultural immersion")
    st.write("• Networking opportunities")
    st.write("• Real-world experience")
    st.write("• International collaboration")

st.divider()

# =========================
# PROGRAM INCLUSIONS (UPDATED PREMIUM VERSION)
# =========================
st.markdown("## Program Inclusions")

included = [

("International Internship Placement",
"High-quality, structured internship experience with global organisations aligned to your career pathway."),

("Learning & Development Workshops",
"Expert-led sessions focused on professional skills, leadership, and global employability."),

("Career Acceleration Support",
"Personalised tools and guidance to enhance employability and long-term career growth."),

("Global Talent Network Access",
"Connect with a diverse international community of peers, mentors, and professionals."),

("1:1 Mentorship & Advisory",
"Ongoing guidance from experienced industry mentors throughout your journey."),

("Professional Branding & CV Development",
"Support to build a strong personal brand, CV, and global-ready profile."),

("Visa & Documentation Support",
"Structured assistance throughout your visa process and required documentation."),

("Accommodation Guidance",
"Support in finding safe, suitable, and well-located housing options."),

("Arrival & Transition Support",
"On-the-ground coordination to ensure a smooth landing and onboarding experience."),

("Cultural Immersion Experiences",
"Curated activities and events designed to deepen cultural understanding and engagement.")

]

for title, desc in included:
    st.markdown(f"### {title}")
    st.write(desc)

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
Join the Cultural Infusion Fellowship and unlock international experience, professional growth, and global exposure.
"""
)

if st.button("Apply Now"):
    st.success("Application received. Our team will contact you shortly.")
