import os
import random
import streamlit as st
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from memories import MEMORIES
@st.cache_data
def load_images():
    photo_folder = "photos"
    images = [
        f for f in os.listdir(photo_folder)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ]
    images.sort()
    return images

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="LOVE TERMINAL",
    page_icon="❤️",
    layout="centered"
)

PASSWORD = "tumaurhum"

# =========================
# STYLE (MOBILE FIRST)
# =========================
st.markdown("""
<style>

.stApp {
    background: radial-gradient(circle at top, #0a0a0a, #000000);
    color: white;
}

header, footer {
    visibility: hidden;
}

.block-container {
    padding: 1rem 1rem 2rem 1rem;
}

/* MAIN HEADER */
.title {
    font-size: 40px;
    font-weight: 900;
    text-align: center;
    color: #00ff88;
    text-shadow: 0 0 12px rgba(0,255,136,0.3);
    margin-bottom: 10px;
}

/* CARD */
.card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 14px;
    padding: 14px;
    margin: 12px 0;
}

/* METRICS */
[data-testid="stMetricValue"] {
    color: #00ff88;
    font-size: 22px;
}

/* BUTTON */
.stButton>button {
    background: linear-gradient(90deg, #00ff88, #00c3ff);
    color: black;
    font-weight: bold;
    border-radius: 10px;
    width: 100%;
}

/* IMAGE */
img {
    border-radius: 14px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# AUTH
# =========================
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:

    st.markdown('<div class="title">❤️ LOVE TERMINAL</div>', unsafe_allow_html=True)
    st.caption("Private Emotional System")

    pwd = st.text_input("Access Code", type="password")

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

# photo_folder = "photos"

# images = sorted(
#     [f for f in os.listdir(photo_folder)
#      if f.lower().endswith((".jpg", ".jpeg", ".png"))],
#     key=lambda x: int(os.path.splitext(x)[0].replace("pic", ""))
# )
photo_folder = "photos"
images = load_images()


relationship_score = min(100, 85 + len(images)//2)
rating = "AAA ❤️"

NEWS_HEADLINES = [
    "Girlfriend remains highest-performing asset in portfolio.",
    "Relationship Index hits all-time highs.",
    "Emotional liquidity remains strong.",
    "Long-term outlook remains bullish."
]

# =========================
# FIX 1: STATIC HEADER (ALWAYS CORRECT)
# =========================
st.markdown('<div class="title">💚 LOVE TERMINAL</div>', unsafe_allow_html=True)

st.caption("Relationship Exchange • Emotional Dashboard")

# =========================
# FIX 2: STABLE RANDOM MEMORY (ONLY ON REFRESH)
# =========================
if "random_memory" not in st.session_state:
    st.session_state.random_memory = random.choice(images)

random_image = st.session_state.random_memory
random_path = os.path.join(photo_folder, random_image)
random_caption = MEMORIES.get(os.path.splitext(random_image)[0], "A beautiful memory ❤️")

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Memories with you💌")
st.image(random_path, use_container_width=True)
st.write(random_caption)
st.markdown('</div>', unsafe_allow_html=True)

# =========================
# STATUS
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
          f"{talk_delta.years}Y {talk_delta.months}M {talk_delta.days}D")

st.metric("Memories Archived", len(images))
st.metric("Relationship Index", relationship_score)

st.markdown('</div>', unsafe_allow_html=True)

# =========================
# NEWS
# =========================
st.markdown('<div class="card">', unsafe_allow_html=True)
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

    current = images[st.session_state.memory_index]
    path = os.path.join(photo_folder, current)
    base = os.path.splitext(current)[0]

    st.image(path, use_container_width=True)
    st.write(MEMORIES.get(base, "A beautiful memory ❤️"))

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("⬅️") and st.session_state.memory_index > 0:
            st.session_state.memory_index -= 1
            st.rerun()

    with col3:
        if st.button("➡️") and st.session_state.memory_index < len(images) - 1:
            st.session_state.memory_index += 1
            st.rerun()

# =========================
# FOOTER
# =========================
st.divider()
st.caption(f"LOVE Terminal • {date.today()} • Private Build")