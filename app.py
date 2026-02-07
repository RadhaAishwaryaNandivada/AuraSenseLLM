import streamlit as st
from PIL import Image

from gemini_utils import analyze_aura
from input_utils import extract_text_from_url
from ui_utils import get_mood_emoji

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AuraSense",
    page_icon="✨",
    layout="centered"
)

# ---------------- HEADER ----------------
st.title("✨ AuraSense")
st.caption("Aesthetic storytelling powered by AI & imagination")

st.divider()

# ---------------- INPUT SECTION ----------------
st.subheader("✨ Share a Moment")

with st.container():
    st.markdown(
        """
        <div style="
            background: linear-gradient(180deg, #ffffff, #f7f9fc);
            padding: 24px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        ">
        """,
        unsafe_allow_html=True
    )

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

# ---------------- PROCESS ----------------
if st.button("✨ Sense the Aura"):
    if not any([text_input, uploaded_image]):
        st.warning("Please enter text or upload an image.")
    else:
        content = []

        if uploaded_image:
            image = Image.open(uploaded_image)
            st.image(image, width=480)
            content.append(image)

        if text_input:
            content.append(text_input)

        if url_input:
            content.append(extract_text_from_url(url_input))

        with st.spinner("Sensing the aura..."):
            output = analyze_aura(content)

        # Extract mood
        mood = "unknown"
        if "Mood:" in output:
            mood = output.split("Mood:")[1].split("\n")[0].strip()

        emoji = get_mood_emoji(mood)

        # Mood-based soft section (THIS is the fix)
        mood_colors = {
            "calm": "#e3f2fd",
            "romantic": "#fde7f3",
            "energetic": "#fff8e1",
            "nature": "#e8f5e9",
            "cosmic": "#ede7f6",
            "mystic": "#f3e5f5"
        }

        bg = mood_colors.get(mood.lower(), "#f7f9fc")

        st.markdown(
            f"""
            <div style="
                background: {bg};
                padding: 28px;
                border-radius: 22px;
                margin-top: 24px;
                box-shadow: 0 12px 32px rgba(0,0,0,0.08);
            ">
                <h3>{emoji} Aura Story & Vibe Match</h3>
                {output}
            </div>
            """,
            unsafe_allow_html=True
        )
