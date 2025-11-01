import streamlit as st
import pandas as pd
import altair as alt

st.title("📊 Biểu đồ cột đứng: Scores vs Hours")

# B1: Đọc dữ liệu từ file score.csv
df = pd.read_csv("score.csv")

# Hiển thị dữ liệu
st.write("### Dữ liệu gốc:")
st.dataframe(df)

# B2: Vẽ biểu đồ cột đứng
chart = alt.Chart(df).mark_bar().encode(
    x=alt.X("Scores:O", title="Scores"),   # trục X là dạng danh mục
    y=alt.Y("Hours", title="Hours"),       # trục Y là số giờ
    color=alt.Color("Scores", legend=None)
).properties(
    title="Biểu đồ cột: Scores vs Hours",
    width=600,
    height=400
)

st.altair_chart(chart, use_container_width=True)


