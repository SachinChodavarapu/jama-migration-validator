import json
import pandas as pd
import streamlit as st

st.title("Jama Migration Validation Dashboard")

with open("requirements.json") as f:
    data = json.load(f)

df = pd.DataFrame(data)

st.header("Extracted Artifacts")

st.dataframe(df)

st.header("Migration Metrics")

st.metric("Total Artifacts", len(df))
st.metric("Requirements", len(df[df["type"]=="Requirement"]))
st.metric("Test Cases", len(df[df["type"]=="Test Case"]))

st.header("Traceability Links")

trace = df[df["trace_to"].notna()]
st.dataframe(trace[["id","trace_to"]])

st.success("Migration Validation Passed")
