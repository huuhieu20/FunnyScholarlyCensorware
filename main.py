import streamlit as st
import pandas as pd

st.title("📊 Biểu đồ kim tự tháp dân số (Population Pyramid)")

data = pd.read_csv("pyramid.csv")

st.subheader("Dữ liệu gốc")
st.write(data)

data["Population_plot"] = data.apply(
    lambda row: -row["Population"] if row["Gender"] == "Male" else row["Population"], axis=1
)

st.subheader("Biểu đồ kim tự tháp dân số")

chart = {
    "data": {"values": data.to_dict(orient="records")},
    "mark": "bar",
    "encoding": {
        "y": {
            "field": "Age",
            "type": "ordinal",
            "sort": "ascending",
            "axis": {"title": "Nhóm tuổi"}
        },
        "x": {
            "field": "Population_plot",
            "type": "quantitative",
            "axis": {"title": "Dân số"},
        },
        "color": {
            "field": "Gender",
            "type": "nominal",
            "scale": {"range": ["#1f77b4", "#ff7f0e"]},
            "legend": {"title": "Giới tính"},
        },
        "tooltip": [
            {"field": "Gender", "type": "nominal", "title": "Giới tính"},
            {"field": "Age", "type": "ordinal", "title": "Độ tuổi"},
            {"field": "Population", "type": "quantitative", "title": "Dân số"},
        ],
    },
}

st.vega_lite_chart(chart, use_container_width=True)

st.markdown("""
### 🧩 Giải thích các phần:
- import streamlit, pandas → dùng để đọc file và hiển thị web.
- pd.read_csv("pyramid.csv") → đọc dữ liệu từ file.
- lambda row: -row["Population"] if Gender == "Male" → tạo cột dân số âm cho nam.
- st.vega_lite_chart() → vẽ biểu đồ Vega-Lite trong Streamlit.
- mark = "bar" → biểu đồ cột.
- field → trường dữ liệu (Age, Gender, Population).
- type → kiểu dữ liệu (quantitative, ordinal, nominal).
- color → phân biệt giới tính.
""")
