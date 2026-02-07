import streamlit as st
from PIL import Image

from gemini_utils import analyze_aura
from input_utils import extract_text_from_url
from ui_utils import set_background, get_mood_emoji

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AuraSense",
    page_icon="✨",
    layout="centered"
)

# ---------------- FINAL SAFE CSS (DO NOT TOUCH AFTER THIS) ----------------
st.markdown(
    """
    <style>
    /* ===== GLOBAL BASE ===== */
    html, body, .stApp {
        background-color: #ffffff !important;
        color: #111111 !important;
    }

    /* ===== CARDS ===== */
    .card {
        background: rgba(255,255,255,0.97);
        color: #111111;
        padding: 26px;
        border-radius: 22px;
        box-shadow: 0 18px 42px rgba(0,0,0,0.12);
        margin-bottom: 26px;
    }

    .output-card {
        background: rgba(255,255,255,0.97);
        color: #111111;
        padding: 24px;
        border-radius: 20px;
        box-shadow: 0 16px 38px rgba(0,0,0,0.12);
        line-height: 1.7;
    }

    /* ===== TEXT INPUT FIXES ===== */
    textarea, input {
        background-color: #ffffff !important;
        color: #111111 !important;
        border-radius: 14px !important;
        border: 1px solid #d0d0d0 !important;
    }

    textarea::placeholder,
    input::placeholder {
        color: #777777 !important;
        opacity: 1 !important;
    }

    textarea:focus,
    input:focus {
        outline: none !important;
        border: 1px solid #7aa7ff !important;
        box-shadow: 0 0 0 2px rgba(122,167,255,0.25) !important;
    }

    /* ===== FILE UPLOADER FIX ===== */
    section[data-testid="stFileUploader"] {
        background-color: #f7f7f7 !important;
        border-radius: 16px;
        padding: 12px;
    }

    /* ===== BUTTON FIX ===== */
    button[kind="primary"] {
        background-color: #111111 !important;
        color: #ffffff !important;
        border-radius: 16px !important;
        padding: 10px 22px !important;
    }

    button[kind="primary"]:hover {
        background-color: #000000 !important;
    }

    /* ===== IMAGE ===== */
    .image-wrapper {
        max-width: 520px;
        margin: 28px auto;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- HEADER ----------------
st.title("✨ AuraSense")
st.caption("Aesthetic storytelling powered by AI & imagination")

st.divider()

# ---------------- INPUT SECTION ----------------
st.subheader("✨ Share a Moment")

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    text_input = st.text_area(
        "💭 Describe the moment",
        placeholder="A calm night sky filled with stars above a silent road...",
        height=120
    )

    uploaded_image = st.file_uploader(
        "📸 Add an image (optional)",
        type=["jpg", "jpeg", "png"]
    )

    url_input = st.text_input(
        "🔗 Paste a link (optional)"
    )

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- PROCESS ----------------
if st.button("✨ Sense the Aura"):
    if not any([text_input, uploaded_image]):
        st.warning("Please enter text or upload an image (at least one).")
    else:
        content = []

        if uploaded_image:
            image = Image.open(uploaded_image)
            st.markdown('<div class="image-wrapper">', unsafe_allow_html=True)
            st.image(image, width=520)
            st.markdown('</div>', unsafe_allow_html=True)
            content.append(image)

        if text_input:
            content.append(text_input)

        if url_input:
            content.append(extract_text_from_url(url_input))

        with st.spinner("Sensing the aura..."):
            output = analyze_aura(content)

        mood = "unknown"
        if "Mood:" in output:
            mood = output.split("Mood:")[1].split("\n")[0].strip()

        set_background(mood)
        emoji = get_mood_emoji(mood)

        st.markdown(
            f"""
            <div class="output-card">
            <h3>{emoji} Aura Story & Vibe Match</h3>
            {output}
            </div>
            """,
            unsafe_allow_html=True
        )
