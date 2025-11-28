# pyright: reportMissingImports=false

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Phân tích dữ liệu mô tả & chuẩn đoán bằng Streamlit")

uploaded_file = st.file_uploader("📥 Tải file Excel (.xlsx)", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    st.subheader("📌 1. Dữ liệu gốc")
    st.dataframe(df)

    st.subheader("📌 2. Phân tích dữ liệu mô tả")
    st.write("### ✔ Thống kê mô tả")
    st.write(df.describe())

    st.write("### ✔ Thiếu dữ liệu")
    st.write(df.isnull().sum())

    st.write("### ✔ Kiểu dữ liệu")
    st.write(df.dtypes)

    st.subheader("📌 3. Biểu đồ phân tích chuẩn đoán")

    numeric_cols = df.select_dtypes(include=["int", "float"]).columns.tolist()

    if numeric_cols:
        st.write("### 🔹 Histogram")
        col_hist = st.selectbox("Chọn cột để vẽ Histogram", numeric_cols)

        fig1, ax1 = plt.subplots()
        ax1.hist(df[col_hist].dropna())
        ax1.set_title(f"Histogram của {col_hist}")
        st.pyplot(fig1)

        st.write("### 🔹 Scatter Plot")
        col_x = st.selectbox("Chọn cột X", numeric_cols)
        col_y = st.selectbox("Chọn cột Y", numeric_cols)

        fig2, ax2 = plt.subplots()
        ax2.scatter(df[col_x], df[col_y])
        ax2.set_title(f"Scatter Plot: {col_x} vs {col_y}")
        st.pyplot(fig2)

