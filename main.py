import streamlit as st

st.title("📚 Thư viện động vật")

# Chia layout thành 5 cột
col1, col2, col3, col4, col5 = st.columns(5)

# Button cho từng loài động vật
with col1:
    if st.button("🐶 Chó"):
        st.header("Thông tin về Chó")
        st.image("https://i.imgur.com/UMK7W0S.jpg", caption="Chó")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")

with col2:
    if st.button("🐱 Mèo"):
        st.header("Thông tin về Mèo")
        st.image("https://i.imgur.com/v0JXau2.jpg", caption="Mèo")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3")
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")

with col3:
    if st.button("🦁 Sư tử"):
        st.header("Thông tin về Sư tử")
        st.image("https://i.imgur.com/r7M8WPt.jpg", caption="Sư tử")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3")
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")

with col4:
    if st.button("🐼 Gấu trúc"):
        st.header("Thông tin về Gấu trúc")
        st.image("https://i.imgur.com/fn7W1Kn.jpg", caption="Gấu trúc")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3")
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")

with col5:
    if st.button("🐧 Chim cánh cụt"):
        st.header("Thông tin về Chim cánh cụt")
        st.image("https://i.imgur.com/J7Q9X1A.jpg", caption="Chim cánh cụt")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3")
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")
