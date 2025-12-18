# 🩺 Milestone 1 — Project Scope & Functional Design

## 🎯 Objective
Design an intelligent chatbot that helps **general users** understand their health symptoms in **simple, human-friendly language**.

---

## 📌 Problem Statement
People often search online for medical information but face several difficulties:

- Technical jargon is **hard to understand**.  
- Articles **differ in accuracy** and reliability.  
- Users can **misinterpret symptoms**, leading to unnecessary anxiety or confusion.

---

## 🧠 Target Users
- General public seeking **symptom understanding**, not professional diagnosis.  
- Users with **low to moderate medical knowledge**.  
- People looking for **quick and simple explanations** rather than lengthy online research.

---

## 💡 Chatbot Features

### 🖊️ Symptom Input Interface (Streamlit Frontend)
- Users can type symptoms in natural language (e.g., “I have chest pain and shortness of breath”).  
- Clean and simple input box with a submit button.

### 🧩 Natural Language Understanding (LangChain Integration)
- The system processes the symptom query and interprets the user’s intent using **prompt templates**.  
- Supports flexible phrasing — not just keyword matching.

### 🤖 Response Generation using LLM
- Uses a free and LLM(like chatgpt4, chatgpt5 etc)  
- Generates responses in **clear and simple language**.  
- *(Features may change according to implementation feasibility.)*

### 📚 Medical Explanation (Knowledge-Augmented)
- The LLM retrieves information from a **verified medical dataset** curated by the developer.  
- Explains **possible causes** and general meaning of symptoms.

### ⚠️ Educational Disclaimer
- Each response includes a short disclaimer:  
  > “This is not a medical diagnosis. Consult a professional if symptoms persist.”

### 🧠 Conversational Memory *(Optional - Future Milestone)*
- Maintains short-term context between user and chatbot using **LangChain Memory**.  
- Example: User can ask follow-up questions like *“What should I do next?”*

### 💻 Simple, Interactive Web UI
- Built using **Streamlit**.  
- Includes sections for:
  - User input  
  - Chatbot response  
  - Explanation and references  

---

## 🚫 Limitations
- ❌ **No Diagnosis or Medical Advice** — Educational purpose only.  
- 📉 **Limited Dataset** — Covers only common symptoms and conditions.  
- 💬 **Text-Only Interaction** — No voice or image support in this version.  
- 🧮 **Limited Context Retention** — Short-term session memory only.  
- 🌐 **Non-Real-Time Data** — Static dataset, not connected to live medical sources.  
- ⚙️ **Model Accuracy Depends on Dataset Quality** — Responses vary based on data and model used.

---


## 🔄 Chatbot Workflow
User Input (Symptoms)  
↓  
LangChain Processing (Prompt Template)  
↓  
LLM Response Generation  
↓  
Display Explanation + Disclaimer (Streamlit)
---

## 🧭 User Journey

1. User opens the **AI Health Assistant** web app.  
2. Types symptoms (e.g., “I feel dizzy and tired”).  
3. The chatbot processes and generates an explanation.  
4. Displays the answer with disclaimer and reference note.  
5. User may ask a follow-up question for more clarity.  

---

📅 **Duration:** 1 Week  
👤 **Target User:** General Public  
💻 **Implementation Tools:** Python, Streamlit, LangChain, Local LLM (Phi-3 / Mistral / Llama 3)

---

✅ **Milestone 1 Completed:** Project scope, features, and user workflow defined.

---

## 🧭 User Journey

1. User opens the **AI Health Assistant** web app.  
2. Types symptoms (e.g., “I feel dizzy and tired”).  
3. The chatbot processes and generates an explanation.  
4. Displays the answer with disclaimer and reference note.  
5. User may ask a follow-up question for more clarity.  

---

📅 **Duration:** 1 Week  
👤 **Target User:** General Public  
💻 **Implementation Tools:** Python, Streamlit, LangChain, Local LLM (Phi-3 / Mistral / Llama 3)

---

✅ **Milestone 1 Completed:** Project scope, features, and user workflow defined.

---

## 🧭 User Journey

1. User opens the **AI Health Assistant** web app.  
2. Types symptoms (e.g., “I feel dizzy and tired”).  
3. The chatbot processes and generates an explanation.  
4. Displays the answer with disclaimer and reference note.  
5. User may ask a follow-up question for more clarity.  

---

📅 **Duration:** 1 Week  
👤 **Target User:** General Public  
💻 **Implementation Tools:** Python, Streamlit, LangChain, Local LLM (Phi-3 / Mistral / Llama 3)

---

✅ **Milestone 1 Completed:** Project scope, features, and user workflow defined.

---

## 🧭 User Journey

1. User opens the **AI Health Assistant** web app.  
2. Types symptoms (e.g., “I feel dizzy and tired”).  
3. The chatbot processes and generates an explanation.  
4. Displays the answer with disclaimer and reference note.  
5. User may ask a follow-up question for more clarity.  

---

📅 **Duration:** 1 Week  
👤 **Target User:** General Public  
💻 **Implementation Tools:** Python, Streamlit, LangChain, Local LLM (Phi-3 / Mistral / Llama 3/GPTALL(the mode can change according to sitution ))

---

✅ **Milestone 1 Completed:** Project scope, features, and user workflow defined.


