import streamlit as st

# Hàm chuyển link shorts -> watch
def fix_youtube_url(url: str) -> str:
    if "youtube.com/shorts/" in url:
        video_id = url.split("/")[-1].split("?")[0]
        return f"https://www.youtube.com/watch?v={video_id}"
    return url

st.title("📚 Thư viện động vật")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("🐶 Chó"):
        st.header("Thông tin về Chó")
        st.image("https://tinhocnews.com/wp-content/uploads/2024/08/con-cho-vector-2.jpg", caption="Chó")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
        st.video(fix_youtube_url("https://www.youtube.com/shorts/ZZe64YdYZtc"))

with col2:
    if st.button("🐱 Mèo"):
        st.header("Thông tin về Mèo")
        st.image("https://life.thanhcong.vn/wp-content/uploads/2023/01/con-vat-yeu-thich-con-meo-1024x576.jpg", caption="Mèo")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3")
        st.video(fix_youtube_url("https://www.youtube.com/shorts/wSmXeHBOX0U"))

with col3:
    if st.button("🦁 Sư tử"):
        st.header("Thông tin về Sư tử")
        st.image("https://upload.wikimedia.org/wikipedia/commons/6/65/S%C6%B0_t%E1%BB%AD.jpg", caption="Sư tử")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3")
        st.video(fix_youtube_url("https://www.youtube.com/shorts/UMG6gdx_XlI"))

with col4:
    if st.button("🐼 Gấu trúc"):
        st.header("Thông tin về Gấu trúc")
        st.image("https://bhd.1cdn.vn/2025/05/07/gau-truc-a-h-1.jpg", caption="Gấu trúc")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3")
        st.video(fix_youtube_url("https://www.youtube.com/shorts/keaqxclw8-Y"))

with col5:
    if st.button("🐧 Chim cánh cụt"):
        st.header("Thông tin về Chim cánh cụt")
        st.image("https://cdn.kienthuc.net.vn/images/9844b981f036879f9b909128e32501aef24648917069dfdccd781d6f102a20d56c47a17730bdff205843a51e1db26111/canhh-5.jpg", caption="Chim cánh cụt")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3")
        st.video(fix_youtube_url("https://www.youtube.com/shorts/8L6NFy09xTI"))
