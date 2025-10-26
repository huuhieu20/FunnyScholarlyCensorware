import streamlit as st
import pandas as pd

st.title("🟠 Biểu đồ tròn tạo hình kim tự tháp bằng Vega-Lite")

# Dữ liệu mô phỏng
data = pd.DataFrame({
    "category": ["Bầu trời", "Mặt tối", "Mặt sáng"],
    "value": [60, 15, 25],
    "order": [1, 2, 3]
})

# Cấu hình biểu đồ
chart = {
    "mark": {"type": "arc"},
    "encoding": {
        "theta": {
            "field": "value",
            "type": "quantitative",
            "scale": {"range": [2.35619449, 8.639379797]}
        },
        "color": {
            "field": "category",
            "type": "nominal",
            "scale": {
                "domain": ["Bầu trời", "Mặt tối", "Mặt sáng"],
                "range": ["#416D9D", "#674028", "#DEAC58"]
            },
            "legend": {
                "orient": "right",
                "title": "Chú thích màu sắc"
            }
        },
        "order": {"field": "order"}
    }
}

# Hiển thị biểu đồ
st.vega_lite_chart(data, chart, use_container_width=True)
