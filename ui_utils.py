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
    overlays = {
        "calm": "rgba(227,242,253,0.45)",
        "romantic": "rgba(252,228,236,0.45)",
        "energetic": "rgba(255,248,225,0.45)",
        "elegant": "rgba(236,239,241,0.45)",
        "nature": "rgba(232,245,233,0.45)",
        "fresh": "rgba(224,247,250,0.45)",
        "cosmic": "rgba(44,83,100,0.35)",
        "mystic": "rgba(146,141,171,0.35)"
    }

    overlay = overlays.get(mood.lower(), "rgba(255,255,255,0.35)")

    st.markdown(
        f"""
        <style>
        .stApp {{
            background:
                linear-gradient(180deg, #ffffff, #ffffff),
                linear-gradient(180deg, {overlay}, rgba(255,255,255,0.95));
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
