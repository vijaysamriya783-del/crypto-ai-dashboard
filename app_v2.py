import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="AI Pro Animated Platform", page_icon="📈", layout="wide")

# Safe Single-line CSS Injection for Animations
st.markdown("<style>div[data-testid='stMetric'] { background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 12px; padding: 15px; transition: transform 0.3s ease; } div[data-testid='stMetric']:hover { transform: translateY(-5px); border: 1px solid #00d09c; }</style>", unsafe_allowed_html=True)
st.markdown("<style>div.stButton > button { background: linear-gradient(135deg, #00d09c 0%, #009a73 100%) !important; color: white !important; border-radius: 8px !important; font-weight: bold !important; box-shadow: 0 4px 15px rgba(0, 208, 156, 0.3) !important; }</style>", unsafe_allowed_html=True)

st.title("🚀 AI Trading Academy & Live Platform")
st.write("Track Live Stocks, Bank Nifty, Sensex & Crypto Markets with Free $10,000 Demo Account!")

# --- STATE MANAGEMENT ---
if "demo_balance" not in st.session_state:
    st.session_state.demo_balance = 10000.00
if "trades_history" not in st.session_state:
    st.session_state.trades_history = []

# Top Header Stats
col_h1, col_h2, col_h3 = st.columns(3)
with col_h1:
    st.markdown(f"### 🎮 Demo Balance: **${st.session_state.demo_balance:,.2f}**")
with col_h2:
    st.success("🟢 Real Account Routing: Active")
with col_h3:
    st.metric(label="📊 Live Overview (Search Enabled Below)", value="All Markets Active", delta="Live")

st.markdown("---")

# Main Tabs
tab_trade, tab_learn, tab_real = st.tabs(["🎮 Demo Trading Platform", "📚 Learn Trading & AI Signals", "💰 Real Money Trading"])

with tab_trade:
    col_chart, col_panel = st.columns([2.5, 1])
    
    with col_chart:
        st.subheader("📊 Live Market Advanced Chart (Search Any Stock/Sensex/Crypto)")
        # Full trading view widget that tracks EVERYTHING
        tradingview_html = """
        <div class="tradingview-widget-container" style="height:420px;width:100%">
          <div id="tv_main_chart" style="height:100%;width:100%"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
          <script type="text/javascript">
          new TradingView.widget({
            "autosize": true,
            "symbol": "NSE:BANKNIFTY",
            "interval": "5",
            "theme": "dark",
            "style": "1",
            "locale": "en",
            "allow_symbol_change": true,
            "container_id": "tv_main_chart"
          });
          </script>
        </div>
        """
        components.html(tradingview_html, height=430)
        st.info("💡 Tip: Chart ke upar click karke aap SENSEX, NIFTY, ya kisi bhi Crypto/Stock ka naam search karke live dekh sakte hain!")
        
    with col_panel:
        st.subheader("Place Practice Trade")
        asset = st.selectbox("Select Market Asset", ["Bank Nifty", "Bitcoin (BTC)", "Nifty 50", "Sensex"])
        direction = st.radio("Prediction", ["🟢 CALL (Goes UP)", "🔴 PUT (Goes DOWN)"])
        amount = st.number_input("Investment ($)", min_value=10, max_value=5000, value=100)
        
        if st.button("Execute Demo Trade", use_container_width=True):
            if amount > st.session_state.demo_balance:
                st.error("Insufficient Demo Balance!")
            else:
                st.session_state.demo_balance -= amount
                dir_text = "UP" if "CALL" in direction else "DOWN"
                st.session_state.trades_history.append(f"Invested ${amount} on {asset} predicting {dir_text}")
                st.success("Demo Trade Executed Successfully!")

with tab_learn:
    st.subheader("📚 Quick Financial Education")
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        st.info("### 🟢 Call & Put Strategy")
        st.write("Market trend upar jane par CALL aur niche girne par PUT se practice karein.")
        st.warning("### 📉 2% Golden Rule")
        st.write("Kabhi bhi ek single trade mein balance ka 2% se zyada risk na lein.")
    with col_l2:
        st.success("### 🤖 Live Technical Gauge Analysis")
        gauge_html = """
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
        {"interval": "1m", "width": "100%", "isTransparent": false, "height": 300, "symbol": "NSE:BANKNIFTY", "showIntervalTabs": false, "displayMode": "single", "locale": "en", "theme": "dark"}
        </script>
        """
        components.html(gauge_html, height=310)

with tab_real:
    st.subheader("💰 Activate Real Money Wallet securely")
    st.write("Earn real money by routing trades safely through global licensed partners.")
    col_d1, col_d2 = st.columns(2)
    with col_d1:
        st.markdown('[<button style="width:100%; padding:12px; background:linear-gradient(135deg, #00D09C 0%, #007d5e 100%); color:white; border:none; border-radius:8px; font-weight:bold; cursor:pointer;">💰 Trade Real Money on Indian Stocks</button>](#)', unsafe_allowed_html=True)
    with col_d2:
        st.markdown('[<button style="width:100%; padding:12px; background:linear-gradient(135deg, #FCD535 0%, #c7a400 100%); color:black; border:none; border-radius:8px; font-weight:bold; cursor:pointer;">💰 Trade Real Money on Crypto</button>](#)', unsafe_allowed_html=True)

st.markdown("---")
st.caption("Platform v4.1 - Safe Multi-Data Build")
