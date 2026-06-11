import os
import random
import time
import streamlit as st
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from memories import MEMORIES

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="LOVE Terminal",
    page_icon="❤️",
    layout="centered"
)

PASSWORD = "tumaurhum"

# =========================
# MOBILE-FIRST + CINEMATIC UI
# =========================
st.markdown("""
<style>

/* GLOBAL BACKGROUND */
.stApp {
    background: radial-gradient(circle at top, #0a0a0a, #000000);
    color: white;
}

/* REMOVE STREAMLIT CHROME */
header, footer {
    visibility: hidden;
}

/* MOBILE RESPONSIVE */
.block-container {
    padding: 1.2rem 1rem 2rem 1rem;
}

/* TITLE */
.title {
    font-size: 36px;
    font-weight: 900;
    text-align: center;
    color: #00ff88;
    text-shadow: 0 0 12px rgba(0,255,136,0.25);
    margin-bottom: 10px;
}

/* CARD SYSTEM */
.card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 14px;
    padding: 14px;
    margin: 12px 0;
    animation: fadeIn 0.8s ease-in-out;
}

/* FADE IN */
@keyframes fadeIn {
    0% {opacity: 0; transform: translateY(10px);}
    100% {opacity: 1; transform: translateY(0);}
}

/* METRICS MOBILE FIX */
[data-testid="stMetricValue"] {
    font-size: 22px;
    color: #00ff88;
}

/* NEWS BOX */
.news {
    padding: 12px;
    border-radius: 12px;
    background: rgba(229,9,20,0.08);
    border: 1px solid rgba(229,9,20,0.25);
}

/* BUTTONS */
.stButton>button {
    background: linear-gradient(90deg, #00ff88, #00c3ff);
    color: black;
    font-weight: bold;
    border-radius: 10px;
    border: none;
    width: 100%;
}

.stButton>button:hover {
    transform: scale(1.02);
    box-shadow: 0 0 12px rgba(0,255,136,0.4);
}

/* IMAGE STYLE */
img {
    border-radius: 14px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# AUTH SYSTEM
# =========================
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:

    st.markdown('<div class="title">❤️ LOVE TERMINAL</div>', unsafe_allow_html=True)
    st.caption("A private emotional system")

    pwd = st.text_input("Enter Access Code", type="password")

    if st.button("Unlock"):
        if pwd == PASSWORD:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Access Denied")

    st.stop()

# =========================
# DATA
# =========================
relationship_start = datetime(2018, 11, 3, 0, 30)
first_talk = datetime(2014, 4, 29, 0, 0)
now = datetime.now()

relationship_delta = relativedelta(now, relationship_start)
talk_delta = relativedelta(now, first_talk)

photo_folder = "photos"

images = sorted(
    [
        f for f in os.listdir(photo_folder)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ],
    key=lambda x: int(os.path.splitext(x)[0].replace("pic", ""))
)

relationship_score = min(100, 85 + len(images)//2)
rating = "AAA ❤️"

NEWS_HEADLINES = [
    "Girlfriend remains highest-performing asset in portfolio.",
    "Relationship Index closes at all-time highs.",
    "Pasta Date Night exceeds expectations.",
    "Emotional liquidity remains abundant.",
    "Long-term outlook remains exceptionally bullish."
]

# =========================
# AUTO RANDOM MEMORY (NEW FEATURE)
# =========================
random_image = random.choice(images)
random_image_path = os.path.join(photo_folder, random_image)
random_caption = MEMORIES.get(os.path.splitext(random_image)[0], "A beautiful memory ❤️")

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("💌 Memory Drop (Auto Generated)")
st.image(random_image_path, use_container_width=True)
st.write(random_caption)
st.markdown('</div>', unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown('<div class="title">💚 LOVE TERMINAL</div>', unsafe_allow_html=True)
st.caption("Relationship Exchange • Emotional Market Dashboard")

# =========================
# STATUS CARD
# =========================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.write(f"""
MARKET STATUS: OPEN  
Ticker: $LOVE  
Rating: {rating}
""")
st.markdown('</div>', unsafe_allow_html=True)

# =========================
# METRICS
# =========================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📊 Relationship Metrics")

st.metric("Relationship Runtime",
          f"{relationship_delta.years}Y {relationship_delta.months}M {relationship_delta.days}D")

st.metric("First Contact",
          f"{talk_delta.years}Y {talk_delta.months}D")

st.metric("Memories Archived", len(images))
st.metric("Relationship Index", relationship_score)

st.markdown('</div>', unsafe_allow_html=True)

# =========================
# NEWS
# =========================
st.markdown('<div class="card news">', unsafe_allow_html=True)
st.subheader("📰 Newswire")
st.write(random.choice(NEWS_HEADLINES))
st.markdown('</div>', unsafe_allow_html=True)

# =========================
# ANALYST
# =========================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📊 Analyst Coverage")
st.success("STRONG BUY • Target: ∞")
st.markdown('</div>', unsafe_allow_html=True)

# =========================
# INDEX
# =========================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📈 Relationship Index")
st.progress(relationship_score)
st.markdown('</div>', unsafe_allow_html=True)

# =========================
# MEMORY ARCHIVE
# =========================
st.divider()

with st.expander(f"🎞 Memory Archive ({len(images)})"):

    if "memory_index" not in st.session_state:
        st.session_state.memory_index = 0

    current_file = images[st.session_state.memory_index]
    path = os.path.join(photo_folder, current_file)
    base = os.path.splitext(current_file)[0]

    st.image(path, use_container_width=True)
    st.write(MEMORIES.get(base, "A beautiful memory ❤️"))

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("⬅️") and st.session_state.memory_index > 0:
            st.session_state.memory_index -= 1
            st.rerun()

    with col3:
        if st.button("➡️") and st.session_state.memory_index < len(images)-1:
            st.session_state.memory_index += 1
            st.rerun()

# =========================
# FOOTER
# =========================
st.divider()
st.caption(f"Terminal v2.0 • {date.today()} • Private Build")