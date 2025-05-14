import os
import google.generativeai as genai
from dotenv import load_dotenv
from pytrends.request import TrendReq

# Load environment variable
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Google Trends
pytrends = TrendReq(hl='en-US', tz=360)

def get_trending_keywords(niche):
    """
    Fetch trending keywords related to the niche using Google Trends.
    """
    try:
        # Get trending searches
        trending_searches = pytrends.trending_searches(pn='united_states')
        # Filter based on niche
        filtered_trends = [keyword for keyword in trending_searches if niche.lower() in keyword.lower()]
        return filtered_trends[:10]  # Return top 5 trends
    except Exception as e:
        print(f"Error fetching trends: {e}")
        return []

def generate_ideas(niche, audience, past_topics):
    trending = get_trending_keywords(niche)
    trends_text = ", ".join(trending) if trending else "N/A"

    prompt = f"""
    Generate 5 creative YouTube or TikTok video ideas in the niche "{niche}".
    Audience: {audience}
    Past topics: {past_topics}
    Trending keywords to incorporate: {trends_text}
    Each idea should include:
    - Catchy title
    - 1-line description
    - 2–3 relevant hashtags
    """

    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text
