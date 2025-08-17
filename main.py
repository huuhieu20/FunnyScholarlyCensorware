import streamlit as st

st.title("📚 Thư viện động vật")

# Chia layout thành 5 cột
col1, col2, col3, col4, col5 = st.columns(5)

# Button cho từng loài động vật
with col1:
    if st.button("🐶 Chó"):
        st.header("Thông tin về Chó")
        st.image("https://tinhocnews.com/wp-content/uploads/2024/08/con-cho-vector-2.jpg", caption="Chó")
        st.audio("https://www.youtube.com/shorts/ZZe64YdYZtc")
        st.video("https://www.youtube.com/shorts/ZZe64YdYZtc")

with col2:
    if st.button("🐱 Mèo"):
        st.header("Thông tin về Mèo")
        st.image("https://life.thanhcong.vn/wp-content/uploads/2023/01/con-vat-yeu-thich-con-meo-1024x576.jpg", caption="Mèo")
        st.audio("https://www.youtube.com/shorts/wSmXeHBOX0U")
        st.video("https://www.youtube.com/shorts/wSmXeHBOX0U")

with col3:
    if st.button("🦁 Sư tử"):
        st.header("Thông tin về Sư tử")
        st.image("https://upload.wikimedia.org/wikipedia/commons/6/65/S%C6%B0_t%E1%BB%AD.jpg", caption="Sư tử")
        st.audio("https://www.youtube.com/shorts/UMG6gdx_XlI")
        st.video("https://www.youtube.com/shorts/UMG6gdx_XlI")

with col4:
    if st.button("🐼 Gấu trúc"):
        st.header("Thông tin về Gấu trúc")
        st.image("https://bhd.1cdn.vn/2025/05/07/gau-truc-a-h-1.jpg", caption="Gấu trúc")
        st.audio("https://www.youtube.com/shorts/keaqxclw8-Y")
        st.video("https://www.youtube.com/shorts/keaqxclw8-Y")

with col5:
    if st.button("🐧 Chim cánh cụt"):
        st.header("Thông tin về Chim cánh cụt")
        st.image("https://cdn.kienthuc.net.vn/images/9844b981f036879f9b909128e32501aef24648917069dfdccd781d6f102a20d56c47a17730bdff205843a51e1db26111/canhh-5.jpg", caption="Chim cánh cụt")
        st.audio("https://www.youtube.com/shorts/8L6NFy09xTI")
        st.video("https://www.youtube.com/shorts/8L6NFy09xTI")
