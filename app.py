
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Happy Teachers' Day • Sakshi Ma'am",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="collapsed",
)

PHOTO = Path(__file__).parent / "assets" / "sakshi_mam.png"

# -------------------- Styling --------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

.stApp {
    background:
      radial-gradient(circle at 15% 15%, rgba(255, 182, 193, .25), transparent 25%),
      radial-gradient(circle at 85% 20%, rgba(255, 218, 185, .28), transparent 25%),
      linear-gradient(135deg, #fff8fb 0%, #fffaf2 48%, #f8f3ff 100%);
    color: #3b2940;
}

.block-container {
    max-width: 850px;
    padding-top: 2.2rem;
    padding-bottom: 3rem;
}

h1, h2, h3, p, div, span, button {
    font-family: 'DM Sans', sans-serif;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.5rem, 8vw, 5rem);
    line-height: 1.02;
    text-align: center;
    margin: 12px 0 12px;
    background: linear-gradient(90deg, #9b3f70, #e08b75, #8b5fbf);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align: center;
    font-size: 1.1rem;
    color: #765b70;
    margin-bottom: 22px;
}

.small-label {
    text-align:center;
    letter-spacing: 3px;
    text-transform: uppercase;
    font-size: .78rem;
    color:#a05b83;
    font-weight:700;
}

.card {
    background: rgba(255,255,255,.72);
    border: 1px solid rgba(255,255,255,.9);
    box-shadow: 0 18px 50px rgba(107, 67, 103, .12);
    border-radius: 28px;
    padding: 28px;
    backdrop-filter: blur(12px);
    margin: 14px 0;
}

.quote {
    font-family: 'Playfair Display', serif;
    font-size: 1.55rem;
    line-height: 1.5;
    text-align:center;
    color:#55364f;
}

.center {
    text-align:center;
}

.photo-wrap {
    display:flex;
    justify-content:center;
    margin: 18px 0 8px;
}

.photo {
    width:min(220px, 58vw);
    aspect-ratio:1/1;
    object-fit:cover;
    border-radius:50%;
    border: 8px solid rgba(255,255,255,.95);
    box-shadow: 0 20px 55px rgba(113, 55, 92, .22);
    animation: float 4s ease-in-out infinite;
}

@keyframes float {
  0%,100% { transform: translateY(0) rotate(-1deg); }
  50% { transform: translateY(-10px) rotate(1deg); }
}

.reveal {
    animation: reveal .9s ease both;
}
@keyframes reveal {
    from { opacity:0; transform:translateY(24px) scale(.97); }
    to { opacity:1; transform:translateY(0) scale(1); }
}

.petals {
    text-align:center;
    font-size: 2rem;
    letter-spacing: 10px;
    animation: drift 3s ease-in-out infinite;
}
@keyframes drift {
  0%,100% { transform: translateY(0); opacity:.85; }
  50% { transform: translateY(-8px); opacity:1; }
}

.progress {
    text-align:center;
    color:#9a7892;
    font-size:.85rem;
    margin: 4px 0 20px;
}

.stButton > button {
    width:100%;
    border:0;
    border-radius:999px;
    padding: .8rem 1.2rem;
    font-weight:700;
    font-size:1rem;
    color:white;
    background: linear-gradient(90deg,#a84d7b,#d37a79,#8661b6);
    box-shadow: 0 10px 25px rgba(137, 73, 116, .20);
    transition: all .2s ease;
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 14px 30px rgba(137, 73, 116, .28);
}

.signature {
    font-family:'Playfair Display', serif;
    text-align:center;
    font-size:1.35rem;
    color:#7e4168;
    margin-top:20px;
}

.final {
    border: 1px solid rgba(191, 128, 169, .3);
    background: linear-gradient(135deg, rgba(255,255,255,.8), rgba(255,240,248,.75));
}

.heart {
    text-align:center;
    font-size:2.4rem;
    animation: heartbeat 1.6s infinite;
}
@keyframes heartbeat {
  0%, 100% { transform:scale(1); }
  20% { transform:scale(1.12); }
  35% { transform:scale(1); }
}
</style>
""", unsafe_allow_html=True)

# -------------------- State --------------------
if "page" not in st.session_state:
    st.session_state.page = 0

def next_page():
    st.session_state.page = min(st.session_state.page + 1, 3)

def back_page():
    st.session_state.page = max(st.session_state.page - 1, 0)

page = st.session_state.page

# -------------------- Page 1 --------------------
if page == 0:
    st.markdown('<div class="petals">🌸 ✨ 🌷 ✨ 🌸</div>', unsafe_allow_html=True)
    st.markdown('<div class="small-label">A little surprise from your students</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title">Happy Teachers’ Day</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">To our dearest <b>Sakshi Ma’am</b> — our coordinator, mentor &amp; guide</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card reveal">
      <div class="quote">
        “Some teachers teach a subject.<br>
        Some teachers leave a mark on your life.”
      </div>
      <p class="center" style="color:#80677a;margin-top:18px;">
        This little page is just a small way for the<br>
        <b>3rd Year B.Tech Biotechnology</b> class to say thank you. 💗
      </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("✨ Open Your Surprise", key="open"):
        next_page()
        st.rerun()

# -------------------- Page 2 --------------------
elif page == 1:
    st.markdown('<div class="progress">SURPRISE 1 OF 4</div>', unsafe_allow_html=True)
    st.markdown('<div class="small-label">Meet the person behind our class</div>', unsafe_allow_html=True)

    st.markdown('<div class="photo-wrap reveal">', unsafe_allow_html=True)
    if PHOTO.is_file():
        from PIL import Image
        image = Image.open(PHOTO).convert("RGB")
        st.image(image, width=220)
    else:
        st.error("Ma'am's photo was not found. Keep assets/sakshi_mam.png in the GitHub repository.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card reveal">
      <h2 class="center" style="color:#7c4168;">Our Dearest Sakshi Ma’am 🌷</h2>
      <p class="center" style="line-height:1.75;color:#705a6b;">
        Being a class coordinator is not just about schedules, notices and responsibilities.
        It is also about being there when students need direction, clarity or simply someone
        who understands.
      </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("💌 Next", key="next1"):
        next_page()
        st.rerun()

# -------------------- Page 3 --------------------
elif page == 2:
    st.markdown('<div class="progress">SURPRISE 2 OF 4</div>', unsafe_allow_html=True)
    st.markdown('<div class="small-label">A few words from your class</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card reveal">
      <div class="quote">
        “Thank you for guiding us when things get confusing,
        keeping us together when things get hectic,
        and reminding us to keep moving forward.”
      </div>
    </div>
    <div class="card reveal">
      <p>🌱 <b>You help us grow</b> — not only as students, but as people.</p>
      <p>🧬 <b>You keep us connected</b> — even when our class gets a little chaotic.</p>
      <p>💡 <b>You give us direction</b> — especially when we are unsure about the next step.</p>
      <p>🌸 <b>You make the journey memorable</b> — and that matters more than any single lecture.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🌷 One More Surprise", key="next2"):
        next_page()
        st.rerun()

# -------------------- Page 4 --------------------
else:
    st.markdown('<div class="progress">FINAL SURPRISE • 4 OF 4</div>', unsafe_allow_html=True)
    st.markdown('<div class="small-label">From the entire class</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card final reveal">
      <div class="heart">❤️</div>
      <div class="hero-title" style="font-size:clamp(2.2rem,7vw,4rem);">
        Thank You, Ma’am
      </div>
      <div class="quote">
        “A good coordinator manages a class.<br>
        A great one becomes a part of its journey.”
      </div>
      <p class="center" style="line-height:1.8;color:#705a6b;margin-top:22px;">
        We may forget a few deadlines, assignments and lectures,
        but we will remember the people who made our college journey
        a little easier, warmer and better.
      </p>
      <p class="signature">With lots of respect &amp; warm wishes 🌸<br>
      — 3rd Year B.Tech Biotechnology</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔄 See It Again", key="again"):
        st.session_state.page = 0
        st.rerun()

st.markdown(
    '<p class="center" style="margin-top:28px;color:#aa8ca4;font-size:.8rem;">Made with ❤️ by the 3rd Year B.Tech Biotechnology class</p>',
    unsafe_allow_html=True
)
