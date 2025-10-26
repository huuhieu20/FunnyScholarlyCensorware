import streamlit as st
import pandas as pd
import math

st.set_page_config(page_title="Biểu đồ tròn kim tự tháp", layout="wide")

st.markdown(
    "<h1 style='text-align:center;'>🟠 Biểu đồ tròn tạo hình kim tự tháp</h1>",
    unsafe_allow_html=True
)

# Dữ liệu cho biểu đồ
data = pd.DataFrame({
    "category": ["Bầu trời", "Mặt tối", "Mặt sáng"],
    "value": [80, 10, 15],
    "order": [1, 2, 3]
})

# Biểu đồ Vega-Lite xoay hướng xuống 6h
chart = {
    "config": {"background": "#ffffff"},
    "mark": {"type": "arc", "outerRadius": 150, "innerRadius": 0},
    "encoding": {
        "theta": {
            "field": "value",
            "type": "quantitative",
            # Xoay biểu đồ xuống hướng 6 giờ
            "startAngle": math.pi,
            "endAngle": 3 * math.pi
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
    }
}

st.vega_lite_chart(data, chart, use_container_width=True)
