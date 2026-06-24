import streamlit as st

from src.agent import GoldAnalysisAgent
from src.chat_history import load_history, save_history
import pandas as pd

from src.market_data import get_gold_history #for visualization
import plotly.express as px

agent = GoldAnalysisAgent()

st.set_page_config(
    page_title="Gold Analysis Agent",
    page_icon="🥇",
    layout="wide"
)

st.title("🥇 Gold Analysis Agent")

# Display Gold Price Chart.
history = get_gold_history()

df = pd.DataFrame(
    {
        "Date": history["dates"],
        "Gold Price": history["prices"]
    }
)

st.subheader("Gold Price - Last 30 Days")

fig = px.line(
    df,
    x="Date",
    y="Gold Price",
    title="Gold Price Trend (Last 30 Days)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# Load history once when app starts
if "messages" not in st.session_state:
    st.session_state.messages = load_history()  # loads previous conversations.

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask about gold..."):

    # Add user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Save after user message
    save_history(st.session_state.messages)

    # Show user message immediately
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate answer
    with st.spinner("Analyzing..."):

        answer = agent.ask(prompt) #for Gemini analysis

    # Show assistant response
    with st.chat_message("assistant"):
        st.markdown(answer)

    # Add assistant message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    # Save after assistant response
    save_history(st.session_state.messages)

    st.rerun()

# Sidebar
with st.sidebar:

    st.header("Options")

    if st.button("Clear Chat History"):

        st.session_state.messages = []

        save_history([])

        st.rerun()