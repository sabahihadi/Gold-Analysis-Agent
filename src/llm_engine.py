import os
import json
import time
import random

from dotenv import load_dotenv
from google import genai

from src.prompts import SYSTEM_PROMPT

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Missing GEMINI_API_KEY in .env")

client = genai.Client(api_key=API_KEY)


def generate_response(
    user_question: str,
    market_data: dict,
    news: list,
    language: str = "en",
    max_retries: int = 4
) -> str:
    """
    Generate a response using Gemini with retry logic.

    Retries transient errors using exponential backoff.
    """

    payload = {
        "question": user_question,
        "market_data": market_data,
        "news": news
    }

    if language == "fa":
        language_instruction = ("Answer ONLY in Persian.")
    else:
        language_instruction = ("Answer ONLY in English.")

    prompt = f"""
{SYSTEM_PROMPT}

{language_instruction}

You are given structured JSON data:

{json.dumps(payload, indent=2, ensure_ascii=False)}

Instructions:
1. Answer in the same language as the user's question.
2. If the user asks in English, answer ONLY in English.
3. Use the provided market data and news.
4. Explain your reasoning.
5. Discuss:
   - market trend
   - key drivers
   - risks
   - outlook
6. Never provide direct financial advice.
7. If data is insufficient, explicitly state the limitation.
8. Provide a complete answer of approximately 150-300 words.
9. Do not switch languages.
10. Mention uncertainty when needed
11. Be concise but informative

User Question:
{user_question}

Market data:
{market_data}

News:
{news}
"""

    last_error = None

    print("\n===== MARKET DATA =====")
    print(json.dumps(market_data, indent=2))

    print("\n===== NEWS =====")
    print(json.dumps(news, indent=2))

    print("\n===== QUESTION =====")
    print(user_question)

    for attempt in range(max_retries):

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=prompt,
                config={
                    "temperature": 0.3,
                    "max_output_tokens": 1200
                }
            )

            if hasattr(response, "text") and response.text:
                return response.text.strip()

            return "[Gemini Error] Empty response received."

        except Exception as e:

            last_error = e
            error_message = str(e)

            print(
                f"[Gemini Retry {attempt + 1}/{max_retries}] "
                f"{error_message}"
            )

            # Retry only for transient errors
            transient_errors = [
                "503",
                "UNAVAILABLE",
                "429",
                "RESOURCE_EXHAUSTED",
                "timeout",
                "connection",
                "getaddrinfo"
            ]

            should_retry = any(
                keyword.lower() in error_message.lower()
                for keyword in transient_errors
            )

            if not should_retry:
                break

            if attempt < max_retries - 1:

                # Exponential backoff with jitter
                sleep_time = (2 ** attempt) + random.uniform(0, 1)

                print(
                    f"Retrying in {sleep_time:.1f} seconds..."
                )

                time.sleep(sleep_time)

    return f"[Gemini Error] {last_error}"