import streamlit as st
import random
import time

# 기본 세션 상태 초기화
if "round" not in st.session_state:
    st.session_state.round = 0
if "user_choice" not in st.session_state:
    st.session_state.user_choice = None
if "ai_choice" not in st.session_state:
    st.session_state.ai_choice = None
if "results" not in st.session_state:
    st.session_state.results = []  # [(user, ai, result)]
if "game_state" not in st.session_state:
    st.session_state.game_state = "start"  # start, countdown, result
if "count" not in st.session_state:
    st.session_state.count = 3

# 가위바위보 이모지 맵핑
emoji_map = {
    "가위": "✌️",
    "바위": "✊",
    "보": "✋"
}

choices = ["가위", "바위", "보"]

# 승부 계산 함수
def get_winner(user, ai):
    if user == ai:
        return "무승부"
    elif (user == "가위" and ai == "보") or \
         (user == "바위" and ai == "가위") or \
         (user == "보" and ai == "바위"):
        return "유저 승"
    else:
        return "AI 승"

# 승률 계산 함수
def calc_win_rate(user_choice):
    if not st.session_state.results:
        return 0.0
    total = 0
    wins = 0
    for u, a, result in st.session_state.results:
        if u == user_choice:
            total += 1
            if result == "유저 승":
                wins += 1
    return wins / total if total > 0 else 0.0

# AI가 낼 확률(랜덤이지만 지금까지 유저선택 대비 예상승률 계산해서 표시)
def calc_expected_win_rate(user_choice):
    # AI가 랜덤이라고 가정
    # 실제로는 AI가 1/3씩 낼거라 승률은 가위,바위,보 조합 평균
    win_count = 0
    for ai_choice in choices:
        result = get_winner(user_choice, ai_choice)
        if result == "유저 승":
            win_count += 1
    return win_count / 3

# 게임 초기화 함수
def reset_game():
    st.session_state.round = 0
    st.session_state.user_choice = None
    st.session_state.ai_choice = None
    st.session_state.results = []
    st.session_state.game_state = "start"
    st.session_state.count = 3

st.title("🎮 가위바위보 카드게임 with 승률 & 카운트다운")

# 초기화 버튼 - 항상 상단에 표시
if st.button("🔄 초기화 (완전 리셋)"):
    reset_game()
    st.experimental_rerun()

st.write(f"현재 라운드: {st.session_state.round}")

# 게임 상태에 따라 화면 분기

if st.session_state.game_state == "start":
    st.write("가위, 바위, 보 중에서 선택하세요.")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button(f"가위 {emoji_map['가위']}"):
            st.session_state.user_choice = "가위"
            st.session_state.count = 3
            st.session_state.game_state = "countdown"
            st.experimental_rerun()
    with col2:
        if st.button(f"바위 {emoji_map['바위']}"):
            st.session_state.user_choice = "바위"
            st.session_state.count = 3
            st.session_state.game_state = "countdown"
            st.experimental_rerun()
    with col3:
        if st.button(f"보 {emoji_map['보']}"):
            st.session_state.user_choice = "보"
            st.session_state.count = 3
            st.session_state.game_state = "countdown"
            st.experimental_rerun()

    # 각 선택지별 예상 승률 표시 (초기에는 AI가 랜덤 1/3 확률)
    st.markdown("### 예상 승률 (각 선택지 선택시 승률)")
    for c in choices:
        rate = calc_expected_win_rate(c) * 100
        st.write(f"{emoji_map[c]} {c}: 약 {rate:.1f}% 승률")

elif st.session_state.game_state == "countdown":
    st.markdown(f"<h1 style='text-align:center; font-size:100px'>{st.session_state.count}</h1>", unsafe_allow_html=True)
    st.write("결과가 곧 나옵니다...")

    if st.button("▶ 다음"):
        st.session_state.count -= 1
        if st.session_state.count == 0:
            st.session_state.ai_choice = random.choice(choices)
            st.session_state.game_state = "result"
        st.experimental_rerun()

elif st.session_state.game_state == "result":
    st.markdown("<h1 style='text-align:center; font-size:80px;'>결과</h1>", unsafe_allow_html=True)
    # 선택 이모지로 크게 보여주기
    st.markdown(f"<h2 style='text-align:center;'>당신: {emoji_map[st.session_state.user_choice]} ({st.session_state.user_choice})</h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center;'>AI: {emoji_map[st.session_state.ai_choice]} ({st.session_state.ai_choice})</h2>", unsafe_allow_html=True)

    # 승부 결과
    result = get_winner(st.session_state.user_choice, st.session_state.ai_choice)
    st.markdown(f"<h2 style='text-align:center; color: blue;'>{result}</h2>", unsafe_allow_html=True)

    # 결과 기록 저장
    st.session_state.results.append((st.session_state.user_choice, st.session_state.ai_choice, result))
    st.session_state.round += 1

    # 전체 결과 표 출력
    st.markdown("### 게임 기록")
    import pandas as pd
    df = pd.DataFrame(st.session_state.results, columns=["유저 선택", "AI 선택", "결과"])
    # 선택지 이모지 함께 표시
    df["유저 선택"] = df["유저 선택"].map(lambda x: f"{emoji_map[x]} {x}")
    df["AI 선택"] = df["AI 선택"].map(lambda x: f"{emoji_map[x]} {x}")
    st.table(df)

    # 다음 게임에서 각 선택지 선택 시 예상 승률 출력
    st.markdown("### 다음 게임 예상 승률")
    for c in choices:
        rate = calc_win_rate(c) * 100
        st.write(f"{emoji_map[c]} {c}: 현재 승률 약 {rate:.1f}%")

    # 버튼으로 다음 게임 시작
    if st.button("▶ 다음 게임"):
        st.session_state.user_choice = None
        st.session_state.ai_choice = None
        st.session_state.game_state = "start"
        st.experimental_rerun()
