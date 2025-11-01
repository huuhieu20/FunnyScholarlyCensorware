import streamlit as st
import pandas as pd
import altair as alt  # Vega-Lite thông qua Altair

# B1: Khai báo thư viện Streamlit và Pandas
st.title("📊 Biểu đồ cột từ file score.csv")

# B2: Đọc file CSV
df = pd.read_csv("score.csv")

# Hiển thị dữ liệu
st.write("### Dữ liệu gốc")
st.dataframe(df)

# B3: Dùng dataframe làm dữ liệu cho biểu đồ
x_col = st.selectbox("Chọn cột cho trục X:", df.columns)
y_col = st.selectbox("Chọn cột cho trục Y:", df.columns)

# B4: Vẽ biểu đồ cột bằng Vega-Lite (Altair)
chart = alt.Chart(df).mark_bar().encode(
    x=alt.X(x_col, title=x_col),
    y=alt.Y(y_col, title=y_col),
    color=alt.Color(x_col, legend=None)
).properties(
    title=f"Biểu đồ cột: {x_col} vs {y_col}",
    width=600,
    height=400
)

st.altair_chart(chart, use_container_width=True)

