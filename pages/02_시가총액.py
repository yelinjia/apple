import streamlit as st
import plotly.express as px
import pandas as pd
import datetime

st.set_page_config(page_title="Top 10 시가총액 변화", layout="wide")

st.title("📈 전 세계 시가총액 TOP 10 기업의 3년간 변화")

# 샘플 데이터 (실제 데이터를 원한다면 웹에서 최신 데이터를 수집하거나 API를 사용하세요)
# 아래는 예시를 위해 하드코딩된 데이터입니다.
data = {
    "Company": ["Apple", "Microsoft", "Saudi Aramco", "Alphabet", "Amazon", "Nvidia", "Berkshire Hathaway", "Meta", "Tesla", "TSMC"] * 3,
    "Year": [2023]*10 + [2024]*10 + [2025]*10,
    "Market Cap (Trillion USD)": [
        2.5, 2.1, 2.0, 1.6, 1.3, 0.9, 0.8, 0.7, 0.6, 0.5,
        2.8, 2.3, 2.1, 1.8, 1.4, 1.2, 0.9, 0.8, 0.7, 0.6,
        3.1, 2.6, 2.4, 2.0, 1.6, 1.5, 1.0, 0.9, 0.75, 0.65
    ]
}

df = pd.DataFrame(data)

# Plotly 그래프
fig = px.line(
    df,
    x="Year",
    y="Market Cap (Trillion USD)",
    color="Company",
    markers=True,
    title="Top 10 기업 시가총액 변화 (2023–2025)",
)

fig.update_layout(
    hovermode="x unified",
    xaxis=dict(dtick=1),
    yaxis_title="시가총액 (조 달러)",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)
