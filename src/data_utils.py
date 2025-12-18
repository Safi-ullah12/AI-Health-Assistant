import pandas as pd
import numpy as np
from typing import List, Tuple
import streamlit as st


def read_csv_files(uploaded_files: List[st.runtime.uploaded_file_manager.UploadedFile]) -> List[pd.DataFrame]:
    """
    Read multiple uploaded CSV files into pandas DataFrames.
    
    Args:
        uploaded_files: List of Streamlit UploadedFile objects.
    
    Returns:
        List of pandas DataFrames (one per successfully read file).
    """
    dfs: List[pd.DataFrame] = []
    for f in uploaded_files:
        try:
            df = pd.read_csv(f)
            dfs.append(df)
        except Exception as e:
            st.warning(f"Could not read {getattr(f, 'name', 'file')}: {e}")
    return dfs


def normalize_string(x) -> str:
    if pd.isna(x):
        return ""
    return str(x).strip().lower()

def clean_dataframe_strings(df: pd.DataFrame) -> pd.DataFrame:
    obj_cols = df.select_dtypes(include=["object"]).columns
    df[obj_cols] = df[obj_cols].applymap(normalize_string)
    return df

def deduplicate_preserve_order(values: List) -> List[str]:
    seen = set()
    result = []
    for v in values:
        # Flatten lists inside cells
        if isinstance(v, list):
            for item in v:
                s = normalize_string(item)
                if s and s not in seen:
                    seen.add(s)
                    result.append(s)
        else:
            s = normalize_string(v)
            if s and s not in seen:
                seen.add(s)
                result.append(s)
    return result


def identify_files(dfs: List[pd.DataFrame]) -> Tuple[pd.DataFrame, pd.DataFrame]:
    symptoms_df, precautions_df = None, None
    for df in dfs:
        if "Disease" not in df.columns:
            continue
        df = clean_dataframe_strings(df)
        has_symptom = any("symptom" in c.lower() for c in df.columns)
        has_precaution = any("precaution" in c.lower() for c in df.columns)
        if has_symptom and symptoms_df is None:
            symptoms_df = df
        elif has_precaution and precautions_df is None:
            precautions_df = df
    return symptoms_df, precautions_df

def merge_symptoms_precautions(symptoms_df: pd.DataFrame, precautions_df: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(symptoms_df, precautions_df, on="Disease", how="left")
    symptom_cols = [c for c in merged.columns if "symptom" in c.lower()]
    precaution_cols = [c for c in merged.columns if "precaution" in c.lower()]

    merged["all_symptoms"] = merged[symptom_cols].apply(lambda r: deduplicate_preserve_order(r.values), axis=1)
    merged["precautions"] = merged[precaution_cols].apply(lambda r: deduplicate_preserve_order(r.values), axis=1)

    # Convert lists to tuples for deduplication
    merged["all_symptoms"] = merged["all_symptoms"].apply(tuple)
    merged["precautions"] = merged["precautions"].apply(tuple)

    merged = merged[["Disease", "all_symptoms", "precautions"]].dropna().drop_duplicates()

    # Convert back to lists for downstream use
    merged["all_symptoms"] = merged["all_symptoms"].apply(list)
    merged["precautions"] = merged["precautions"].apply(list)

    return merged
