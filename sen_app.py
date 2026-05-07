# Cultural Infusion Fellowship — Final Fixed Streamlit Code

```python
import streamlit as st

st.set_page_config(page_title="Cultural Infusion Fellowship", layout="wide")

# =========================
# CSS STYLES
# =========================
st.markdown("""
<style>

.hero {
    padding: 90px 40px;
    background: linear-gradient(135deg, #0f172a, #1e3a8a);
    border-radius: 24px;
    text-align: center;
    color: white;
    margin-bottom: 40px;
}

.hero h1 {
    font-size: 52px;
    margin-bottom: 15px;
}

.hero p {
    font-size: 20px;
    color: #dbeafe;
}

.section-title {
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 15px;
    color: #0f172a;
}

.text {
    font-size: 16px;
    color: #475569;
    line-height: 1.8;
}

.overview-box {
    background: #f8fafc;
    padding: 30px;
    border-radius: 20px;
    border-left: 5px solid #1e3a8a;
}

.focus-box {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.08);
}

.card {
    background: white;
    padding: 24px;
    border-radius: 18px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    border-top: 4px solid #1e3a8a;
    margin-bottom: 20px;
}

.card-title {
    font-size: 17px;
    font-weight: 600;
    margin-bottom: 10px;
    color: #0f172a;
}

.card-text {
    font-size: 14px;
    color: #475569;
    line-height: 1.7;
}

.price-card {
    background: white;
    padding: 24px;
    border-radius: 18px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    border-top: 4px solid #1e3a8a;
    text-align: center;
    margin-bottom: 20px;
}

.price-duration {
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 15px;
    color: #0f172a;
}

.price-value {
    font-size: 15px;
    color: #334155;
    line-height: 1.8;
    margin-bottom: 12px;
}

.cta {
    background: linear-gradient(135deg, #0f172a, #1e3a8a);
    padding: 60px;
    border-radius: 24px;
    text-align: center;
    color: white;
    margin-top: 40px;
}

.cta h2 {
    font-size: 38px;
    margin-bottom: 15px;
}

.cta p {
    font-size: 18px;
    color: #dbeafe;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HERO SECTION
# =========================
st.markdown('''
<div class="hero">
    <h1>Cultural Infusion Fellowship</h1>
    <p>Where Talent, Opportunity, and Culture Converge</p>
</div>
''', unsafe_allow_html=True)

# =========================
# PROGRAM OVERVIEW
# =========================
st.markdown("## Program Overview")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('''
    <div class="overview-box">
        <div class="section-title">Building Future Global Leaders</div>

        <div class="text">
            The Cultural Infusion Fellowship combines international experience,
            professional development, and cultural learning into one immersive journey.
            <br><br>
            Designed for ambitious young individuals, the program provides opportunities
            to gain practical industry exposure, develop globally relevant skills,
            and build meaningful international connections in diverse environments.
        </div>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown('''
    <div class="focus-box">
        <div class="section-title">Key Areas</div>

        <div class="text">
            Global Internships<br>
            Professional Growth<br>
            Cultural Immersion<br>
            International Networking<br>
            Career Development
        </div>
    </div>
    ''', unsafe_allow_html=True)

st.divider()

# =========================
# EXPERIENCE SECTION
# =========================
st.markdown("## Learning & Experience Pathway")

exp1, exp2 = st.columns(2)

with exp1:
    st.markdown('''
    ### Professional Development

    - Structured international internship experience
    - Industry-relevant skill development
    - Career readiness enhancement
    - Leadership capability building
    ''')

with exp2:
    st.markdown('''
    ### Global Exposure

    - Immersive cultural integration
    - International collaboration opportunities
    - Global peer networking
    - Real-world cross-cultural experience
    ''')

st.divider()

# =========================
# PROGRAM INCLUSIONS
# =========================
st.markdown("## Program Inclusions")

included = [
    ("International Internship Placement", "Structured professional experience within global organisations."),
    ("Learning & Workshop Series", "Practical sessions supporting personal and professional growth."),
    ("Career Development Support", "Guidance to strengthen employability and long-term career readiness."),
    ("Global Community Access", "Connections with international participants and professionals."),
    ("Mentorship Support", "Guidance from experienced mentors and industry professionals."),
    ("Professional Profile Development", "Support in CV enhancement and personal branding."),
    ("Visa Guidance", "Structured support for visa preparation and documentation."),
    ("Accommodation Assistance", "Guidance in securing suitable housing arrangements."),
    ("Arrival Support", "Onboarding assistance upon arrival in destination."),
    ("Cultural Integration Activities", "Experiences and events designed for immersion and networking.")
]

cols = st.columns(3)

for i, (title, desc) in enumerate(included):
    with cols[i % 3]:
        st.markdown(f'''
        <div class="card">
            <div class="card-title">{title}</div>
            <div class="card-text">{desc}</div>
        </div>
        ''', unsafe_allow_html=True)

st.divider()

# =========================
# PRICING SECTION
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
    ("24 Weeks", "AUD 24,150", "AUD 6,600")
]

price_cols = st.columns(4)

for i, (duration, full, without) in enumerate(pricing):
    with price_cols[i % 4]:
        st.markdown(f'''
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
        ''', unsafe_allow_html=True)

# =========================
# CTA SECTION
# =========================
st.markdown('''
<div class="cta">
    <h2>Begin Your Global Journey</h2>

    <p>
        Take the next step toward international experience,
        professional growth, and global exposure through the
        Cultural Infusion Fellowship.
    </p>
</div>
''', unsafe_allow_html=True)

st.write("")

if st.button("Apply Now"):
    st.success("Application received. Our team will contact you shortly.")
```

## Run the app

```bash
streamlit run app.py
```
