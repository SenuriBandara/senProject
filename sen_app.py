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

col1, col2 = st.columns([2, 1])

with col1:
    st.info(
        "The Cultural Infusion Fellowship combines international experience, "
        "professional development, and cultural learning into one immersive journey.\n\n"
        "It prepares young individuals with global exposure, practical skills, "
        "and international opportunities."
    )

with col2:
    st.success(
        "**Key Areas**\n\n"
        "- Global Internships\n"
        "- Professional Growth\n"
        "- Cultural Immersion\n"
        "- Networking\n"
        "- Career Development"
    )

st.divider()

# =========================
# EXPERIENCE
# =========================
st.markdown("## Experience Pathway")

c1, c2 = st.columns(2)

with c1:
    st.markdown("### Professional Development")
    st.write("- Internship experience")
    st.write("- Skill development")
    st.write("- Career readiness")

with c2:
    st.markdown("### Global Exposure")
    st.write("- Cultural immersion")
    st.write("- Global networking")
    st.write("- Real-world experience")

st.divider()

# =========================
# PROGRAM INCLUSIONS
# =========================
st.markdown("## Program Inclusions")

inclusions = [
"Internship Placement",
"Workshops & Training",
"Mentorship Support",
"Global Networking",
"Visa Guidance",
"Accommodation Support",
"Arrival Assistance",
"Cultural Activities"
]

cols = st.columns(2)

for i, item in enumerate(inclusions):
    with cols[i % 2]:
        st.checkbox(item, value=True)

st.divider()

# =========================
# PRICING (NO HTML - CLEAN TABLE STYLE)
# =========================
st.markdown("## Program Investment")

data = {
    "Duration": ["4 Weeks", "6 Weeks", "8 Weeks", "10 Weeks"],
    "Full Program": ["AUD 9,340", "AUD 9,585", "AUD 11,440", "AUD 13,295"],
    "Without Accommodation": ["AUD 5,600", "AUD 5,600", "AUD 5,600", "AUD 5,600"]
}

st.table(data)

st.divider()

# =========================
# CTA
# =========================
st.subheader("Begin Your Global Journey")

if st.button("Apply Now"):
    st.success("Application received. Our team will contact you soon.")
