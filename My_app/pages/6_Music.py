import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import feedparser
import numpy as np
import time
import matplotlib.pyplot as plt
import random
import time

st.title("🎧 Ứng dụng giải trí và sức khỏe")
menu = st.selectbox("Chọn chức năng mà bạn muốn dùng: ",["🎤 MV yêu thích", "📰 Đọc báo","Giá vàng", "Kiểm tra sức khoẻ","Kiểm tra tính cách theo DISC","Nhân tướng học","Nhắc nhở nghỉ ngơi và tập thể dục","Ứng dụng theo dõi sức khoẻ nâng cao","Game"])
if menu == '🎤 MV yêu thích':
    st.sidebar.title("🎶 Danh sách nghệ sĩ")
    selected_artist = st.sidebar.radio("Chọn nghệ sĩ:", ["Đen Vâu", "Sơn Tùng M-TP", "Big Bang", "BTS", "Alan Walker", "LowG", "The Fat Rat", "Justin Bieber", "Other"])

    videos = {
        "Đen Vâu": [
            ("Bữa ăn cho em", "https://www.youtube.com/watch?v=ukHK1GVyr0I"),
            ("Mang tiền về cho mẹ", "https://www.youtube.com/watch?v=UVbv-PJXm14"),
            ("Trời hôm nay nhiều mây cực!", "https://www.youtube.com/watch?v=MBaF0l-PcRY"),
            ("Hai triệu năm", "https://www.youtube.com/watch?v=LSMDNL4n0kM"),
            ("Trốn tìm", "https://youtu.be/Ws-QlpSltr8?si=KN1LHA3C_EkUyoLZ")
        ],
        
        "Sơn Tùng M-TP": [
            ("Lạc trôi", "https://www.youtube.com/watch?v=Llw9Q6akRo4"),
            ("Chúng ta không thuộc về nhau", "https://www.youtube.com/watch?v=qGRU3sRbaYw"),
            ("Muộn rồi mà sao còn", "https://www.youtube.com/watch?v=xypzmu5mMPY"),
            ("Hãy trao cho anh", "https://www.youtube.com/watch?v=knW7-x7Y7RE"),
            ("Come my way", "https://youtu.be/SlQR9iu09bQ?si=6e4w4ruvx93VZr0M")
        ],
        "Big Bang": [
            ("Bang Bang Bang", "https://youtu.be/2ips2mM7Zqw?si=YdpWjYcAlrqwroYH"),
            ("Fantastic baby", "https://youtu.be/AAbokV76tkU?si=qZuLkDF79dO-k1YI"),
            ("Fxxk it", "https://youtu.be/iIPH8LFYFRk?si=gq9KBCPaaWzzQHth"),
            ("Sober", "https://youtu.be/MBNQgq56egk?si=pqAs5-IRwQmqjA-Z"),
            ("Bad boy", "https://youtu.be/1qnV55LUFVM?si=MVOlyRhhmP2Gmw1j")
        ],
        "BTS": [
            ("Fire", "https://youtu.be/ALj5MKjy2BU?si=ngNdsVlfqGFERDoY"),
            ("Mic drop", "https://youtu.be/kTlv5_Bs8aw?si=E5pDSbB8zDr2YHEB"),
            ("We are bulletproof p2", "https://youtu.be/gqhWHy0rrtM?si=QRkK8cyYUxzG9qV3"),
            ("DNA", "https://youtu.be/MBdVXkSdhwU?si=iomEIvIUn56yCbCY"),
            ("Dope", "https://youtu.be/BVwAVbKYYeM?si=DlY7xQXjY_RT6bR-")
        ],
        "Alan Walker": [
            ("The spectre", "https://youtu.be/wJnBTPUQS5A?si=DSD1txkr8ziMJuY7"),
            ("Faded", "https://youtu.be/60ItHLz5WEA?si=SuIWxOpmSCnPytQR"),
            ("Alone", "https://youtu.be/1-xGerv5FOk?si=vu3ZQPQ8qDEzIBV7"),
            ("Fate", "https://youtu.be/LKp-IdxVf4A?si=3nhybVRKP80oioAk"),
            ("Force", "https://youtu.be/lqYQXIt4SpA?si=PBjJe5i8Wo2oX58Y")
        ],
        "LowG": [
            ("Simp gái 808", "https://youtu.be/6aBnhxRvmok?si=9JEYltiqKEAiDbKG"),
            ("An thần", "https://youtu.be/J7eYhM6wXPo?si=tRDxYWyXWHfDB8lU"),
            ("Tiếp đất", "https://youtu.be/IPdRiYPOvj0?si=ezf5cDO2B8kM96aX"),
            ("Love game", "https://youtu.be/cI5b71ZBAn0?si=IZBoxPfXgVrO8cvd"),
            ("Đừng để tiền rơi", "https://youtu.be/IGHBSyXKZ8Y?si=W8DdhXbEnu7zhfU8")
        ],
        "The Fat Rat": [
            ("Unity", "https://youtu.be/n8X9_MgEdCg?si=BN6CtbvetScLmUIy"),
            ("Monody", "https://youtu.be/B7xai5u_tnk?si=kRRxptgTu4qm5Efj"),
            ("Fly away", "https://youtu.be/cMg8KaMdDYo?si=ivcsdPEbAB-aI3dG"),
            ("Back one day", "https://youtu.be/2QdPxdcMhFQ?si=tnorAUFvWVFU1Zf8"),
            ("Time lapse", "https://youtu.be/3fxq7kqyWO8?si=_b-IcywBYVBQ2-Sa")
        ],
        "Justin Bieber": [
            ("Stay", "https://youtu.be/kTJczUoc26U?si=zXsWmRvFTuk0xgpf"),
            ("Baby", "https://youtu.be/kffacxfA7G4?si=ujzWp9LxTfE3VwRE"),
            ("Beauty and a beat", "https://youtu.be/Ys7-6_t7OEQ?si=rwLy_0LLeL0NVwY9"),
            ("First place", "https://youtu.be/EGKfSUDAiFg?si=K7QgEnjMN0eXnCSb"),
            ("Honest", "https://youtu.be/n1khwOk5dN8?si=nqVPztq8nc_IMGNV")
        ],
        "Other": [
            ("Thu cuối", "https://youtu.be/tN1TZAuL4P8?si=MTWTxU6EsysYRb9c"),
            ("Tháng năm", "https://youtu.be/UyXngX4kTfE?si=0qvZ6ytZaFNOzjFf"),
            ("Gangnam style", "https://youtu.be/9bZkp7q19f0?si=42NSSZBZip0yWrM0"),
            ("Bigcityboi", "https://youtu.be/jgZkrA8E5do?si=jn_DdCULQdQ9iz2R"),
            ("Blackjack", "https://youtu.be/zRdHnseM0PE?si=iHKwNw54IEZL165M")
        ]
    }
    st.header(f"Các bài hát của {selected_artist} 🎵")
    for title, url in videos[selected_artist]:
        st.subheader(title)
        st.video(url)