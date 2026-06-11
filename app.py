PASSWORD = "tumaurhum"
import os
import random
import streamlit as st
from datetime import date
from memories import MEMORIES

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="LOVE Terminal",
    page_icon="❤️",
    layout="centered"
)
st.markdown("""
<style>

/* Netflix-style dark background */
body {
    background: radial-gradient(circle at top, #111 0%, #000 100%);
}

/* Main title animation */
@keyframes fadeIn {
    0% {opacity: 0; transform: translateY(-20px);}
    100% {opacity: 1; transform: translateY(0);}
}

.netflix-title {
    font-size: 48px;
    font-weight: 800;
    color: #e50914;
    text-align: center;
    animation: fadeIn 1.2s ease-in-out;
    letter-spacing: 2px;
}

/* Subtext glow */
.glow-text {
    text-align: center;
    color: #aaa;
    font-size: 16px;
    animation: fadeIn 2s ease-in-out;
}

/* Login box */
.login-box {
    background: rgba(20,20,20,0.8);
    padding: 30px;
    border-radius: 12px;
    border: 1px solid #333;
    width: 300px;
    margin: auto;
    box-shadow: 0 0 20px rgba(229,9,20,0.3);
    animation: fadeIn 1.5s ease-in-out;
}

/* Button glow */
.stButton>button {
    background-color: #e50914;
    color: white;
    border-radius: 6px;
    border: none;
    width: 100%;
    padding: 10px;
}

.stButton>button:hover {
    box-shadow: 0 0 15px #e50914;
    transform: scale(1.02);
}

</style>
""", unsafe_allow_html=True)
import streamlit as st

# --------------------------
# PASSWORD GATE
# --------------------------

import time
import streamlit as st

PASSWORD = "tumaurhum"

if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:

    st.markdown('<div class="netflix-title">LOVE TERMINAL</div>', unsafe_allow_html=True)
    st.markdown('<div class="glow-text">Initializing secure emotional connection...</div>', unsafe_allow_html=True)

    time.sleep(0.5)

    with st.container():
        st.markdown('<div class="login-box">', unsafe_allow_html=True)

        pwd = st.text_input("Enter Access Code", type="password")

        if st.button("Unlock"):
            if pwd == PASSWORD:
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Access Denied")

        st.markdown('</div>', unsafe_allow_html=True)

    st.stop()

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #0d1117;
}

.big-ticker {
    font-size: 42px;
    font-weight: bold;
    color: #00ff88;
}

.metric-box {
    border: 1px solid #333;
    border-radius: 10px;
    padding: 10px;
}

img {
    border-radius: 18px !important;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# DYNAMIC DATA
# ==========================================

from datetime import datetime
from dateutil.relativedelta import relativedelta

relationship_start = datetime(
    2018, 11, 3, 0, 30
)

first_talk = datetime(
    2014, 4, 29, 0, 0
)

now = datetime.now()

relationship_delta = relativedelta(
    now,
    relationship_start
)

talk_delta = relativedelta(
    now,
    first_talk
)

photo_folder = "photos"

images = sorted(
    [
        file
        for file in os.listdir(photo_folder)
        if file.lower().endswith(
            (".jpg", ".jpeg", ".png")
        )
    ],
    key=lambda x: int(
        os.path.splitext(x)[0].replace("pic", "")
    )
)

relationship_score = min(
    100,
    85 + len(images) // 2
)

rating = "AAA ❤️"

NEWS_HEADLINES = [

    "Girlfriend remains highest-performing asset in portfolio.",

    "Relationship Index closes at all-time highs.",

    "Analysts upgrade Aanchal Holdings to STRONG BUY.",

    "Pasta Date Night exceeds expectations.",

    "Emotional liquidity remains abundant.",

    "Management guidance remains unchanged: Forever.",

    "Boyfriend spotted smiling at phone again.",

    "Long-term outlook remains exceptionally bullish."
]

# ==========================================
# HEADER
# ==========================================

st.markdown(
    '<p class="big-ticker">$LOVE ▲ 4.23%</p>',
    unsafe_allow_html=True
)

st.caption(
    "Relationship Exchange • S&A Markets"
)

# ==========================================
# MARKET STATUS
# ==========================================

# ==========================================
# TERMINAL OVERVIEW
# ==========================================

st.info(f"""
MARKET STATUS: OPEN

Ticker: $LOVE
Exchange: S&A

Primary Listing:
03-Nov-2018 00:30

Coverage Initiated:
29-Apr-2014

Credit Rating:
{rating}
""")

st.divider()

st.subheader("📊 SECURITY OVERVIEW")

st.metric(
    "Relationship Runtime",
    f"{relationship_delta.years}Y "
    f"{relationship_delta.months}M "
    f"{relationship_delta.days}D"
)

st.caption(
    f"{relationship_delta.hours}H "
    f"{relationship_delta.minutes}M "
    f"{relationship_delta.seconds}S"
)

st.metric(
    "First Contact Runtime",
    f"{talk_delta.years}Y "
    f"{talk_delta.months}M "
    f"{talk_delta.days}D"
)

st.caption(
    f"{talk_delta.hours}H "
    f"{talk_delta.minutes}M "
    f"{talk_delta.seconds}S"
)

c1, c2 = st.columns(2)

with c1:
    st.metric(
        "Memories Archived",
        len(images)
    )

with c2:
    st.metric(
        "Relationship Index",
        relationship_score
    )

# ==========================================
# NEWSWIRE
# ==========================================

st.divider()

st.subheader("📰 RELATIONSHIP NEWSWIRE")

st.warning(
    random.choice(
        NEWS_HEADLINES
    )
)

# ==========================================
# ANALYST COVERAGE
# ==========================================

st.divider()

st.subheader(
    "📊 ANALYST COVERAGE"
)

st.success(f"""
Rating: {rating}

Target Price:
∞

Investment Thesis:

• Strong long-term fundamentals

• Consistent emotional returns

• Exceptional management quality

• High growth visibility

Recommendation:
STRONG BUY
""")

# ==========================================
# RELATIONSHIP INDEX
# ==========================================

st.divider()

st.subheader(
    "📈 RELATIONSHIP INDEX"
)

st.progress(
    relationship_score
)

st.caption(
    f"Current Score: {relationship_score}/100"
)

# ==========================================
# MEMORY ARCHIVE
# ==========================================

st.divider()

with st.expander(
    f"🎞 MEMORY ARCHIVE ({len(images)})",
    expanded=False
):

    if "memory_index" not in st.session_state:
        st.session_state.memory_index = 0

    current_file = images[
        st.session_state.memory_index
    ]

    image_path = os.path.join(
        photo_folder,
        current_file
    )

    base_name = os.path.splitext(
        current_file
    )[0]

    caption = MEMORIES.get(
        base_name,
        "A beautiful memory ❤️"
    )

    st.image(
        image_path,
        use_container_width=True
    )

    st.markdown(
        f"""
### MEMORY RECORD

**Asset ID:** {base_name.upper()}

**Commentary:** {caption}
"""
    )

    st.caption(
        f"Record {st.session_state.memory_index + 1} of {len(images)}"
    )

    left, center, right = st.columns(
        [1, 1, 1]
    )

    with left:

        if st.button(
            "⬅️",
            use_container_width=True
        ):

            if st.session_state.memory_index > 0:

                st.session_state.memory_index -= 1
                st.rerun()

    with center:

        st.markdown(
            "<h3 style='text-align:center'>❤️</h3>",
            unsafe_allow_html=True
        )

    with right:

        if st.button(
            "➡️",
            use_container_width=True
        ):

            if (
                st.session_state.memory_index
                < len(images) - 1
            ):

                st.session_state.memory_index += 1
                st.rerun()

# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    f"""
Terminal Version 2.0

Last Updated:
{date.today()}

For Internal Use Only
"""
)