import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="가위바위보 카드게임", page_icon="🃏", layout="centered")

st.title("🃏 가위바위보 카드게임")
st.write("카드를 선택하면 컴퓨터와 대결합니다. 승률과 결과가 아래에 표시됩니다.")

# 초기 세션 상태 설정
if 'game_log' not in st.session_state:
    st.session_state.game_log = []
if 'win' not in st.session_state:
    st.session_state.win = 0
if 'draw' not in st.session_state:
    st.session_state.draw = 0
if 'lose' not in st.session_state:
    st.session_state.lose = 0
if 'round' not in st.session_state:
    st.session_state.round = 1

# 선택지
choices = ["가위", "바위", "보"]
emoji_map = {"가위": "✌️", "바위": "✊", "보": "✋"}

def get_result(player, computer):
    if player == computer:
        return "무승부"
    elif (player == "가위" and computer == "보") or \
         (player == "바위" and computer == "가위") or \
         (player == "보" and computer == "바위"):
        return "승리"
    else:
        return "패배"

# 카드 선택
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("✌️ 가위"):
        player_choice = "가위"
with col2:
    if st.button("✊ 바위"):
        player_choice = "바위"
with col3:
    if st.button("✋ 보"):
        player_choice = "보"

# 게임 실행
if 'player_choice' in locals():
    computer_choice = random.choice(choices)
    result = get_result(player_choice, computer_choice)

    # 결과 저장
    st.session_state.game_log.append({
        "회차": st.session_state.round,
        "플레이어": player_choice,
        "컴퓨터": computer_choice,
        "결과": result
    })
    st.session_state.round += 1

    if result == "승리":
        st.session_state.win += 1
    elif result == "무승부":
        st.session_state.draw += 1
    else:
        st.session_state.lose += 1

    # 애니메이션 느낌 연출
    st.markdown(f"""
    <div style="font-size:30px; text-align:center; margin-top:20px;">
        당신의 카드: {emoji_map[player_choice]} &nbsp;&nbsp;&nbsp; VS &nbsp;&nbsp;&nbsp; 컴퓨터: {emoji_map[computer_choice]}
    </div>
    <div style="font-size:24px; text-align:center; color:#007ACC; margin-top:10px;">
        결과: <strong>{result}</strong>
    </div>
    """, unsafe_allow_html=True)

# 결과표 출력
if st.session_state.game_log:
    st.subheader("📋 게임 기록")
    df = pd.DataFrame(st.session_state.game_log)
    st.dataframe(df, use_container_width=True)

    total_games = len(df)
    if total_games > 0:
        win_rate = (st.session_state.win / total_games) * 100
        st.metric("🏆 승률", f"{win_rate:.2f}%")

        col_w, col_d, col_l = st.columns(3)
        col_w.metric("✅ 승", st.session_state.win)
        col_d.metric("➖ 무", st.session_state.draw)
        col_l.metric("❌ 패", st.session_state.lose)

# 리셋 버튼
if st.button("🔄 전체 초기화"):
    st.session_state.game_log = []
    st.session_state.win = 0
    st.session_state.draw = 0
    st.session_state.lose = 0
    st.session_state.round = 1
    st.success("게임 데이터가 초기화되었습니다!")

