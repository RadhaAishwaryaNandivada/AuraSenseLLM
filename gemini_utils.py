from transformers import pipeline

# Text generation model (LLM)
text_generator = pipeline(
    "text-generation",
    model="google/gemma-2b-it",
    max_new_tokens=300
)

# Image captioning model
image_captioner = pipeline(
    "image-to-text",
    model="Salesforce/blip-image-captioning-base"
)

BASE_PROMPT = """
You are a creative AI assistant.

Tasks:
1. First line must be: Mood: <one word>
2. Write a short aesthetic story (3–4 lines)
3. Give bullet-point suggestions:
   - Outfit style
   - Color palette
   - Photography pose ideas
   - Nature or cosmic theme
"""

def analyze_aura(content):
    context = ""

    for item in content:
        # Image input
        if hasattr(item, "size"):
            caption = image_captioner(item)[0]["generated_text"]
            context += f"Image description: {caption}. "
        else:
            context += str(item) + " "

    prompt = BASE_PROMPT + "\nContext:\n" + context

    result = text_generator(prompt)[0]["generated_text"]
    return result
