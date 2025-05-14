import streamlit as st
import os
from generate_ai import generate_ideas
import re

# Streamlit UI
st.title("🎬 Hayyu AI Content Generator")

niche = st.text_input("Enter your niche (e.g., fitness, tech, cooking):")
audience = st.text_input("Target audience (e.g., teens, moms, students):")
past_topics = st.text_area("Mention a few past topics you’ve posted about:")

# format output
def format_ideas(raw_text):
    ideas = re.split(r'\n\d+\. ', "\n" + raw_text.strip())  # Split on numbered list
    formatted = []
    for idea in ideas:
        if idea.strip():
            formatted.append(f"🔹 {idea.strip()}")
    return "\n\n".join(formatted)


if st.button("Generate"):
    if niche and audience:
        with st.spinner("Generating..."):
            raw_output = generate_ideas(niche, audience, past_topics)
            formatted_output = format_ideas(raw_output)
            st.markdown("## 🔥 Content Ideas:")
            st.markdown(formatted_output)
    else:
        st.warning("Please fill in the required fields.")
# Add a footer
st.markdown(
    """
    ---
    Made by [Hayyu-ai](https://hayyu.ai)
    [![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?style=flat&logo=github)](https://github.com/hayyu-ai)
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat&logo=linkedin)](https://www.linkedin.com/company/hayyu-ai)
    [![YouTube](https://img.shields.io/badge/YouTube-Channel-red?style=flat&logo=youtube)](https://www.youtube.com/@hayyuai)
    [![Instagram](https://img.shields.io/badge/Instagram-Profile-pink?style=flat&logo=instagram)](https://www.instagram.com/hayyu.ai/)
    [![Facebook](https://img.shields.io/badge/Facebook-Page-blue?style=flat&logo=facebook)](https://www.facebook.com/hayyu.ai)          
    
    Disclaimer: This tool is for Motivational purposes only. Please use responsibly.
  
    ---
    **Note:** This is a demo version. For more features, visit [Hayyu.ai](https://hayyu.ai).
    """
)
