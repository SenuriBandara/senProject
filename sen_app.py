import streamlit as st

st.set_page_config(page_title="Cultural Infusion Fellowship", layout="wide")

# =========================
# STYLES
# =========================
st.markdown("""
<style>

.hero {
    padding: 85px 50px;
    background: linear-gradient(135deg, #0b1220 0%, #1e3a8a 100%);
    color: white;
    border-radius: 22px;
    text-align: center;
}

.hero h1 {
    font-size: 52px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 18px;
    color: #dbeafe;
}

.section-title {
    font-size: 28px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 10px;
}

.subtext {
    font-size: 15px;
    color: #475569;
    line-height: 1.8;
}

.overview-box {
    background: #f8fafc;
    padding: 30px;
    border-radius: 18px;
    border-left: 5px solid #1e3a8a;
}

.focus-box {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
}

.card {
    background: white;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    border-top: 4px solid #1e3a8a;
    margin-bottom: 20px;
}

.card-title {
    font-weight: 600;
    margin-bottom: 8px;
}

.card-text {
    font-size: 14px;
    color: #475569;
    line-height: 1.6;
}

.price-card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    text-align: center;
    border-top: 4px solid #1e3a8a;
    margin-bottom: 20px;
}

.price-duration {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 12px;
    color: #0f172a;
}

.price-value {
    font-size: 14px;
    color: #334155;
    margin-bottom: 10px;
    line-height: 1.6;
}

.cta {
    background: linear-gradient(135deg, #0b1220, #1e3a8a);
    padding: 50px;
    border-radius: 22px;
    text-align: center;
    color: white;
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

# =========================
# PROGRAM OVERVIEW
# =========================
st.markdown("## Program Overview")

col1, col2 = st.columns([2,1])

with col1:
    st.markdown("""
    <div class="overview-box">
        <div class="section-title">Building Future Global Leaders</div>
        <div class="subtext">
            The Cultural Infusion Fellowship combines international experience,
            professional development, and cultural learning into one immersive journey.<br><br>

            It prepares young individuals with global exposure, practical skills,
            and international opportunities.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="focus-box">
        <div class="section-title">Key Areas</div>
        <div class="subtext">
            Global Internships<br>
            Professional Growth<br>
            Cultural Immersion<br>
            Networking<br>
            Career Development
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =========================
# EXPERIENCE
# =========================
st.markdown("## Experience Pathway")

c1, c2 = st.columns(2)

with c1:
    st.markdown("""
    ### Professional Development
    - Internship experience  
    - Skill development  
    - Career readiness  
    """)

with c2:
    st.markdown("""
    ### Global Exposure
    - Cultural immersion  
    - Global networking  
    - Real-world experience  
    """)

st.divider()

# =========================
# PROGRAM INCLUSIONS
# =========================
st.markdown("## Program Inclusions")

included = [
("Internship Placement","Real-world professional experience."),
("Workshops","Skill-building sessions."),
("Mentorship","Guided career support."),
("Networking","Global connections."),
("Visa Support","Application guidance."),
("Accommodation","Housing assistance."),
]

cols = st.columns(3)

for i, (title, desc) in enumerate(included):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">{title}</div>
            <div class="card-text">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# =========================
# PRICING (FIXED VERSION)
# =========================
st.markdown("## Program Investment")

pricing = [
("4 Weeks","AUD 9,340","AUD 5,600"),
("6 Weeks","AUD 9,585","AUD 5,600"),
("8 Weeks","AUD 11,440","AUD 5,600"),
("10 Weeks","AUD 13,295","AUD 5,600"),
]

cols = st.columns(4)

for i, (duration, full, without) in enumerate(pricing):

    with cols[i % 4]:

        st.markdown(f"""
        <div class="price-card">

            <div class="price-duration">{duration}</div>

            <div class="price-value">
                <b>Full Program</b><br>
                {full}
            </div>

            <div class="price-value">
                <b>Without Accommodation</b><br>
                {without}
            </div>

        </div>
        """, unsafe_allow_html=True)

st.divider()

# =========================
# CTA
# =========================
st.markdown("""
<div class="cta">
    <h2>Begin Your Global Journey</h2>
    <p>Apply now to join the Cultural Infusion Fellowship.</p>
</div>
""", unsafe_allow_html=True)

if st.button("Apply Now"):
    st.success("Application received. We'll contact you soon.")
