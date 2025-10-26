import streamlit as st
import pandas as pd
import math

# Cấu hình trang
st.set_page_config(page_title="Biểu đồ tròn kim tự tháp", layout="wide")

# Tiêu đề trang
st.markdown(
    "<h1 style='text-align:center;'>🟠 Biểu đồ tròn tạo hình kim tự tháp</h1>",
    unsafe_allow_html=True
)

# Dữ liệu
data = pd.DataFrame({
    "category": ["Bầu trời", "Mặt tối", "Mặt sáng"],
    "value": [80, 10, 15],
    "order": [1, 2, 3]
})

# Cấu hình biểu đồ
chart = {
    "mark": {"type": "arc", "outerRadius": 150},
    "encoding": {
        "theta": {
            "field": "value",
            "type": "quantitative",
            # Xoay biểu đồ về hướng 6h (thẳng xuống)
            "scale": {"range": [math.pi / 2, (5 * math.pi) / 2]}
        },
        "color": {
            "field": "category",
            "type": "nominal",
            "scale": {
                "domain": ["Bầu trời", "Mặt tối", "Mặt sáng"],
                "range": ["#416D9D", "#674028", "#DEAC58"]
            },
            "legend": {"orient": "right", "title": "Chú thích màu sắc"}
        },
        "order": {"field": "order"}
    },
    "config": {"background": "#ffffff"}  # Nền trắng
}

# Hiển thị biểu đồ
st.vega_lite_chart(data, chart, use_container_width=True)


