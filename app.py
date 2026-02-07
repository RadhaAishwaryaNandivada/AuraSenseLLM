import streamlit as st
from PIL import Image

from gemini_utils import analyze_aura
from input_utils import extract_text_from_url
from ui_utils import set_background, get_mood_emoji

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="AuraSense",
    page_icon="✨",
    layout="centered"
)

# -------------------------------------------------
# BASE STYLES (SAFE, MINIMAL)
# -------------------------------------------------
st.markdown(
    """
    <style>
    .content-card {
        background: rgba(255,255,255,0.95);
        padding: 26px;
        border-radius: 22px;
        box-shadow: 0 12px 30px rgba(0,0,0,0.08);
        margin-bottom: 24px;
    }

    .output-card {
        background: rgba(255,255,255,0.95);
        padding: 28px;
        border-radius: 24px;
        box-shadow: 0 14px 34px rgba(0,0,0,0.10);
        line-height: 1.7;
    }

    .image-wrapper {
        max-width: 520px;
        margin: 24px auto;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.title("✨ AuraSense")
st.caption("Aesthetic storytelling powered by AI & imagination")
st.divider()

# -------------------------------------------------
# INPUT SECTION
# -------------------------------------------------
st.subheader("✨ Share a Moment")

with st.container():
    st.markdown('<div class="content-card">', unsafe_allow_html=True)

    text_input = st.text_area(
        "Describe the moment",
        placeholder="A calm night sky filled with stars above a silent road...",
        height=120
    )

    uploaded_image = st.file_uploader(
        "Add an image (optional)",
        type=["jpg", "jpeg", "png"]
    )

    url_input = st.text_input(
        "Paste a link (optional)"
    )

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# PROCESS
# -------------------------------------------------
if st.button("✨ Sense the Aura"):

    # ✅ ALWAYS define content first (fixes NameError)
    content = []

    if not any([text_input, uploaded_image]):
        st.warning("Please enter text or upload an image.")
    else:
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

        # Extract mood safely
        mood = "unknown"
        if "Mood:" in output:
            mood = output.split("Mood:")[1].split("\n")[0].strip()

        # 🔥 FULL PAGE BACKGROUND CHANGE (SOFT & SAFE)
        set_background(mood)
        emoji = get_mood_emoji(mood)

        # -------------------------------------------------
        # OUTPUT
        # -------------------------------------------------
        st.markdown(
            f"""
            <div class="output-card" style="color:#111111;">
                <h3 style="color:#000000;">{emoji} Aura Story & Vibe Match</h3>
                <div style="color:#111111; font-size:16px; line-height:1.7;">
                    {output}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
