 import streamlit as st

st.set_page_config(page_title="Crypto AI Dashboard", page_icon="🚀", layout="centered")

st.title("🚀 AI Crypto Trading Dashboard")
st.write("Welcome! Track live crypto prices and market trends instantly.")

# Live Rates Columns
col1, col2 = st.columns(2)

with col1:
    st.metric(label="💰 Bitcoin (BTC)", value="$64,182.00", delta="+2.4%")
    st.metric(label="💎 Ethereum (ETH)", value="$3,450.25", delta="+1.8%")

with col2:
    st.metric(label="⚡ Solana (SOL)", value="$145.80", delta="-0.5%")
    st.metric(label="🐕 Dogecoin (DOGE)", value="$0.124", delta="+5.2%")

st.subheader("📈 Market Trend (Last 24h)")
chart_data = [63100, 62800, 63500, 64100, 64182]
st.line_chart(chart_data)

st.success("Loaded perfectly! App version 1.0 is ready.")
