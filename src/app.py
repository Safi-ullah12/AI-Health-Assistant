import streamlit as st
from data_utils import read_csv_files, identify_files, merge_symptoms_precautions
from knowledge_base import create_chunks, build_knowledge_base, build_retriever
from chat_utils import get_conversation_chain
from ui import render_chat_ui

def main():
    st.set_page_config(page_title="Healthcare Chatbot", page_icon="🏥", layout="centered")
  
    st.warning("This project is for educational purposes only.It is not a substitute for professional medical advice, diagnosis, or treatment.", icon="⚠️")

    
    with st.sidebar:
        uploaded_files = st.file_uploader("Upload CSV files", type=["csv"], accept_multiple_files=True)
        process = st.button("Process")
        api_key = st.text_input("OpenAI API Key", type="password")
    if process and uploaded_files:
        dfs = read_csv_files(uploaded_files)
        symptoms_df, precautions_df = identify_files(dfs)
        final_df = merge_symptoms_precautions(symptoms_df, precautions_df)
        chunks_df = create_chunks(final_df)
        kb_index = build_knowledge_base(chunks_df)
        retriever = build_retriever(kb_index)
        st.session_state["conversation"] = get_conversation_chain(retriever, api_key)
        st.session_state["input_box"] = ""
    render_chat_ui()

if __name__ == "__main__":
    main()
