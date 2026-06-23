import streamlit as st

st.title("Gold Analysis Agent")

question = st.text_input(
    "Ask a question about gold:"
)

if question:
    st.write(f"You asked: {question}")