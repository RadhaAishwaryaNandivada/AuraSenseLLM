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
    "calm": "linear-gradient(180deg, #eaf4ff, #ffffff)",
    "romantic": "linear-gradient(180deg, #ffe6f0, #ffffff)",
    "passionate": "linear-gradient(180deg, #ffe5e5, #ffffff)",
    "energetic": "linear-gradient(180deg, #fff4d6, #ffffff)",
    "nature": "linear-gradient(180deg, #e9f7ef, #ffffff)",
    "cosmic": "linear-gradient(180deg, #efe9ff, #ffffff)",
    "mystic": "linear-gradient(180deg, #f3e8ff, #ffffff)"
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
