import streamlit as st
import pandas as pd

# Cấu hình giao diện trang
st.set_page_config(page_title="Biểu đồ tròn kim tự tháp", layout="wide")

# Tiêu đề
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

# Cấu hình biểu đồ Vega-Lite (đã thay thế phần code trong ảnh)
chart = {
    "config": {
        "background": "#ffffff"  # Nền trắng
    },
    "mark": {"type": "arc", "outerRadius": 10, "innerRadius": 0},
    "encoding": {
        "theta": {"field": "value", "type": "quantitative"},
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

# Hiển thị biểu đồ
st.vega_lite_chart(data, chart, use_container_width=True)
