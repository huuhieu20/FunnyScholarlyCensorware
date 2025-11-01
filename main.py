import streamlit as st
import pandas as pd
import altair as alt

st.title("📊 Biểu đồ cột đứng từ file score.csv")

# Đọc dữ liệu
df = pd.read_csv("score.csv")
st.write("### Dữ liệu gốc:")
st.dataframe(df)

# Chọn trục X và Y
x_col = st.selectbox("Chọn cột trục X:", df.columns)
y_col = st.selectbox("Chọn cột trục Y:", df.columns)

# Biểu đồ cột đứng
chart = alt.Chart(df).mark_bar().encode(
    x=alt.X(f"{x_col}:O", title=x_col),  # ":O" = dạng phân loại → cột đứng
    y=alt.Y(y_col, title=y_col),
    color=alt.Color(x_col, legend=None)
).properties(
    title=f"Biểu đồ cột: {x_col} vs {y_col}",
    width=600,
    height=400
)

st.altair_chart(chart, use_container_width=True)

