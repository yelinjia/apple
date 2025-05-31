import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Top 10 주가 일일 변화율", layout="wide")
st.title("📉 시가총액 Top 10 기업의 하루하루 주가 변화율")

# 기업 리스트
top10_companies = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    # "Saudi Aramco": "2222.SR",  # 제외: 데이터 자주 실패
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Berkshire Hathaway": "BRK-B",
    "Meta Platforms": "META",
    "Eli Lilly": "LLY",
    "TSMC": "TSM"
}

# 날짜 설정
end_date = datetime.today()
start_date = end_date - timedelta(days=3 * 365)

# 선택 옵션
view_option = st.selectbox("변화 기준을 선택하세요:", ["변화율 (%)", "절대 변화량 (USD)"])

@st.cache_data
def fetch_daily_change(ticker, percent=True):
    df = yf.download(ticker, start=start_date, end=end_date)
    if df.empty or "Close" not in df.columns:
        return None
    close = df["Close"]
    if percent:
        change = close.pct_change() * 100
    else:
        change = close.diff()
    return change.dropna()

# Plotly 그래프 초기화
fig = go.Figure()
data_loaded = False  # 그래프 추가 여부 체크

# 데이터 로딩 메시지
with st.spinner("📊 데이터를 불러오는 중입니다..."):
    for name, ticker in top10_companies.items():
        changes = fetch_daily_change(ticker, percent=(view_option == "변화율 (%)"))
        if changes is not None:
            fig.add_trace(go.Scatter(
                x=changes.index,
                y=changes.values,
                mode="lines",
                name=name
            ))
            data_loaded = True
        else:
            st.warning(f"⚠️ {name} ({ticker}) 데이터 불러오기 실패")

# 그래프 레이아웃 설정
y_label = "일일 변화율 (%)" if view_option == "변화율 (%)" else "일일 변화량 (USD)"
fig.update_layout(
    title=f"Top 10 기업의 하루하루 주가 {y_label}",
    xaxis_title="날짜",
    yaxis_title=y_label,
    hovermode="x unified",
    template="plotly_white",
    height=600,
    legend=dict(orientation="h", y=-0.2)
)

# 그래프 출력
if data_loaded:
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("😢 불러온 데이터가 없어 그래프를 표시할 수 없습니다.")
