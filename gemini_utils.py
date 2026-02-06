import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

MODEL = genai.GenerativeModel("gemini-2.5-flash")

BASE_PROMPT = """
You are an imaginative AI storyteller with strong aesthetic intelligence.

From the given input:

1. Start with:
   Mood: <one single word>
   (If the vibe feels dreamy, vast, mysterious, or timeless, use cosmic or mystic.)

2. Write a short engaging story (3–4 lines).
   The story can be:
   - romantic
   - cinematic
   - funny
   - aesthetic
   - cosmic / space-inspired

3. Then present suggestions in clear bullet points:

✨ Outfit Style  
✨ Accessories / Jewellery  
✨ Color Palette  
✨ Flowers / Natural Elements  
✨ Nature or Cosmic Scene  
✨ Tourist or Stargazing Place  
✨ Perfume / Fragrance Family  
✨ Music Mood / Genre  

4. Add a photography section:

📸 Photography Style  
📸 Pose Ideas (2–3 simple poses)  
📸 Composition Tips (lighting, angle, framing)

Rules:
- Keep it beautiful, creative, and inspiring
- Avoid technical jargon
- Do NOT give advice, diagnosis, or predictions
"""


def analyze_aura(content):
    response = MODEL.generate_content([BASE_PROMPT] + content)
    return response.text
