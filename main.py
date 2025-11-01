import streamlit as st
import pandas as pd
import altair as alt  # Vega-Lite được tích hợp qua thư viện Altair

# B1: Khai báo thư viện Streamlit và Pandas (đã làm ở trên)

# B2: Đọc file CSV
df = pd.read_csv("score.csv")  # đổi tên file đúng với file bạn có

# Hiển thị dữ liệu
st.write("📊 Dữ liệu gốc:")
st.dataframe(df)

# B3: Chuyển dữ liệu sang dataframe (đã là DataFrame)
# Nếu cần, có thể xử lý cột hoặc đổi kiểu dữ liệu tại đây

# B4: Vẽ biểu đồ cột
chart = alt.Chart(df).mark_bar().encode(
    x=alt.X(df.columns[0], title="Tên cột X"),
    y=alt.Y(df.columns[1], title="Giá trị"),
    color=alt.Color(df.columns[0], legend=None)
).properties(
    title="Biểu đồ cột từ file score.csv",
    width=600,
    height=400
)

st.altair_chart(chart, use_container_width=True)


