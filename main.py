import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 공부법 추천기", page_icon="🧠", layout="centered")

# 타이틀
st.markdown("<h1 style='text-align:center;'>🎯 MBTI별 맞춤 공부법 가이드 🎯</h1>", unsafe_allow_html=True)
st.markdown("공부가 안 될 땐, 내 성격을 먼저 이해해보자! 💡<br>MBTI를 선택하면 당신에게 딱 맞는 공부법을 알려드릴게요 👇", unsafe_allow_html=True)

# MBTI 리스트
mbti_list = [
    'ISTJ', 'ISFJ', 'INFJ', 'INTJ',
    'ISTP', 'ISFP', 'INFP', 'INTP',
    'ESTP', 'ESFP', 'ENFP', 'ENTP',
    'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ'
]

# MBTI 선택
selected = st.selectbox("🧬 당신의 MBTI는?", mbti_list)

# MBTI별 정보
info = {
    'ISTJ': {
        'title': '📘 ISTJ – 현실적이고 철저한 계획러',
        'description': '''
**성향**: 신중하고 논리적이며 책임감이 강해요. 계획을 세우고 지키는 데 능숙하며, 혼자 조용히 일하는 걸 선호하죠.

**공부 취향/특성**:
- 구조화된 학습을 좋아함
- 예측 가능한 루틴에 편안함
- 세부사항을 잘 기억함

**공부법**:
🗂️ **체계적인 계획 세우기**: 월간/주간 계획표를 만들어 정해진 시간에 공부하기  
🧾 **체크리스트 작성**: 목표 달성 후 체크하는 게 동기부여에 도움  
🔁 **반복 학습 & 요약 노트**: 복습과 정리된 문서가 큰 도움이 돼요  
🔗 추천 사이트: [Khan Academy](https://www.khanacademy.org)
'''
    },
    'ISFJ': {
        'title': '🌿 ISFJ – 조용한 헌신가, 정성 가득한 학습러',
        'description': '''
**성향**: 차분하고 성실해요. 남을 배려하고, 책임감 있게 자기 할 일을 해내는 스타일이에요.

**공부 취향/특성**:
- 익숙한 환경에서의 학습을 선호
- 감정적 안정이 중요
- 노트 필기와 정리가 뛰어남

**공부법**:
📚 **정리 중심의 필기**: 정보를 시각적으로 정리하면 기억에 오래 남아요  
🧘 **조용한 환경에서의 몰입**: 백색소음이나 카페보다는 방해 없는 공간 추천  
👩‍🏫 **누군가에게 설명하듯 공부**: 설명하면서 이해도를 높일 수 있어요  
🔗 추천 사이트: [StudyTubers](https://www.youtube.com/results?search_query=studytubers)
'''
    },
    'INFJ': {
        'title': '🔮 INFJ – 통찰력 깊은 전략가',
        'description': '''
**성향**: 조용하면서도 목표 지향적. 깊은 이해를 추구하고, 혼자서 몰입하는 시간이 중요해요.

**공부 취향/특성**:
- 혼자 집중할 수 있는 환경 선호
- 의미 있는 내용에 몰입
- 창의적인 방식으로 지식 구성

**공부법**:
🌀 **마인드맵 활용**: 전체 흐름을 파악하고 연결 지점을 시각화  
🕯️ **감성적인 요소 활용**: 예쁜 필기, 감각적인 학습 환경이 동기 자극  
📖 **깊이 있는 탐구**: 한 주제를 깊게 파고드는 ‘탐험형’ 공부 추천  
🔗 추천 사이트: [Coursera](https://www.coursera.org)
'''
    },
    'INTJ': {
        'title': '🧠 INTJ – 전략적인 마스터마인드',
        'description': '''
**성향**: 목표 달성에 집중하며 분석적이고 독립적이에요. 시스템적으로 생각하고 빠르게 학습합니다.

**공부 취향/특성**:
- 자기 주도 학습에 능숙
- 효율성과 생산성을 중시
- 장기적 목표를 세우고 추진

**공부법**:
📊 **목표를 쪼개기**: 큰 목표를 분할해 체계적으로 접근  
🧩 **구조 파악 및 논리 전개**: 개념 간의 연관성을 파악하면 이해가 빨라요  
💼 **생산성 도구 활용**: 타이머, 플래너 앱 적극 활용  
🔗 추천 사이트: [edX](https://www.edx.org)
'''
    },
    # 이하 나머지 MBTI도 유사한 형식으로 추가 가능
}

# 출력
if selected:
    st.markdown(f"### {info[selected]['title']}")
    st.markdown(info[selected]['description'])

    st.balloons()  # 효과

