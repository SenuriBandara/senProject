import streamlit as st

st.set_page_config(
    page_title="Cultural Infusion Fellowship",
    layout="wide"
)

# =========================
# GLOBAL STYLES
# =========================
st.markdown("""
<style>

.main {
    background-color: #ffffff;
}

/* HERO SECTION */
.hero {
    padding: 90px 50px;
    background: linear-gradient(135deg, #0b1220 0%, #1e3a8a 100%);
    color: white;
    border-radius: 22px;
    text-align: center;
    margin-bottom: 30px;
}

.hero h1 {
    font-size: 54px;
    font-weight: 700;
    margin-bottom: 15px;
}

.hero p {
    font-size: 19px;
    color: #dbeafe;
    max-width: 850px;
    margin: auto;
    line-height: 1.8;
}

/* SECTION TITLES */
.section-title {
    font-size: 30px;
    font-weight: 700;
    margin-bottom: 15px;
    color: #0f172a;
}

/* GENERAL TEXT */
.subtext {
    font-size: 16px;
    color: #475569;
    line-height: 1.9;
}

/* PROGRAM OVERVIEW */
.overview-box {
    background: #f8fafc;
    padding: 32px;
    border-radius: 18px;
    border-left: 5px solid #1e3a8a;
    height: 100%;
}

.focus-box {
    background: white;
    padding: 30px;
    border-radius: 18px;
    box-shadow: 0 6px 18px rgba(15,23,42,0.08);
    height: 100%;
}

/* INCLUSION CARDS */
.card {
    background: white;
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0 6px 18px rgba(15,23,42,0.08);
    border-top: 4px solid #1e3a8a;
    margin-bottom: 20px;
    height: 100%;
}

.card-title {
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 10px;
    color: #0f172a;
}

.card-text {
    font-size: 14px;
    color: #475569;
    line-height: 1.7;
}

/* PRICING CARDS */
.price-card {
    background: white;
    padding: 24px;
    border-radius: 18px;
    box-shadow: 0 6px 18px rgba(15,23,42,0.08);
    text-align: center;
    border-top: 4px solid #1e3a8a;
    margin-bottom: 20px;
}

.price-duration {
    font-size: 20px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 15px;
}

.price-value {
    font-size: 15px;
    color: #334155;
    margin-bottom: 10px;
    line-height: 1.7;
}

/* CTA SECTION */
.cta-box {
    background: linear-gradient(135deg, #0b1220 0%, #1e3a8a 100%);
    padding: 55px;
    border-radius: 22px;
    text-align: center;
    color: white;
}

.cta-box h2 {
    font-size: 36px;
    margin-bottom: 15px;
}

.cta-box p {
    font-size: 17px;
    color: #dbeafe;
    margin-bottom: 25px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HERO SECTION
# =========================
st.markdown("""
<div class="hero">
    <h1>Cultural Infusion Fellowship</h1>

    <p>
        Where Talent, Opportunity, and Culture Converge
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# PROGRAM OVERVIEW
# =========================
st.markdown("## Program Overview")

col1, col2 = st.columns([2, 1])

with col1:

    st.markdown("""
    <div class="overview-box">

        <div class="section-title">
            Building Future Global Leaders
        </div>

        <div class="subtext">
            The Cultural Infusion Fellowship combines international experience, professional development, and cultural learning into one immersive journey.<br><br>

            Designed for ambitious young individuals, the program provides opportunities to gain practical industry exposure, develop globally relevant skills, and build meaningful international connections in diverse environments.
        </div>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="focus-box">

        <div class="section-title">
            Key Areas
        </div>

        <div class="subtext">
            Global Internships<br>
            Professional Growth<br>
            Cultural Immersion<br>
            International Networking<br>
            Career Development
        </div>

    </div>
    """, unsafe_allow_html=True)

st.write("")
st.divider()

# =========================
# EXPERIENCE SECTION
# =========================
st.markdown("## Learning & Experience Pathway")

exp1, exp2 = st.columns(2)

with exp1:

    st.markdown("""
    ### Professional Development

    - Structured international internship experience  
    - Industry-relevant skill building  
    - Career readiness development  
    - Leadership capability enhancement  
    """)

with exp2:

    st.markdown("""
    ### Global Exposure

    - Immersive cultural integration  
    - International collaboration opportunities  
    - Global peer networking  
    - Real-world cross-cultural experience  
    """)

st.write("")
st.divider()

# =========================
# PROGRAM INCLUSIONS
# =========================
st.markdown("## Program Inclusions")

included = [

("International Internship Placement",
"Structured professional experience within global organisations."),

("Learning & Workshop Series",
"Practical sessions designed to support personal and professional growth."),

("Career Development Support",
"Tools and guidance to strengthen employability and career readiness."),

("Global Community Access",
"Connections with international participants and professionals."),

("Mentorship & Advisory Support",
"Guidance from experienced mentors throughout the journey."),

("Professional Profile Development",
"Support in CV enhancement and personal branding."),

("Visa Guidance",
"Structured support for visa preparation and documentation."),

("Accommodation Assistance",
"Guidance in securing suitable housing arrangements."),

("Arrival & Onboarding Support",
"Coordination and support upon arrival in destination."),

("Cultural Integration Activities",
"Experiences and events designed for immersion and networking.")

]

def render_cards(data):

    cols = st.columns(3)

    for i, (title, desc) in enumerate(data):

        with cols[i % 3]:

            card_html = f"""
            <div class="card">

                <div class="card-title">
                    {title}
                </div>

                <div class="card-text">
                    {desc}
                </div>

            </div>
            """

            st.markdown(card_html, unsafe_allow_html=True)

render_cards(included)

st.write("")
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

        card_html = f"""
        <div class="price-card">

            <div class="price-duration">
                {duration}
            </div>

            <div class="price-value">
                <b>Full Program</b><br>
                {full}
            </div>

            <div class="price-value" style="margin-top:15px;">
                <b>Without Accommodation</b><br>
                {without}
            </div>

        </div>
        """

        st.markdown(card_html, unsafe_allow_html=True)

st.write("")
st.divider()

# =========================
# CTA SECTION
# =========================
st.markdown("""
<div class="cta-box">

    <h2>
        Begin Your Global Journey
    </h2>

    <p>
        Take the next step toward international experience, professional growth, and global exposure through the Cultural Infusion Fellowship.
    </p>

</div>
""", unsafe_allow_html=True)

st.write("")

if st.button("Apply Now"):
    st.success("Application received. Our team will contact you shortly.")
