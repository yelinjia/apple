import streamlit as st
import folium
from streamlit_folium import st_folium

# 여행지 데이터 (20개)
locations = [
    {"name": "경복궁", "lat": 37.579617, "lon": 126.977041, "desc": "조선의 숨결을 느낄 수 있는 아름다운 궁궐"},
    {"name": "부산 해운대", "lat": 35.158698, "lon": 129.160384, "desc": "푸른 바다가 반겨주는 최고의 해변"},
    {"name": "제주도 성산일출봉", "lat": 33.4588, "lon": 126.9426, "desc": "일출 명소로 유명한 환상적인 오름"},
    {"name": "경주 불국사", "lat": 35.7902, "lon": 129.3313, "desc": "천년 고도의 불교문화유산"},
    {"name": "서울 남산타워", "lat": 37.5512, "lon": 126.9882, "desc": "야경이 아름다운 사랑의 명소"},
    {"name": "인사동", "lat": 37.5740, "lon": 126.9849, "desc": "한국 전통문화가 살아 숨 쉬는 거리"},
    {"name": "전주 한옥마을", "lat": 35.8142, "lon": 127.1509, "desc": "한옥의 아름다움을 간직한 마을"},
    {"name": "남이섬", "lat": 37.7906, "lon": 127.5250, "desc": "로맨틱한 드라마 촬영지"},
    {"name": "강릉 경포대", "lat": 37.7894, "lon": 128.9021, "desc": "바다와 호수가 만나는 절경"},
    {"name": "속초 설악산", "lat": 38.1194, "lon": 128.4656, "desc": "사계절 절경을 자랑하는 명산"},
    {"name": "대구 동성로", "lat": 35.8686, "lon": 128.5947, "desc": "젊음의 거리가 살아있는 쇼핑 명소"},
    {"name": "수원 화성", "lat": 37.2850, "lon": 127.0190, "desc": "정조의 꿈이 담긴 유네스코 문화유산"},
    {"name": "청계천", "lat": 37.5700, "lon": 126.9784, "desc": "도심 속 자연을 만나는 산책로"},
    {"name": "부산 감천문화마을", "lat": 35.0970, "lon": 129.0108, "desc": "알록달록 예술이 살아있는 마을"},
    {"name": "울산 대왕암공원", "lat": 35.5272, "lon": 129.4476, "desc": "해돋이와 파도가 어우러진 절경"},
    {"name": "안동 하회마을", "lat": 36.5383, "lon": 128.5185, "desc": "전통이 살아 숨쉬는 고택마을"},
    {"name": "DMZ 평화전망대", "lat": 38.2517, "lon": 127.0173, "desc": "분단의 역사와 평화를 느끼는 곳"},
    {"name": "충남 태안 꽃지해수욕장", "lat": 36.5501, "lon": 126.3126, "desc": "일몰이 아름다운 해변"},
    {"name": "무주 덕유산", "lat": 35.8666, "lon": 127.7542, "desc": "겨울엔 눈꽃, 여름엔 숲향기"},
    {"name": "포항 영일대 해수욕장", "lat": 36.0651, "lon": 129.3761, "desc": "바다 위 정자가 인상적인 휴양지"},
]

# 페이지 제목
st.title("🇰🇷 외국인이 사랑한 한국 여행지 TOP 20")
st.markdown("따뜻하고 사랑스러운 느낌으로 한국을 소개해요 💖")

# 중심 좌표는 서울 근처로 설정
m = folium.Map(location=[36.5, 127.9], zoom_start=7, tiles="CartoDB positron")

# 핑크 계열 마커 스타일
for place in locations:
    folium.Marker(
        [place["lat"], place["lon"]],
        tooltip=place["name"],
        popup=f"<b>{place['name']}</b><br>{place['desc']}",
        icon=folium.Icon(color='pink', icon='heart', prefix='fa')
    ).add_to(m)

# Folium 지도 렌더링
st_folium(m, width=700, height=500)
