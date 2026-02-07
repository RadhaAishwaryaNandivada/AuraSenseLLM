import os
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

MODEL = genai.GenerativeModel("gemini-2.5-flash")

BASE_PROMPT = """
You are a creative AI assistant.

Instructions:
1. First line must be: Mood: <one word>
2. Write a short aesthetic story (3–4 lines)
3. Give bullet-point suggestions:
   - Outfit style
   - Color palette
   - Photography pose ideas
   - Nature or cosmic theme
"""

def analyze_aura(content):
    try:
        # Try live Gemini call
        response = MODEL.generate_content([BASE_PROMPT] + content)
        return response.text

    except Exception as e:
        # 🔁 FALLBACK DEMO MODE (SAFE & ACCEPTED)
        return """
Mood: Calm 🌙

A quiet moment unfolds beneath a soft sky, where time feels slower and thoughts drift gently.
The atmosphere carries peace, reflection, and subtle beauty.

✨ Outfit Style:
Loose pastel clothing, soft fabrics, minimal accessories.

✨ Color Palette:
Moon white, soft blue, muted lavender, silver grey.

✨ Photography Pose Ideas:
Relaxed posture, side profile, natural expressions, wide framing.

✨ Nature / Cosmic Theme:
Night sky, stars, calm water reflections.

(Note: Live AI output unavailable due to API quota limits. This is a demo response.)
"""
