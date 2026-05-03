import streamlit as st
import pandas as pd

st.title("📊 Sales Data Analyzer")

file = st.file_uploader("CSV yoki Excel yuklang", type=["csv","xlsx"])

if file:
    df = pd.read_csv(file) if file.name.endswith("csv") else pd.read_excel(file)
    st.dataframe(df)
    st.subheader("📈 Statistika")
st.write(df.describe(include='all'))
