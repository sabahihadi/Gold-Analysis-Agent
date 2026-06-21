import os
import json

import google.generativeai as genai
from dotenv import load_dotenv

from prompts import SYSTEM_PROMPT


# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found in environment variables."
    )

# Configure Gemini
genai.configure(api_key=api_key)

# Initialize model
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=SYSTEM_PROMPT
)


def generate_response(
    user_question: str,
    market_data: dict,
    news: list
) -> str:
    """
    Generate a response using Gemini based on:
    - User question
    - Market data
    - Latest news
    """

    try:

        prompt = f"""
User Question:
{user_question}

Market Data:
{json.dumps(market_data, indent=2, ensure_ascii=False)}

News:
{json.dumps(news, indent=2, ensure_ascii=False)}

Instructions:

1. Analyze the current gold price.
2. Summarize the most important news.
3. Explain how macroeconomic factors affect gold:
   - Interest rates
   - Inflation
   - US Dollar Index (DXY)
   - Geopolitical risks

4. Answer in the same language as the user's question.
5. Be concise and factual.
6. Mention uncertainty when appropriate.
7. Do not provide direct financial advice.
"""

        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                temperature=0.2,
                max_output_tokens=1000
            )
        )

        return response.text

    except Exception as e:

        return (
            f"Error generating response: {str(e)}"
        )