# =========================
# WHAT'S INCLUDED (PREMIUM CARDS)
# =========================
st.markdown("## Program Inclusions")

st.markdown("""
<style>
.included-card {
    background: #ffffff;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    height: 100%;
    border-left: 4px solid #1e3a8a;
}

.included-title {
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 8px;
    color: #111;
}

.included-text {
    font-size: 14px;
    color: #555;
    line-height: 1.5;
}
</style>
""", unsafe_allow_html=True)

# =========================
# DATA (GROUPED)
# =========================
core = [
("International Internship Placement",
"Real-world in-person internship experience in a global environment."),

("Workshop & Learning Series",
"Structured sessions designed to build practical and professional skills."),

("Professional Development Resources",
"Tools and materials to support continuous career growth."),

("Career Acceleration Training",
"Focused training to improve employability and job readiness."),

("Global Community Access",
"Connect and collaborate with a diverse international network of participants.")
]

career = [
("Alumni Mentorship & Guidance",
"Ongoing support from past participants and industry mentors."),

("CV & Profile Enhancement",
"Professional support to improve employability documents and profiles."),

("1-1 Dedicated Advisory Support",
"Personal guidance throughout the full program journey.")
]

support = [
("24/7 Participant Support",
"Continuous assistance throughout the program duration."),

("Visa Guidance Support",
"Structured help with visa preparation and documentation."),

("Accommodation Assistance",
"Support in securing housing options where applicable."),

("Airport Arrival Support",
"Guidance and coordination upon arrival in destination country."),

("Cultural & Social Integration",
"Activities and events to support cultural immersion and connection.")
]

# =========================
# RENDER CARDS
# =========================
def render_cards(items):
    cols = st.columns(3)
    for i, (title, desc) in enumerate(items):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="included-card">
                <div class="included-title">{title}</div>
                <div class="included-text">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

st.markdown("### Core Experience")
render_cards(core)

st.markdown("### Career & Growth Support")
render_cards(career)

st.markdown("### Program Support Services")
render_cards(support)
