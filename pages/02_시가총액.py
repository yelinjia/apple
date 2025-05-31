import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Top 10 Market Cap Trends", layout="wide")

st.title("📈 전세계 시가총액 Top 10 기업의 최근 3년 시가총액 변화")

# 시가총액 상위 10개 (2024년 기준 추정)
companies = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Saudi Aramco": "2222.SR",  # 사우디 거래소
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Berkshire Hathaway": "BRK-B",
    "Meta Platforms": "META",
    "TSMC": "TSM",
    "Tesla": "TSLA"
}

# 주식 수 (단위: 억 주), 실제는 변동 가능성이 있어 참고치로 사용
# yfinance는 실시간 outstanding shares를 제공하지 않으므로 일부는 고정 추정 사용
shares_outstanding = {
    "AAPL": 15.65e9,
    "MSFT": 7.42e9,
    "2222.SR": 219.0e9,
    "GOOGL": 12.46e9,
    "AMZN": 10.28e9,
    "NVDA": 2.47e9,
    "BRK-B": 2.20e9,
    "META": 2.55e9,
    "TSM": 5.18e9,
    "TSLA": 3.19e9
}

start_date = datetime.now() - timedelta(days=3*365)
end_date = datetime.now()

st.write("⏳ 데이터 로딩 중...")

@st.cache_data(ttl=3600)
def load_data():
    data = {}
    for name, symbol in companies.items():
        ticker = yf.Ticker(symbol)
        hist = ticker.history(start=start_date.strftime("%Y-%m-%d"), end=end_date.strftime("%Y-%m-%d"), interval="1mo")
        hist = hist[["Close"]].rename(columns={"Close": name})
        hist[name + "_MarketCap"] = hist[name] * shares_outstanding[symbol]
        data[name] = hist[[name + "_MarketCap"]]
    df = pd.concat(data.values(), axis=1)
    df.index = pd.to_datetime(df.index)
    return df

df = load_data()

# Plotly 그래프
fig = go.Figure()

for name in companies:
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df[f"{name}_MarketCap"] / 1e12,  # Trillions of USD
        mode='lines+markers',
        name=name
    ))

fig.update_layout(
    title="Top 10 시가총액 기업의 월별 시가총액 추이 (최근 3년)",
    xaxis_title="날짜",
    yaxis_title="시가총액 (조 달러)",
    hovermode="x unified",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)

