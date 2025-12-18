import pandas as pd
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

def format_entry(disease: str, symptoms: list, precautions: list) -> str:
    return f"Disease: {disease}\nSymptoms: {', '.join(symptoms)}\nPrecautions: {', '.join(precautions)}"

def create_chunks(df: pd.DataFrame, chunk_size: int = 800, chunk_overlap: int = 50) -> pd.DataFrame:
    splitter = CharacterTextSplitter(separator="\n\n", chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    rows = []
    for _, row in df.iterrows():
        text = format_entry(row["Disease"], row["all_symptoms"], row["precautions"])
        for j, chunk in enumerate(splitter.split_text(text)):
            rows.append({"disease": row["Disease"], "chunk_id": f"{row['Disease']}_{j}", "text_chunk": chunk})
    return pd.DataFrame(rows)

def build_knowledge_base(chunks_df: pd.DataFrame):
    embedding = HuggingFaceEmbeddings(model_name=MODEL_NAME)
    return FAISS.from_texts(chunks_df["text_chunk"].tolist(), embedding)

def build_retriever(kb_index):
    return kb_index.as_retriever()
