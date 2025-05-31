import streamlit as st
import random
import time
import pandas as pd

# --- 초기화 ---
if "round" not in st.session_state:
    st.session_state.round = 1
if "results" not in st.session_state:
    st.session_state.results = []
if "win" not in st.session_state:
    st.session_state.win = 0
if "draw" not in st.session_state:
    st.session_state.draw = 0
if "lose" not in st.session_state:
    st.session_state.lose = 0

st.set_page_config(page_title="가위바위보 카드게임", layout="centered")

st.title("✊✌️✋ 가위바위보 카드게임")
st.markdown(f"### 🎯 현재 라운드: {st.session_state.round}")

# --- 선택지 ---
choices = ["가위", "바위", "보"]
user_choice = st.radio("당신의 선택:", choices, horizontal=True)

# --- AI 전략 예측 ---
def get_ai_prediction_stats(results):
    counts = {"가위": 0, "바위": 0, "보": 0}
    for result in results:
        counts[result["AI"]] += 1
    total = sum(counts.values())
    if total == 0:
        return {k: 33.3 for k in counts}
    return {k: round((v / total) * 100, 1) for k, v in counts.items()}

ai_stats = get_ai_prediction_stats(st.session_state.results)

st.markdown("#### 🤖 다음 선택 승률 예측")
col1, col2, col3 = st.columns(3)
for i, choice in enumerate(choices):
    with [col1, col2, col3][i]:
        # 단순 확률 전략 (무작위 AI에 대한 이길 확률)
        win_against = {"가위": "보", "바위": "가위", "보": "바위"}
        win_prob = ai_stats[win_against[choice]]
        st.metric(label=choice, value=f"{win_prob}% 승률")

# --- 게임 실행 ---
if st.button("선택하고 대결하기"):
    with st.spinner("카운트다운 중..."):
        for i in ["3...", "2...", "1..."]:
            st.markdown(f"<h2 style='text-align:center;'>{i}</h2>", unsafe_allow_html=True)
            time.sleep(0.6)

    ai_choice = random.choice(choices)
    st.markdown(f"### 🤖 AI의 선택: **{ai_choice}**")

    if user_choice == ai_choice:
        result = "무승부"
        st.session_state.draw += 1
    elif (user_choice == "가위" and ai_choice == "보") or \
         (user_choice == "바위" and ai_choice == "가위") or \
         (user_choice == "보" and ai_choice == "바위"):
        result = "승리"
        st.session_state.win += 1
    else:
        result = "패배"
        st.session_state.lose += 1

    st.success(f"💥 결과: {result}!")

    st.session_state.results.append({
        "라운드": st.session_state.round,
        "플레이어": user_choice,
        "AI": ai_choice,
        "결과": result
    })
    st.session_state.round += 1

# --- 통계표 ---
if st.session_state.results:
    df = pd.DataFrame(st.session_state.results)
    st.markdown("### 📊 경기 결과 요약")
    st.dataframe(df, use_container_width=True)

    total_games = len(df)
    win = st.session_state.win
    draw = st.session_state.draw
    lose = st.session_state.lose
    win_rate = round((win / total_games) * 100, 1)

    st.markdown(f"#### 🧮 현재까지 전적: {win}승 / {draw}무 / {lose}패")
    st.metric(label="🏆 승률", value=f"{win_rate} %")

# --- 리셋 ---
if st.button("🔄 전체 리셋"):
    for key in ["round", "results", "win", "draw", "lose"]:
        st.session_state[key] = 0 if key != "results" else []
    st.experimental_rerun()
