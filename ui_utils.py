import streamlit as st

MOOD_EMOJI = {
    "calm": "😌",
    "romantic": "💖",
    "energetic": "⚡",
    "nature": "🌿",
    "cosmic": "🌌",
    "mystic": "🪐"
}

MOOD_BACKGROUNDS = {
    "calm": "linear-gradient(180deg, #e3f2fd, #ffffff)",
    "romantic": "linear-gradient(180deg, #fde7f3, #ffffff)",
    "energetic": "linear-gradient(180deg, #fff8e1, #ffffff)",
    "nature": "linear-gradient(180deg, #e8f5e9, #ffffff)",
    "cosmic": "linear-gradient(180deg, #ede7f6, #ffffff)",
    "mystic": "linear-gradient(180deg, #f3e5f5, #ffffff)"
}

def get_mood_emoji(mood: str) -> str:
    return MOOD_EMOJI.get(mood.lower(), "🌈")

def set_background(mood: str):
    bg = MOOD_BACKGROUNDS.get(mood.lower(), "linear-gradient(180deg, #f7f9fc, #ffffff)")
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: {bg};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
