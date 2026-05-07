import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cultural Infusion Fellowship", layout="wide")

# =========================
# 🎨 STYLES
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
    font-size: 30px;
    font-weight: 700;
    margin-top: 50px;
}

.text {
    font-size: 16px;
    color: #333;
    line-height: 1.6;
}

.card {
    background: white;
    padding: 22px;
    border-radius: 14px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    text-align: center;
    margin-bottom: 15px;
}

.price-card {
    background: #f8f9fa;
    padding: 20px;
    border-radius: 14px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

.price {
    font-size: 24px;
    font-weight: bold;
    color: #1e3a8a;
}

.duration {
    font-weight: 600;
    font-size: 18px;
}

.note {
    font-size: 12px;
    color: gray;
}

</style>
""", unsafe_allow_html=True)

# =========================
# 🚀 HERO SECTION
# =========================
st.markdown("""
<div class="hero">
    <h1>Cultural Infusion Fellowship</h1>
    <p>Where Talent, Opportunity, and Culture Converge</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# =========================
# 📌 PROGRAM BRIEF
# =========================
st.markdown("## 🌍 Program Overview")

st.markdown("""
<div class="text">
A youth-focused global ecosystem designed to develop globally competent talent through structured development experiences and international mobility pathways.

The initiative connects youth, universities, companies, and institutions through an integrated system that links engagement with skill development and real-world global exposure.
</div>
""", unsafe_allow_html=True)

st.divider()

# =========================
# 🎯 OBJECTIVES
# =========================
st.markdown("## 🎯 Primary Objectives")

objectives = [
"Establish a scalable global youth platform extending impact beyond programs",
"Strengthen intercultural development and global mobility pathways",
"Create sustainable revenue through structured programs and partnerships",
"Build a strong global talent pipeline and community",
"Expand partnerships with universities and companies",
"Convert demand into structured programs",
"Enhance global brand visibility",
"Develop scalable systems across regions"
]

for i, obj in enumerate(objectives, 1):
    st.markdown(f"{i}. {obj}")

st.divider()

# =========================
# 🌍 EXPERIENCE SECTION
# =========================
st.markdown("## 🌏 Explore, Learn, and Grow")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 💼 Professional Growth
    - Real-world internship exposure  
    - Industry-based learning  
    - Skill development  
    - Career acceleration  
    """)

with col2:
    st.markdown("""
    ### 🤝 Global Experience
    - Cultural immersion  
    - International friendships  
    - Local events & travel  
    - Global networking  
    """)

st.divider()

# =========================
# 🤝 SUPPORT SECTION
# =========================
st.markdown("## 🛡️ How We Support You")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.success("🛂 Visa Support\nEnd-to-end guidance")

with c2:
    st.success("🌍 Local Team\nOn-ground assistance")

with c3:
    st.success("🎉 Orientation\nMeet & connect globally")

with c4:
    st.success("📞 24/7 Support\nAlways available")

st.divider()

# =========================
# 💼 PRICING SECTION
# =========================
st.markdown("## 💼 Program Pricing")

pricing = [
("4 Weeks", 9340),
("6 Weeks", 9585),
("8 Weeks", 11440),
("10 Weeks", 13295),
("12 Weeks", 15290),
("16 Weeks", 18730),
("20 Weeks", 21460),
("24 Weeks", 24150),
]

no_accommodation = {
"4 Weeks": 5600,
"6 Weeks": 5600,
"8 Weeks": 5600,
"10 Weeks": 5600,
"12 Weeks": 6600,
"16 Weeks": 6600,
"20 Weeks": 6600,
"24 Weeks": 6600,
}

cols = st.columns(4)

for i, (duration, price) in enumerate(pricing):
    with cols[i % 4]:
        st.markdown(f"""
        <div class="price-card">
            <div class="duration">{duration}</div>
            <div class="price">AU$ {price:,}</div>
            <div class="note">Without Accommodation: AU$ {no_accommodation[duration]:,}</div>
        </div>
        """, unsafe_allow_html=True)

st.write("")

# TABLE VIEW (backup)
df = pd.DataFrame({
    "Duration": [d[0] for d in pricing],
    "Full Program (AU$)": [d[1] for d in pricing],
    "Without Accommodation (AU$)": [no_accommodation[d[0]] for d in pricing]
})

st.markdown("### 📊 Pricing Summary")
st.table(df)

# =========================
# 🚀 CTA
# =========================
st.markdown("## 🚀 Ready to Start Your Journey?")

if st.button("Apply Now"):
    st.success("🎉 Application received! Our team will reach out to you soon.")
