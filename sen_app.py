import streamlit as st

st.set_page_config(page_title="Cultural Infusion Fellowship", layout="wide")

# ---------- STYLES ----------
st.markdown("""
<style>
.hero {
    padding: 70px 40px;
    background: linear-gradient(to right, #0f172a, #1e3a8a);
    color: white;
    border-radius: 15px;
    text-align: center;
}

.section {
    padding: 30px 10px;
}

.title {
    font-size: 42px;
    font-weight: 700;
}

.subtitle {
    font-size: 20px;
    margin-top: 10px;
    color: #e5e7eb;
}

.btn {
    background-color: #f59e0b;
    color: white;
    padding: 12px 20px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: bold;
    display: inline-block;
    margin-top: 20px;
}

.card {
    padding: 20px;
    border-radius: 12px;
    background: #f8f9fa;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown("""
<div class="hero">
    <div class="title">Cultural Infusion Fellowship</div>
    <div class="subtitle">
        Experience global cultures, develop future-ready skills, and grow through immersive international opportunities.
    </div>
    <a class="btn">Apply Now</a>
</div>
""", unsafe_allow_html=True)

st.write("")

# ---------- FEATURE STRIP ----------
st.markdown("### FEATURED ON GLOBAL YOUTH & EDUCATION NETWORKS")
st.write("⭐⭐⭐⭐⭐ Trusted by universities, institutions, and global partners")

st.divider()

# ---------- INTRO ----------
st.markdown("""
## In-Person Fellowship Program

Experience new cultures and lifestyles with complete immersion in a new location.  
The Cultural Infusion Fellowship is designed for young people who want to travel, learn, and grow while engaging in meaningful global experiences.

You will connect with diverse communities, build international friendships, and gain exposure to real-world professional environments that shape your global career journey.
""")

st.divider()

# ---------- BOOST EMPLOYABILITY ----------
st.markdown("## 🚀 Boost Your Employability")

st.markdown("""
The Cultural Infusion Fellowship offers structured in-person experiences designed for professional and personal development.

Participants gain exposure across multiple fields, combining real-world experience with cultural immersion.  
This program helps you build:

- Global mindset  
- Cross-cultural communication skills  
- Professional industry experience  
- International network  
- Leadership and independence  

By completing the fellowship, you demonstrate adaptability, curiosity, and the ability to thrive in diverse environments — qualities highly valued by global employers.
""")

st.divider()

# ---------- EXPERIENCE ----------
st.markdown("## 🌍 Explore, Adventure, and Make Friends")

col1, col2 = st.columns([1,1])

with col1:
    st.markdown("""
You’ll experience a new country while being fully supported by our on-the-ground team.

- Work in a real professional environment  
- Join cultural and social experiences  
- Live with a global community of fellows  
- Travel and explore your host city  
""")

with col2:
    st.info("""
✨ What makes this special:

- Immersive cultural experience  
- Global peer network  
- Career-focused learning  
- Lifelong friendships  
""")

st.divider()

# ---------- SUPPORT ----------
st.markdown("## 🤝 How We Support You")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.success("🛂 Visa Support\nGuidance before and during your journey")

with c2:
    st.success("🌍 On-the-Ground Team\nLocal support in every destination")

with c3:
    st.success("🎉 Orientation\nMeet your peers & explore your city")

with c4:
    st.success("📞 24/7 Support\nAlways available when you need help")

st.divider()

# ---------- CTA ----------
st.markdown("## ✈️ Ready to Start Your Journey?")

if st.button("Apply Now"):
    st.success("Thanks! Our team will contact you soon regarding your application.")
