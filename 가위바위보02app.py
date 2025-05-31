import streamlit as st
import random
import pandas as pd

# 세션 상태 초기화
if "round" not in st.session_state:
    st.session_state.round = 0
if "user_choice" not in st.session_state:
    st.session_state.user_choice = None
if "ai_choice" not in st.session_state:
    st.session_state.ai_choice = None
if "results" not in st.session_state:
    st.session_state.results = []
if "game_state" not in st.session_state:
    st.session_state.game_state = "start"  # start, countdown, result
if "count" not in st.session_state:
    st.session_state.count = 3

emoji_map = {"가위": "✌️", "바위": "✊", "보": "✋"}
choices = list(emoji_map.keys())

def get_winner(user, ai):
    if user == ai:
        return "무승부"
    elif (user == "가위" and ai == "보") or \
         (user == "바위" and ai == "가위") or \
         (user == "보" and ai == "바위"):
        return "유저 승"
    else:
        return "AI 승"

def calc_win_rate(user_choice):
    total = sum(1 for u, a, r in st.session_state.results if u == user_choice)
    if total == 0:
        return 0.0
    wins = sum(1 for u, a, r in st.session_state.results if u == user_choice and r == "유저 승")
    return wins / total

def calc_expected_win_rate(user_choice):
    # AI가 랜덤이지만 승률 예상 (이론상 승률은 1/3)
    win_count = 0
    for ai_choice in choices:
        if get_winner(user_choice, ai_choice) == "유저 승":
            win_count += 1
    return win_count / len(choices)

def reset_game():
    st.session_state.round = 0
    st.session_state.user_choice = None
    st.session_state.ai_choice = None
    st.session_state.results = []
    st.session_state.game_state = "start"
    st.session_state.count = 3

st.title("🎮 가위바위보 카드게임 with 승률 & 카운트다운")

if st.button("🔄 초기화 (완전 리셋)"):
    reset_game()
    st.experimental_rerun()

st.write(f"현재 라운드: {st.session_state.round}")

if st.session_state.game_state == "start":
    st.write("가위, 바위, 보 중에서 선택하세요.")
    cols = st.columns(3)
    for i, c in enumerate(choices):
        if cols[i].button(f"{emoji_map[c]} {c}"):
            st.session_state.user_choice = c
            st.session_state.count = 3
            st.session_state.game_state = "countdown"
            st.experimental_rerun()

    st.markdown("### 예상 승률 (각 선택지 선택 시)")
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
    user = st.session_state.user_choice
    ai = st.session_state.ai_choice
    result = get_winner(user, ai)

    st.markdown("<h1 style='text-align:center; font-size:80px;'>결과</h1>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center;'>당신: {emoji_map[user]} ({user})</h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center;'>AI: {emoji_map[ai]} ({ai})</h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center; color: blue;'>{result}</h2>", unsafe_allow_html=True)

    # 기록 저장
    st.session_state.results.append((user, ai, result))
    st.session_state.round += 1

    st.markdown("### 게임 기록")
    df = pd.DataFrame(st.session_state.results, columns=["유저 선택", "AI 선택", "결과"])
    df["유저 선택"] = df["유저 선택"].map(lambda x: f"{emoji_map[x]} {x}")
    df["AI 선택"] = df["AI 선택"].map(lambda x: f"{emoji_map[x]} {x}")
    st.table(df)

    st.markdown("### 다음 게임 예상 승률")
    for c in choices:
        rate = calc_win_rate(c) * 100
        st.write(f"{emoji_map[c]} {c}: 현재 승률 약 {rate:.1f}%")

    if st.button("▶ 다음 게임"):
        st.session_state.user_choice = None
        st.session_state.ai_choice = None
        st.session_state.game_state = "start"
        st.session_state.count = 3
        st.experimental_rerun()

