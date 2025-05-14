import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variable
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Gemini prompt
def generate_ideas(niche, audience, past_topics):
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""
    Generate 5 engaging YouTube or TikTok content ideas for a creator in the "{niche}" niche.
    Audience: {audience}.
    Past topics include: {past_topics}.
    For each idea, include:
    - A catchy title
    - A short description
    - 2–3 relevant hashtags
    """

    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.title("🎬 Hayyu AI Content Generator")

niche = st.text_input("Enter your niche (e.g., fitness, tech, cooking):")
audience = st.text_input("Target audience (e.g., teens, moms, students):")
past_topics = st.text_area("Mention a few past topics you’ve posted about:")

if st.button("Generate"):
    if niche and audience:
        with st.spinner("Generating..."):
            output = generate_ideas(niche, audience, past_topics)
            st.markdown("### 🔥 Content Ideas:")
            st.markdown(output)
    else:
        st.warning("Please fill in the required fields.")
