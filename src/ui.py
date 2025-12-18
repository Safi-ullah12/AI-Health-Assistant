import streamlit as st
from streamlit_chat import message
from langchain.schema import HumanMessage, AIMessage
from chat_utils import handle_userinput

def render_chat_ui():
    st.subheader("💬 Chat with the Healthcare Bot")
    if "conversation" not in st.session_state:
        st.info("Process your CSV files first.")
        return
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    for idx, turn in enumerate(st.session_state.chat_history):
        if isinstance(turn, HumanMessage):
            message(turn.content, is_user=True, key=f"user_{idx}")
        elif isinstance(turn, AIMessage):
            message(turn.content, key=f"ai_{idx}")
        else:
            message(str(turn), key=f"plain_{idx}")
    st.text_input("💡 Enter your symptoms (e.g., I have itching and skin rash)  or ask a question based on medical conditions in our knowledge base...", key="input_box", label_visibility="collapsed", on_change=handle_userinput)
