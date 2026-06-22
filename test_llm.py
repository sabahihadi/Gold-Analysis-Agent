from src.llm_engine import generate_response

response = generate_response(
    user_question="What is the outlook for gold this week?",
    market_data={"price": 3350},
    news=[
        {
            "title": "Fed signals possible rate cuts",
            "content": "Markets expect lower rates."
        }
    ]
)

print(response)