from src.agent import GoldAnalysisAgent


agent = GoldAnalysisAgent()

while True:

    question = input("\nUser: ")

    if question.lower() in ["exit", "quit"]:
        break

    answer = agent.ask(question)

    print("\nAgent:", answer)