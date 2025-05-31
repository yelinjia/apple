import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

# 시가총액 기준 TOP10 기업 (2025년 기준 추정)
TICKERS = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Saudi Aramco': '2222.SR',
    'Alphabet (Google)': 'GOOGL',
    'Amazon': 'AMZN',
    'Nvidia': 'NVDA',
    'Berkshire Hathaway': 'BRK-B',
    'Meta': 'META',
    'Tesla': 'TSLA',
    'TSMC': 'TSM'
}

st.title("📈 전 세계 시가총액 Top 10 기업 - 최근 3년간 주가 변화")

# 기간 설정
end_date = datetime.now()
start_date = end_date - timedelta(days=3*365)

# 사용자 멀티 선택
selected_companies = st.multiselect(
    "기업 선택", options=list(TICKERS.keys()), default=list(TICKERS.keys())[:5]
)

if selected_companies:
    fig = go.Figure()

    for company in selected_companies:
        ticker = TICKERS[company]
        data = yf.download(ticker, start=start_date, end=end_date)
        
        if not data.empty:
            fig.add_trace(go.Scatter(
                x=data.index, y=data['Adj Close'],
                mode='lines', name=company
            ))
        else:
            st.warning(f"{company}의 데이터를 불러올 수 없습니다.")

    fig.update_layout(
        title="주가 추이 (최근 3년)",
        xaxis_title="날짜",
        yaxis_title="조정 종가 (USD)",
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("왼쪽에서 하나 이상의 기업을 선택하세요.")
