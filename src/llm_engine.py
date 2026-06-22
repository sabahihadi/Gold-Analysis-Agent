import os
import json
from dotenv import load_dotenv
from google import genai

from src.prompts import SYSTEM_PROMPT

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Missing GEMINI_API_KEY in .env")

client = genai.Client(api_key=API_KEY)


def generate_response(user_question: str, market_data: dict, news: list) -> str:
    """
    Production-safe Gemini call with structured input
    """

    try:
        payload = {
            "question": user_question,
            "market_data": market_data,
            "news": news
        }

        prompt = f"""
{SYSTEM_PROMPT}

You are given structured JSON data:

{json.dumps(payload, indent=2, ensure_ascii=False)}

Rules:
- Use only provided data
- Be concise
- No financial advice
- Mention uncertainty when needed
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={
                "temperature": 0.2,
                "max_output_tokens": 800
            }
        )

        return response.text

    except Exception as e:
        return f"[Gemini Error] {str(e)}"