import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="AI Pro Platform", layout="wide")

st.title("🚀 AI Trading Academy & Live Platform")
st.write("Track Live Markets & Practice Trading with Free $10,000 Demo Account!")

if "demo_balance" not in st.session_state:
    st.session_state.demo_balance = 10000.00

st.markdown(f"### 🎮 Demo Balance: **${st.session_state.demo_balance:,.2f}**")

t_trade, t_learn, t_real = st.tabs(["🎮 Demo Platform", "📚 Learn & AI Signals", "💰 Real Money"])

with t_trade:
    c_chart, c_panel = st.columns([2.5, 1])
    with c_chart:
        tv_html = """<div style="height:400px;width:100%"><div id="tv_chart" style="height:100%;width:100%"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"autosize":true,"symbol":"NSE:BANKNIFTY","interval":"5","theme":"dark","style":"1","locale":"en","allow_symbol_change":true,"container_id":"tv_chart"});</script></div>"""
        components.html(tv_html, height=410)
    with c_panel:
        asset = st.selectbox("Asset", ["Bank Nifty", "Bitcoin (BTC)", "Nifty 50"])
        direction = st.radio("Prediction", ["🟢 CALL (UP)", "🔴 PUT (DOWN)"])
        amount = st.number_input("Investment ($)", min_value=10, value=100)
        if st.button("Execute Demo Trade", use_container_width=True):
            if amount > st.session_state.demo_balance: 
                st.error("Insufficient Balance!")
            else:
                st.session_state.demo_balance -= amount
                st.success("Trade Executed!")

with t_learn:
    st.write("Market upar jane par CALL aur niche girne par PUT select karein.")
    gauge_html = """<script src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>{"interval":"1m","width":"100%","height":300,"symbol":"NSE:BANKNIFTY","showIntervalTabs":false,"displayMode":"single","locale":"en","theme":"dark"}</script>"""
    components.html(gauge_html, height=310)

with t_real:
    st.write("Ready for real profits? Route trades safely through licensed partners.")
    st.write("1. Trade on Indian Stocks (Groww/AngelOne)")
    st.write("2. Trade on Crypto (Binance)")

st.markdown("---")
st.caption("Platform v4.4 - Plain Text Safe Build")
