import streamlit as st

st.set_page_config(page_title="MBTI 플레이리스트 추천", layout="wide")
st.title("🎧 MBTI별 플레이리스트 & 대표곡 추천")
st.markdown("""
당신의 MBTI 유형에 어울리는 **분위기 있는 플레이리스트**와 **유명한 노래**들을 확인해보세요!
감성부터 에너지까지, MBTI별 감정에 딱 맞는 노래들을 큐레이션했습니다.
""")

mbti_playlist = {
    "INFP": {
        "분위기": "감성적이고 몽환적인 분위기",
        "대표 노래": [
            "Lauv - Paris in the Rain",
            "Billie Eilish - idontwannabeyouanymore",
            "Troye Sivan - Fools",
            "세정 - 꽃길",
            "적재 - 나랑 같이 걸을래",
            "검정치마 - Everything",
            "윤하 - 사건의 지평선"
        ]
    },
    "INFJ": {
        "분위기": "잔잔하고 의미 있는 가사 위주의 음악",
        "대표 노래": [
            "Sufjan Stevens - Mystery of Love",
            "Lana Del Rey - Young and Beautiful",
            "태연 - 사계",
            "오반 - 어쩌면",
            "IU - Love Poem",
            "브로콜리 너마저 - 유자차",
            "정승환 - 너였다면"
        ]
    },
    "ENFP": {
        "분위기": "자유롭고 기분 좋아지는 노래",
        "대표 노래": [
            "Foster the People - Sit Next to Me",
            "Shawn Mendes - There's Nothing Holdin' Me Back",
            "아이유 - 팔레트",
            "AKMU - 200%",
            "Red Velvet - Queendom",
            "볼빨간사춘기 - 여행",
            "NewJeans - Super Shy"
        ]
    },
    "ENTP": {
        "분위기": "도전적이고 창의적인 분위기의 음악",
        "대표 노래": [
            "Imagine Dragons - Thunder",
            "Glass Animals - Heat Waves",
            "BTS - IDOL",
            "지코 - Artist",
            "카더가든 - 명동콜링",
            "Dean - Instagram",
            "혁오 - 위잉위잉"
        ]
    },
    "INTJ": {
        "분위기": "지적인 느낌의 몰입 가능한 음악",
        "대표 노래": [
            "Imagine Dragons - Warriors",
            "AURORA - Runaway",
            "Woodkid - Run Boy Run",
            "이수 - My Way",
            "케이윌 - 이러지마 제발",
            "RADWIMPS - Zenzenzense",
            "김필 - 다시 사랑한다면"
        ]
    },
    "INTP": {
        "분위기": "철학적이고 실험적인 음악",
        "대표 노래": [
            "Bon Iver - Holocene",
            "Radiohead - Creep",
            "카더가든 - 그대 나를 일으켜주면",
            "요조 - 우리는 선처럼 가만히 누워",
            "이하이 - 한숨",
            "검정치마 - Love Shine",
            "정승환 - 이 바보야"
        ]
    },
    "ENTJ": {
        "분위기": "열정적이고 리더십 있는 음악",
        "대표 노래": [
            "Kanye West - Stronger",
            "Beyoncé - Run The World (Girls)",
            "2NE1 - 내가 제일 잘 나가",
            "박재범 - All I Wanna Do",
            "Stray Kids - Maniac",
            "NCT 127 - Cherry Bomb",
            "MAMAMOO - HIP"
        ]
    },
    "ENFJ": {
        "분위기": "사람을 생각하게 하는 감성적인 음악",
        "대표 노래": [
            "Coldplay - Fix You",
            "Adele - Someone Like You",
            "폴킴 - 모든 날, 모든 순간",
            "태연 - 만약에",
            "소유 - I Miss You",
            "케이시 - 그때가 좋았어",
            "Crush - 잊어버리지 마"
        ]
    },
    "ISFJ": {
        "분위기": "따뜻하고 편안한 분위기의 음악",
        "대표 노래": [
            "백예린 - 우주를 건너",
            "IU - 밤편지",
            "김동률 - 감사",
            "10cm - 폰서트",
            "노리플라이 - 그대와 함께",
            "Standing Egg - 오래된 노래",
            "윤하 - 비밀번호 486"
        ]
    },
    "ISTJ": {
        "분위기": "꾸준하고 성실한 느낌의 음악",
        "대표 노래": [
            "Paul Kim - 너를 만나",
            "임영웅 - 이제 나만 믿어요",
            "이석훈 - 그대를 사랑하는 10가지 이유",
            "김범수 - 보고싶다",
            "이승철 - 소녀시대",
            "나얼 - 바람기억",
            "이수 - My Way"
        ]
    },
    "ESFJ": {
        "분위기": "따뜻하고 사랑 가득한 음악",
        "대표 노래": [
            "마마무 - Starry Night",
            "윤미래 - Always (태양의 후예 OST)",
            "임한별 - 이별하러 가는 길",
            "볼빨간사춘기 - 나만, 봄",
            "아이유 - 좋은 날",
            "Paul Kim - 허전해",
            "태연 - 그대라는 시"
        ]
    },
    "ESTJ": {
        "분위기": "성취욕 자극하는 파워풀한 음악",
        "대표 노래": [
            "Imagine Dragons - Believer",
            "Fall Out Boy - Centuries",
            "Stray Kids - God's Menu",
            "박재범 - 좋아",
            "Beyoncé - Run the World (Girls)",
            "Jessie J - Bang Bang",
            "NCT 127 - 영웅 (Kick It)"
        ]
    },
    "ISTP": {
        "분위기": "혼자 있을 때 듣기 좋은 감각적 음악",
        "대표 노래": [
            "Joji - Glimpse of Us",
            "DEAN - D (half moon)",
            "Crush - SOFA",
            "잔나비 - 주저하는 연인들을 위해",
            "검정치마 - 기다린 만큼, 더",
            "Colde - WA-R-R",
            "혁오 - TOMBOY"
        ]
    },
    "ISFP": {
        "분위기": "감성적이고 잔잔한 감정선의 음악",
        "대표 노래": [
            "IU - 무릎",
            "백예린 - 그건 아마 우리의 잘못은 아닐 거야",
            "하현우 - 돌덩이",
            "정승환 - 눈사람",
            "이하이 - 손잡아줘요",
            "윤하 - 비가 내리는 날에는",
            "잔나비 - 꿈과 책과 힘과 벽"
        ]
    },
    "ESFP": {
        "분위기": "흥 넘치고 에너지 있는 음악",
        "대표 노래": [
            "Dua Lipa - Don't Start Now",
            "Doja Cat - Say So",
            "BTS - Dynamite",
            "ZICO - 아무노래",
            "Twice - Dance The Night Away",
            "Itzy - WANNABE",
            "IVE - I AM"
        ]
    }
}

mbti_list = list(mbti_playlist.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_list)

if selected_mbti:
    info = mbti_playlist[selected_mbti]
    st.subheader(f"🎵 {selected_mbti} - {info['분위기']}")
    st.markdown("### 📀 대표 추천 노래")
    for song in info["대표 노래"]:
        st.markdown(f"- {song}")
