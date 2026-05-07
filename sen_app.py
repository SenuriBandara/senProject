import streamlit as st

st.set_page_config(page_title="Cultural Infusion Fellowship", layout="wide")

# ---------- STYLES ----------
st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    margin-top: 30px;
}

.subtitle {
    font-size: 20px;
    text-align: center;
    color: #555;
    margin-bottom: 40px;
}

.section-title {
    font-size: 28px;
    font-weight: 600;
    margin-top: 40px;
}

.box {
    background-color: #f8f9fa;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 15px;
    border-left: 5px solid #1e3a8a;
}

.highlight {
    background: linear-gradient(to right, #1e3a8a, #0f172a);
    color: white;
    padding: 40px;
    border-radius: 15px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown('<div class="highlight">', unsafe_allow_html=True)
st.markdown("# Cultural Infusion Fellowship")
st.markdown("### Where Talent, Opportunity, and Culture Converge")
st.markdown("</div>", unsafe_allow_html=True)

st.write("")

# ---------- DESCRIPTION ----------
st.markdown("""
A youth-focused global ecosystem designed to develop globally competent talent through structured development experiences and international mobility pathways.

The initiative connects youth, universities, companies, and institutions through an integrated system that links engagement with skill development and real-world global exposure.
""")

st.divider()

# ---------- OBJECTIVES ----------
st.markdown("## 🎯 Primary Objectives for Cultural Infusion")

objectives = [
"Establish a scalable global youth platform that extends Cultural Infusion’s impact beyond programs into a structured, long-term ecosystem",
"Strengthen market positioning in intercultural development by embedding cultural intelligence into career pathways and global mobility",
"Create sustainable revenue streams through structured programs, partnerships, and global opportunities aligned with the organisation’s mission",
"Build a strong talent pipeline and community that continuously engages youth and feeds into multiple program offerings",
"Expand strategic partnerships with universities, companies, and institutions to increase reach, credibility, and long-term collaboration",
"Leverage existing demand to drive growth by converting interest into structured, repeatable programs",
"Enhance brand visibility and global presence by positioning Cultural Infusion as a leader in youth development and intercultural capability",
"Develop scalable systems and operating models that can be replicated across regions and markets"
]

for i, obj in enumerate(objectives, 1):
    st.markdown(f"**{i}.** {obj}")

st.divider()

# ---------- COMMERCIAL PATHWAYS ----------
st.markdown("## 💼 Commercial Pathways")

pathways = {
"Structured Internship Programs (Internal)": 
"Delivery of in-house internship experiences within Cultural Infusion, providing youth with practical exposure and structured development.",

"External Internship Placements":
"Coordination of internship opportunities with partner organisations, connecting youth with real-world industry environments.",

"Premium Global Experience Programs":
"Curated programs combining internships, travel, and cultural immersion for international exposure.",

"International Student Placement Pathways":
"Facilitation of student placements into Australian universities through institutional partnerships.",

"Cultural Exchange Programs":
"Overseas cultural learning experiences for students focusing on global exposure.",

"Sponsorship & Institutional Partnerships":
"Collaboration with organisations aligned with youth, culture, and global mobility."
}

for title, desc in pathways.items():
    st.markdown(f"### {title}")
    st.markdown(f'<div class="box">{desc}</div>', unsafe_allow_html=True)

st.divider()

# ---------- FOOTER CTA ----------
st.markdown("## 🚀 Strategic Vision")
st.info("Building a scalable global ecosystem that connects youth, culture, education, and industry into one integrated growth platform.")
