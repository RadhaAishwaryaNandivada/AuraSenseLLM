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

# ---------------- GLOBAL SAFE STYLES ----------------
st.markdown(
    """
    <style>
    /* Keep background aesthetic, but isolate content */
    body {
        background-color: transparent;
    }

    /* CARD BASE (this is the key fix) */
    .card {
        background: #ffffff;
        color: #111111;
        padding: 24px;
        border-radius: 22px;
        box-shadow: 0 16px 40px rgba(0,0,0,0.12);
        margin-bottom: 24px;
    }

    /* Ensure inputs always readable */
    textarea, input {
        background-color: #ffffff !important;
        color: #111111 !important;
        border-radius: 14px !important;
    }

    /* Image alignment */
    .image-wrapper {
        max-width: 520px;
        margin: 24px auto;
        text-align: center;
    }

    /* Output card */
    .output-card {
        background: #ffffff;
        color: #111111;
        padding: 22px;
        border-radius: 20px;
        box-shadow: 0 14px 36px rgba(0,0,0,0.12);
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- HEADER ----------------
st.title("✨ AuraSense")
st.caption("Aesthetic storytelling powered by AI & imagination")

st.divider()

# ---------------- INPUT SECTION (SOLID CARD) ----------------
st.subheader("✨ Share a Moment")

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    text_input = st.text_area(
        "💭 Describe the moment",
        placeholder="A calm night sky filled with stars above a silent road...",
        height=110
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

        # Image (clean, centered, fixed width)
        if uploaded_image:
            image = Image.open(uploaded_image)

            st.markdown('<div class="image-wrapper">', unsafe_allow_html=True)
            st.image(image, width=520)
            st.markdown('</div>', unsafe_allow_html=True)

            content.append(image)

        # Text
        if text_input:
            content.append(text_input)

        # Optional link
        if url_input:
            content.append(extract_text_from_url(url_input))

        with st.spinner("Sensing the aura..."):
            output = analyze_aura(content)

        # Extract mood
        mood = "unknown"
        if "Mood:" in output:
            mood = output.split("Mood:")[1].split("\n")[0].strip()

        # Apply transparent mood background (now SAFE)
        set_background(mood)
        emoji = get_mood_emoji(mood)

        # Output inside solid card
        st.markdown(
            f"""
            <div class="output-card">
            <h3>{emoji} Aura Story & Vibe Match</h3>
            {output}
            </div>
            """,
            unsafe_allow_html=True
        )
