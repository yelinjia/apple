import streamlit as st

st.set_page_config(page_title="MBTI 공부법 가이드", page_icon="🧠", layout="centered")

st.markdown("<h1 style='text-align:center;'>📚 MBTI별 맞춤 시험 공부법 가이드 📚</h1>", unsafe_allow_html=True)
st.markdown("👉 당신의 MBTI를 선택하면, 성격에 딱 맞는 공부법과 사이트를 추천해드려요!", unsafe_allow_html=True)

mbti_types = [
    'ISTJ', 'ISFJ', 'INFJ', 'INTJ',
    'ISTP', 'ISFP', 'INFP', 'INTP',
    'ESTP', 'ESFP', 'ENFP', 'ENTP',
    'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ'
]

mbti = st.selectbox("🧬 당신의 MBTI는?", mbti_types)

mbti_info = {
    'ISTJ': {
        'title': '📘 ISTJ – 현실적이고 철저한 계획러',
        'desc': '''
**성향**: 신중하고 체계적이며 책임감이 강한 유형으로, 질서와 안정감을 선호합니다.

**시험공부법**:
✅ 세부 계획표를 만들고 철저히 실천  
✅ 핵심 요약 노트를 만들어 반복 복습  
✅ 실전 모의고사로 시험 감각 훈련  

🔗 추천 사이트: [Khan Academy](https://www.khanacademy.org)
'''
    },
    'ISFJ': {
        'title': '🧾 ISFJ – 따뜻한 조력자',
        'desc': '''
**성향**: 성실하고 조용하며 타인을 돕는 걸 좋아합니다. 감정적으로 안정된 환경을 선호하죠.

**시험공부법**:
✅ 조용한 공간에서 차근차근 정리  
✅ 마인드맵 또는 손 필기 활용  
✅ 친절한 설명 강의로 감정적 연결 형성  

🔗 추천 사이트: [StudyTubers 유튜브](https://www.youtube.com/results?search_query=studytuber)
'''
    },
    'INFJ': {
        'title': '🔮 INFJ – 직관적인 이상주의자',
        'desc': '''
**성향**: 통찰력 있고 분석적인 사고를 선호. 목표에 깊은 의미를 부여하는 타입입니다.

**시험공부법**:
✅ 혼자 있는 시간 확보  
✅ 주제를 깊이 파고들며 전체 구조 파악  
✅ 창의적인 시각 자료(그림, 스토리 등) 활용  

🔗 추천 사이트: [Coursera](https://www.coursera.org)
'''
    },
    'INTJ': {
        'title': '🧠 INTJ – 전략적 마스터마인드',
        'desc': '''
**성향**: 독립적이고 목표 지향적. 효율성과 논리적인 구조를 중시합니다.

**시험공부법**:
✅ 장기 계획 수립 후 전략적 분할  
✅ 이해 > 암기, 원리 위주 학습  
✅ 타이머 앱으로 집중 시간 설정  

🔗 추천 사이트: [edX](https://www.edx.org)
'''
    },
    'ISTP': {
        'title': '🛠 ISTP – 문제 해결의 달인',
        'desc': '''
**성향**: 실용적이고 관찰력이 뛰어나며 손으로 직접 해결하는 걸 좋아합니다.

**시험공부법**:
✅ 문제를 직접 풀면서 원리 익히기  
✅ 실전 연습 위주 (문제 → 해설 → 반복)  
✅ 짧은 시간 집중 → 자주 휴식  

🔗 추천 사이트: [Project Euler](https://projecteuler.net)
'''
    },
    'ISFP': {
        'title': '🎨 ISFP – 감각적인 아티스트',
        'desc': '''
**성향**: 조용하고 유연하며, 감성적이고 미적 요소에 민감합니다.

**시험공부법**:
✅ 예쁜 노트 정리, 시각화된 자료 활용  
✅ 자유로운 분위기에서 공부  
✅ 강제성보다 자율성 기반 학습  

🔗 추천 사이트: [Notion](https://www.notion.so)
'''
    },
    'INFP': {
        'title': '📖 INFP – 이상을 좇는 몽상가',
        'desc': '''
**성향**: 감정이입이 깊고 이상주의적이며 의미 있는 공부에 열정을 느낍니다.

**시험공부법**:
✅ 공부에 의미 부여 (왜 공부하는가?)  
✅ 좋아하는 스타일(영상, 글)로 시작  
✅ 이야기식 요약 노트 만들기  

🔗 추천 사이트: [TED Talks](https://www.ted.com)
'''
    },
    'INTP': {
        'title': '🔍 INTP – 논리적인 사색가',
        'desc': '''
**성향**: 분석적이고 호기심 많으며, 지적인 주제를 탐구하는 걸 즐깁니다.

**시험공부법**:
✅ 이론을 체계적으로 구조화  
✅ 개념 간 연결 → 전체 흐름 파악  
✅ 논리적으로 설명 가능한 수준까지  

🔗 추천 사이트: [Wikipedia](https://www.wikipedia.org)
'''
    },
    'ESTP': {
        'title': '🏃 ESTP – 즉흥적인 실행가',
        'desc': '''
**성향**: 활동적이고 도전적이며 문제 해결 능력이 뛰어납니다.

**시험공부법**:
✅ 실전 문제 → 바로 해설 반복  
✅ 속도감 있게 테스트하며 외우기  
✅ 스터디 그룹과 퀴즈로 학습  

🔗 추천 사이트: [Quizlet](https://quizlet.com)
'''
    },
    'ESFP': {
        'title': '🎤 ESFP – 감각적인 사교가',
        'desc': '''
**성향**: 외향적이고 에너제틱하며 사람과 소통을 즐깁니다.

**시험공부법**:
✅ 그룹 스터디, 스터디카페 활용  
✅ 영상, 오디오 자료로 감각적 학습  
✅ 이야기식 요약법 활용  

🔗 추천 사이트: [CrashCourse](https://www.youtube.com/user/crashcourse)
'''
    },
    'ENFP': {
        'title': '🌈 ENFP – 열정적인 아이디어 뱅크',
        'desc': '''
**성향**: 창의적이고 자유로운 학습자. 다양하고 새로운 아이디어를 좋아합니다.

**시험공부법**:
✅ 다양한 방식 시도 (플래너, 포스트잇 등)  
✅ 공부에 재미 요소 넣기 (퀴즈, 게임화)  
✅ 말하면서 정리하는 ‘자기 설명’ 방식  

🔗 추천 사이트: [Notion Template](https://www.notion.so)
'''
    },
    'ENTP': {
        'title': '🧪 ENTP – 호기심 많은 발명가',
        'desc': '''
**성향**: 토론과 질문을 즐기며 새로운 접근에 능합니다.

**시험공부법**:
✅ 여러 교재 비교하며 공부  
✅ 질문과 답변으로 내용 정리  
✅ 실생활 적용 방식으로 암기  

🔗 추천 사이트: [Brilliant](https://www.brilliant.org)
'''
    },
    'ESTJ': {
        'title': '📊 ESTJ – 조직적이고 실용적인 관리자',
        'desc': '''
**성향**: 실용적이고 논리적인 문제 해결을 선호. 명확한 기준과 체계 중시.

**시험공부법**:
✅ 타이트한 시간관리 + 정해진 루틴  
✅ 실전 문제 풀이 → 오답노트 작성  
✅ 그룹 내 리더 역할 수행하며 학습 주도  

🔗 추천 사이트: [StudyStack](https://www.studystack.com)
'''
    },
    'ESFJ': {
        'title': '🤝 ESFJ – 따뜻한 리더, 사교적 학습가',
        'desc': '''
**성향**: 배려심 많고 책임감 강하며, 사회적 상호작용을 중시합니다.

**시험공부법**:
✅ 누군가에게 설명하면서 학습  
✅ 체크리스트로 진행 관리  
✅ 공부 계획을 친구와 공유하며 동기 유지  

🔗 추천 사이트: [Study With Me 영상](https://www.youtube.com/results?search_query=study+with+me)
'''
    },
    'ENFJ': {
        'title': '🦸 ENFJ – 카리스마 있는 동기부여자',
        'desc': '''
**성향**: 리더십 강하며 사람들과의 유대가 동기부여의 원천입니다.

**시험공부법**:
✅ 스터디 그룹 운영하며 주도적 학습  
✅ 공부 목표를 시각적으로 정리  
✅ 성과 공유하며 동기 유지  

🔗 추천 사이트: [MindTools](https://www.mindtools.com)
'''
    },
    'ENTJ': {
        'title': '🏆 ENTJ – 목표 중심의 지휘관',
        'desc': '''
**성향**: 효율, 성과를 중시하는 타입. 리더십 강하고 도전 의식 높음.

**시험공부법**:
✅ 시간 관리 앱, 공부 타이머 적극 활용  
✅ 계획 → 실행 → 검토 루틴 반복  
✅ 공부 계획도 전략적으로 설계  

🔗 추천 사이트: [Trello](https://www.trello.com)
'''
    }
}

# 출력
if mbti in mbti_info:
    st.markdown(f"## {mbti_info[mbti]['title']}")
    st.markdown(mbti_info[mbti]['desc'])
    st.balloons()
else:
    st.warning("❌ 해당 MBTI 정보가 없습니다.")
