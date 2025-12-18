# 🧩 Milestone 2 — Tech Stack & Environment Setup

## 🎯 Goal
The goal of **Milestone 2** is to set up the complete technical environment for the **AI Health Assistant** project.  
This milestone ensures all libraries, tools, and frameworks are installed, tested, and configured — so the development environment is ready for model integration and data processing.

---

## 🧠 Project Overview

**Project Name:** AI Health Assistant    
**Target Users:** General users (non-technical)  
**Purpose:**  
A healthcare chatbot that explains disease symptoms in simple language, provides basic precautions, and helps users understand health-related terms.

---

## 🧰 Task 1 — Define Tech Stack

| Category | Tool / Library | Purpose |
|-----------|----------------|----------|
| **Language** | Python 3.10+ | Core programming language |
| **Framework** | Streamlit | Web app interface for chatbot |
| **LLM Framework** | LangChain | LLM orchestration and chaining |
| **Model** | GPT-4o-mini (OpenAI-compatible) | For generating natural language responses |
| **Data** | `DiseaseAndSymptoms.csv`, `DiseasePrecaution.csv` | Kaggle datasets for disease & symptom info |
| **Libraries** | Pandas, Numpy | Data handling and analysis |
| **Environment** | Anaconda / VS Code | Development and execution environment |
| **Version Control** | Git & GitHub | For version tracking and collaboration |

---

## ⚙️ Task 2 — Environment Setup

### 🧩 Steps Performed

1. **Installed Dependencies**
   ```bash
   pip install langchain langchain-community langchain-openai streamlit pandas numpy
python --version
conda list
## 🧪 Task 3 — Verify Dataset Integration

* Downloaded datasets from Kaggle:

    * DiseaseAndSymptoms.csv

    * DiseasePrecaution.csv

* Verified correct loading in Python:
## 🔗 Task 4 — Verify LangChain Installation
Commands Executed:  
```bash
pip install langchain langchain-community langchain-openai
```
## 🧠 Task 5 — LangChain Integration Test (Proof of Concept)
# 🎯 Goal

To test a simple LangChain prompt using PromptTemplate and LLMChain, ensuring LLM response flow is working.
## Task 6 — Version Control & Documentation

## Created and committed all files to GitHub repository:

```bash git add .
git commit -m "Completed Milestone 2: Environment setup and LangChain integration test"
git push origin main
```
| Task                   | Description                                         | Status |
| ---------------------- | --------------------------------------------------- | ------ |
| Tech Stack Definition  | Selected tools, frameworks, and libraries           | ✅      |
| Environment Setup      | Installed dependencies and created folder structure | ✅      |
| Dataset Integration    | Verified CSV loading                                | ✅      |
| LangChain Installation | Installed and tested                                | ✅      |
| LangChain Test Script  | Implemented proof-of-concept LLMChain               | ✅      |
| GitHub Commit          | Pushed milestone files                              | ✅      |
## 🏁 Milestone 2 Status: Completed Successfully ✅
## Next Step → Milestone 3: Data Preprocessing

You will clean, format, and prepare the Kaggle datasets (DiseaseAndSymptoms.csv and DiseasePrecaution.csv) for chatbot integration.



