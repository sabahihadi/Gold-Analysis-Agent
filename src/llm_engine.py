from openai import OpenAI
import os

from src.prompts import SYSTEM_PROMPT


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_response(user_question, market_data, news):

    prompt = f"""
    User Question:
    {user_question}

    Market Data:
    {market_data}

    News:
    {news}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.2,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content