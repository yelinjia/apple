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
    "Saudi Aramco": "2222.SR",
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
    close = df["Close"]
    if percent:
        change = close.pct_change() * 100  # 퍼센트 변화율
    else:
        change = close.diff()  # 절대 변화량
    return change.dropna()

# Plotly 그래프 초기화
fig = go.Figure()

for name, ticker in top10_companies.items():
    try:
        changes = fetch_daily_change(ticker, percent=(view_option == "변화율 (%)"))
        fig.add_trace(go.Scatter(
            x=changes.index,
            y=changes.values,
            mode="lines",
            name=name
        ))
    except Exception as e:
        st.warning(f"{name} 데이터 로딩 실패: {e}")

# y축 단위
y_label = "일일 변화율 (%)" if view_option == "변화율 (%)" else "일일 변화량 (USD)"

# 그래프 레이아웃
fig.update_layout(
    title=f"Top 10 기업의 하루하루 주가 {y_label}",
    xaxis_title="날짜",
    yaxis_title=y_label,
    hovermode="x unified",
    template="plotly_white",
    height=600,
    legend=dict(orientation="h", y=-0.2)
)

st.plotly_chart(fig, use_container_width=True)
