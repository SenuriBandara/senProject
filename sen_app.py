import streamlit as st

st.set_page_config(page_title="Cultural Infusion Fellowship", layout="wide")

# =========================
# HERO
# =========================
st.title("Cultural Infusion Fellowship")
st.subheader("Where Talent, Opportunity, and Culture Converge")

st.divider()

# =========================
# OVERVIEW
# =========================
st.markdown("## Program Overview")

st.write(
"""
The Cultural Infusion Fellowship is a global development experience that combines international exposure,
professional learning, and cultural immersion into one structured journey for young talent.
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
# INCLUSIONS (SAFE UI)
# =========================
st.markdown("## Program Inclusions")

inclusions = [
"Internship Placement",
"Workshops & Training",
"Mentorship Support",
"Visa Guidance",
"Accommodation Support",
"Global Networking",
"Cultural Activities",
"Career Support"
]

for item in inclusions:
    st.success(item)

st.divider()

# =========================
# PRICING (SAFE TABLE - NO HTML)
# =========================
st.markdown("## Program Investment")

st.table({
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
})

st.divider()

# =========================
# CTA
# =========================
st.markdown("## Begin Your Global Journey")

st.write(
"""
Join the Cultural Infusion Fellowship and gain international experience,
professional growth, and cultural exposure.
"""
)

if st.button("Apply Now"):
    st.success("Application received. Our team will contact you shortly.")
