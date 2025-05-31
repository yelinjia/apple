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

if "game_state" not in st.session_state:
    # game_state: "select" (플레이어 선택), "countdown", "result"
    st.session_state.game_state = "select"
if "user_choice" not in st.session_state:
    st.session_state.user_choice = None
if "ai_choice" not in st.session_state:
    st.session_state.ai_choice = None

st.set_page_config(page_title="가위바위보 카드게임", layout="centered")
st.title("✊✌️✋ 가위바위보 카드게임")
st.markdown(f"### 🎯 현재 라운드: {st.session_state.round}")

choices = ["가위", "바위", "보"]

# --- AI 선택 통계 ---
def get_ai_prediction_stats(results):
    counts = {"가위": 0, "바위": 0, "보": 0}
    for result in results:
        counts[result["AI"]] += 1
    total = sum(counts.values())
    if total == 0:
        return {k: 33.3 for k in counts}
    return {k: round((v / total) * 100, 1) for k, v in counts.items()}

ai_stats = get_ai_prediction_stats(st.session_state.results)

# --- 다음 선택별 예상 승률 ---
def calc_win_prob(choice, ai_stats):
    # 내가 선택한 카드가 이기는 AI 카드 확률
    win_against = {"가위": "보", "바위": "가위", "보": "바위"}
    return ai_stats.get(win_against[choice], 0)

# --- 화면 그리기 ---

if st.session_state.game_state == "select":
    st.markdown("#### 당신의 선택을 골라주세요:")
    user_choice = st.radio("", choices, horizontal=True)

    # 다음 선택 승률 표시
    st.markdown("#### 🤖 다음 선택 승률 예측")
    col1, col2, col3 = st.columns(3)
    for i, c in enumerate(choices):
        with [col1, col2, col3][i]:
            prob = calc_win_prob(c, ai_stats)
            st.metric(label=c, value=f"{prob}% 승률")

    if st.button("▶️ 선택 완료"):
        st.session_state.user_choice = user_choice
        st.session_state.game_state = "countdown"
        st.experimental_rerun()

elif st.session_state.game_state == "countdown":
    placeholder = st.empty()
    for i in ["3", "2", "1"]:
        placeholder.markdown(f"<h1 style='text-align:center;'>{i}</h1>", unsafe_allow_html=True)
        time.sleep(1)
    placeholder.empty()

    # AI 선택
    st.session_state.ai_choice = random.choice(choices)
    st.session_state.game_state = "result"
    st.experimental_rerun()

elif st.session_state.game_state == "result":
    user = st.session_state.user_choice
    ai = st.session_state.ai_choice

    st.markdown(f"### 당신 선택: **{user}**")
    st.markdown(f"<h2 style='color:#FF4B4B; text-align:center;'>🤖 AI 선택: <b style='font-size:40px;'>{ai}</b></h2>", unsafe_allow_html=True)

    # 승패 판단
    if user == ai:
        result = "무승부"
        st.session_state.draw += 1
    elif (user == "가위" and ai == "보") or (user == "바위" and ai == "가위") or (user == "보" and ai == "바위"):
        result = "승리"
        st.session_state.win += 1
    else:
        result = "패배"
        st.session_state.lose += 1

    st.success(f"💥 결과: {result}!")

    # 기록 저장
    st.session_state.results.append({
        "라운드": st.session_state.round,
        "플레이어": user,
        "AI": ai,
        "결과": result
    })

    # 통계표 표시
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

    # 다음 선택 승률 다시 계산 (새로운 결과 포함)
    ai_stats = get_ai_prediction_stats(st.session_state.results)
    st.markdown("#### 🤖 다음 선택 승률 예측")
    col1, col2, col3 = st.columns(3)
    for i, c in enumerate(choices):
        with [col1, col2, col3][i]:
            prob = calc_win_prob(c, ai_stats)
            st.metric(label=c, value=f"{prob}% 승률")

    # 다음 게임 버튼
    if st.button("➡️ 다음 게임"):
        st.session_state.round += 1
        st.session_state.game_state = "select"
        st.session_state.user_choice = None
        st.session_state.ai_choice = None
        st.experimental_rerun()

# --- 리셋 버튼은 항상 표시 ---
st.markdown("---")
if st.button("🔄 전체 리셋"):
    for key in ["round", "results", "win", "draw", "lose", "game_state", "user_choice", "ai_choice"]:
        if key == "results":
            st.session_state[key] = []
        elif key == "game_state":
            st.session_state[key] = "select"
        else:
            st.session_state[key] = 0 if key == "round" else None
    st.experimental_rerun()
