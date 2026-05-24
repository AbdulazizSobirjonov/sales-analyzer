import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sales Analyzer", layout="wide")

st.title("📊 Sales Data Analyzer")

# File upload
file = st.file_uploader(
    "CSV yoki Excel yuklang",
    type=["csv", "xlsx"]
)

if file:

    # Fayl o‘qish
    if file.name.endswith(".csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    # Data preview
    st.subheader("📄 Dataset")
    st.dataframe(df)

    # Statistics
    st.subheader("📈 Statistik ma'lumotlar")
    st.dataframe(df.describe(include='all'))

    # Numeric columns
    numeric_cols = df.select_dtypes(include='number').columns

    # Metrics
    if len(numeric_cols) > 0:

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Rows", df.shape[0])

        with col2:
            st.metric("Columns", df.shape[1])

        with col3:
            st.metric("Numeric Columns", len(numeric_cols))

        # Chart
        st.subheader("📊 Grafik")

        selected_col = st.selectbox(
            "Grafik uchun ustun tanlang",
            numeric_cols
        )

        st.bar_chart(df[selected_col].head(20))

    # Missing values
    st.subheader("❗ Missing Values")

    missing = df.isnull().sum()
    st.dataframe(missing[missing > 0])

else:
    st.info("CSV yoki Excel fayl yuklang")
