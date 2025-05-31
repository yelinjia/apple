import streamlit as st
import random
import pandas as pd

# 초기화 함수
def reset_game():
    st.session_state.round = 0
    st.session_state.user_choice = None
    st.session_state.ai_choice = None
    st.session_state.results = []
    st.session_state.game_state = "start"
    st.session_state.count = 3

# 승자 계산 함수
def get_winner(user, ai):
    if user == ai:
        return "무승부"
    elif (user == "가위" and ai == "보") or \
         (user == "바위" and ai == "가위") or \
         (user == "보" and ai == "바위"):
        return "유저 승"
    else:
        return "AI 승"

emoji_map = {"가위": "✌️", "바위": "✊", "보": "✋"}
choices = list(emoji_map.keys())

# 세션 상태 초기화
if "round" not in st.session_state:
    reset_game()

st.title("🎮 가위바위보 카드게임")

# 초기화 버튼
if st.button("🔄 초기화 (완전 리셋)"):
    reset_game()

st.write(f"현재 라운드: {st.session_state.round}")

if st.session_state.game_state == "start":
    st.write("가위, 바위, 보 중에서 선택하세요.")
    cols = st.columns(3)
    for i, c in enumerate(choices):
        if cols[i].button(f"{emoji_map[c]} {c}"):
            st.session_state.user_choice = c
            st.session_state.count = 3
            st.session_state.game_state = "countdown"

elif st.session_state.game_state == "countdown":
    st.markdown(f"<h1 style='text-align:center; font-size:100px'>{st.session_state.count}</h1>", unsafe_allow_html=True)
    st.write("결과가 곧 나옵니다...")

    if st.button("▶ 다음"):
        st.session_state.count -= 1
        if st.session_state.count == 0:
            st.session_state.ai_choice = random.choice(choices)
            st.session_state.game_state = "result"

elif st.session_state.game_state == "result":
    user = st.session_state.user_choice
    ai = st.session_state.ai_choice
    result = get_winner(user, ai)

    st.markdown(f"### 당신: {emoji_map[user]} {user}")
    st.markdown(f"### AI: {emoji_map[ai]} {ai}")
    st.markdown(f"### 결과: **{result}**")

    # 기록 저장 (처음 한번만 추가)
    if len(st.session_state.results) == st.session_state.round:
        st.session_state.results.append((user, ai, result))
        st.session_state.round += 1

    st.markdown("### 기록")
    df = pd.DataFrame(st.session_state.results, columns=["유저 선택", "AI 선택", "결과"])
    df["유저 선택"] = df["유저 선택"].map(lambda x: f"{emoji_map[x]} {x}")
    df["AI 선택"] = df["AI 선택"].map(lambda x: f"{emoji_map[x]} {x}")
    st.table(df)

    if st.button("▶ 다음 게임"):
        st.session_state.user_choice = None
        st.session_state.ai_choice = None
        st.session_state.game_state = "start"
        st.session_state.count = 3
