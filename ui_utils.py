import streamlit as st

MOOD_EMOJI = {
    "calm": "😌",
    "romantic": "💖",
    "energetic": "⚡",
    "elegant": "✨",
    "nature": "🌿",
    "fresh": "🍃",
    "cosmic": "🌌",
    "mystic": "🪐"
}

def get_mood_emoji(mood):
    return MOOD_EMOJI.get(mood.lower(), "🌈")

def set_background(mood):
    cosmic_gradients = {
        "cosmic": "linear-gradient(180deg, #0f2027, #203a43, #2c5364)",
        "mystic": "linear-gradient(180deg, #1f1c2c, #928dab)",
        "calm": "linear-gradient(180deg, #e3f2fd, #ffffff)",
        "romantic": "linear-gradient(180deg, #fdeff9, #ec38bc)",
        "energetic": "linear-gradient(180deg, #fffbd5, #f15f79)",
        "nature": "linear-gradient(180deg, #d4fc79, #96e6a1)"
    }

    gradient = cosmic_gradients.get(mood.lower(), "linear-gradient(180deg,#ffffff,#f7f7f7)")

    st.markdown(
        f"""
        <style>
        .stApp {{
            background: {gradient};
            color: #111111;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
