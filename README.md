# Gold-Analysis-Agent

Gold Analysis Agent is an AI-powered application that provides insights into the gold market by combining real-time market data, financial news, and Large Language Models (LLMs). The system retrieves gold price information from Alpha Vantage, gathers relevant economic and market news, and generates natural-language analysis to help users understand current market conditions and trends.

### Features

* Real-time gold market data retrieval
* Historical gold price visualization
* Financial news aggregation and analysis
* AI-generated market insights and outlook
* English and Persian language support
* Conversation history storage
* Interactive Streamlit-based user interface

### Project Architecture

The application consists of four main components:

1. **Market Data Module** – Retrieves gold prices and historical data from Alpha Vantage.
2. **News Module** – Collects and summarizes gold-related news.
3. **LLM Engine** – Uses a Large Language Model (Gemini or Ollama) to analyze market conditions and generate responses.
4. **Streamlit Interface** – Provides a user-friendly chat interface, price charts, and conversation history.

### Installation

1. Clone the repository.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure API keys in the `.env` file (e.g., Alpha Vantage).

### Running the Application

Start the Streamlit interface:

```bash
streamlit run streamlit_app.py
```

Then open the local URL displayed in the terminal (typically `http://localhost:8501`).

### Example Questions

* What is the current gold price?
* What is the outlook for gold this week?
* How do interest rates affect gold prices?
* What recent news is impacting the gold market?

This project was developed as an educational AI agent for gold market analysis and does not provide financial advice.

