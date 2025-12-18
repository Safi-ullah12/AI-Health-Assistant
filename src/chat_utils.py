from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage, AIMessage
import streamlit as st

def get_conversation_chain(retriever, api_key: str):
    system_prompt = """You are a Healthcare Symptom Analysis Assistant. 
Your role is to analyze user‑provided symptoms using ONLY the retrieved dataset entries. 
Do not invent, guess, or provide medical advice beyond the dataset.

Tasks:
1. Match the user’s symptoms to the most relevant disease entry in the dataset. 
   - If no match is found, respond: “I don’t have enough data to identify a disease based on this symptom.”
2. Provide a simple, user‑friendly explanation of the disease (from dataset context only).
3. List all associated symptoms exactly as they appear in the dataset.
4. Provide the recommended precautions exactly as they appear in the dataset.
5. Always include a disclaimer: “⚠️ This project is for educational purposes only and not a substitute for medical advice.”

Output format:
- Possible Disease: <disease name or 'No match'>
- Explanation: <plain language summary>
- Key Symptoms: <comma‑separated list>
- Recommended Precautions: <comma‑separated list>
    """
    qa_prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "User question: {question}\n\nRelevant dataset entries:\n{context}")
    ])
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=api_key)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    return ConversationalRetrievalChain.from_llm(llm, retriever, memory=memory,
                                                 combine_docs_chain_kwargs={"prompt": qa_prompt})

def handle_userinput():
    user_question = st.session_state.get("input_box", "").strip()
    if not user_question:
        return
    st.session_state.chat_history.append(HumanMessage(content=user_question))
    try:
        response = st.session_state.conversation({"question": user_question})
        assistant_text = response.get("answer") or response.get("result") or "(No response)"
    except Exception as e:
        assistant_text = f"Error: {e}"
    st.session_state.chat_history.append(AIMessage(content=assistant_text))
    st.session_state.input_box = ""
