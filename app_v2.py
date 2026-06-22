import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="AI Pro Animated Platform", page_icon="📈", layout="wide")

# --- CUSTOM PREMIUM CSS FOR ANIMATIONS & DESIGN ---
st.markdown("""
<style>
    /* Global Styles */
    .stApp {
        background-color: #0d1117;
    }
    
    /* Premium Glassmorphic Cards with Fade-in Animation */
    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 15px 20px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(5px);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        animation: fadeIn 0.8s ease-in-out;
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0, 208, 156, 0.1);
        border: 1px solid rgba(0, 208, 156, 0.2);
    }

    /* Pulse Glow Animation for Demo Balance */
    h3 {
        animation: pulseGlow 2s infinite alternate;
    }

    /* Custom Animated Button */
    div.stButton > button {
        background: linear-gradient(135deg, #00d09c 0%, #009a73 100%) !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 12px 24px !important;
        font-weight: bold !important;
        box-shadow: 0 4px 15px rgba(0, 208, 156, 0.3) !important;
        transition: all 0.3s ease-in-out !important;
    }
    div.stButton > button:hover {
        transform: scale(1.02) !important;
        box-shadow: 0 6px 20px rgba(0, 208, 156, 0.5) !important;
    }
    div.stButton > button:active {
        transform: scale(0.98) !important;
    }

    /* Keyframes for Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes pulseGlow {
        from { text-shadow: 0 0 5px rgba(255,255,255,0.1); }
        to { text-shadow: 0 0 15px rgba(0, 208, 156, 0.4); }
    }
</style>
""", unsafe_allowed_html=True)

st.title("🚀 AI Trading Academy & Live Platform")
st.write("Learn Trading, Practice with Demo Account, and Trade with Real Money Safely!")

# --- STATE MANAGEMENT ---
if "demo_balance" not in st.session_state:
    st.session_state.demo_balance = 10000.00
if "trades_history" not in st.session_state:
    st.session_state.trades_history = []

# Top Header Stats with hover animations
col_h1, col_h2, col_h3 = st.columns(3)
with col_h1:
    st.markdown(f"### 🎮 Demo Balance: **${st.session_state.demo_balance:,.2f}**")
with col_h2:
    st.success("🟢 Real Account: Connected Securely")
with col_h3:
    st.metric(label="📊 Bank Nifty Live", value="48,250.30", delta="+1.2%")

st.markdown("---")

# Main Tabs: Trading, Learning, Real Money
tab_trade, tab_learn, tab_real = st.tabs(["🎮 Demo Trading Platform", "📚 Learn Trading (Key Features)", "💰 Real Money Trading"])

with tab_trade:
    col_chart, col_panel = st.columns([2.5, 1])
    
    with col_chart:
        st.subheader("📊 Live Market Chart")
        tradingview_html = """
        <div class="tradingview-widget-container" style="height:400px;width:100%">
          <div id="tv_main" style="height:100%;width:100%"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
          <script type="text/javascript">
          new TradingView.widget({"autosize": true, "symbol": "NSE:BANKNIFTY", "interval": "5", "theme": "dark", "style": "1", "locale": "en", "container_id": "tv_main"});
          </script>
        </div>
        """
        components.html(tradingview_html, height=410)
        
    with col_panel:
        st.subheader("Place Practice Trade")
        asset = st.selectbox("Select Asset", ["Bank Nifty", "Bitcoin (BTC)", "Nifty 50"])
        direction = st.radio("Market Prediction", ["🟢 CALL (Goes UP)", "🔴 PUT (Goes DOWN)"])
        amount = st.number_input("Investment ($)", min_value=10, max_value=5000, value=100)
        
        if st.button("Execute Demo Trade", use_container_width=True):
            if amount > st.session_state.demo_balance:
                st.error("Insufficient Demo Funds!")
            else:
                st.session_state.demo_balance -= amount
                dir_text = "UP" if "CALL" in direction else "DOWN"
                st.session_state.trades_history.append(f"Invested ${amount} on {asset} predicting {dir_text}")
                st.success("Demo Trade Executed!")

with tab_learn:
    st.subheader("📚 Trading Key Features & Guide for Beginners")
    
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        st.info("### 🟢 What is CALL & PUT?")
        st.write("- **CALL (Up):** Jab aapko lagta hai ki price upar jayega, tab Call option buy karte hain.")
        st.write("- **PUT (Down):** Jab aapko lagta hai ki price niche girega, tab Put option buy karte hain.")
        
        st.warning("### 📉 Risk Management Rule")
        st.write("Ek trade mein kabhi bhi apne total balance ka **2% se zyada** invest na karein. Ise Stop Loss kehte hain.")
        
    with col_l2:
        st.success("### 🤖 AI Technical Signals (Live Guide)")
        gauge_html = """
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
        {"interval": "1m", "width": "100%", "isTransparent": false, "height": 330, "symbol": "NSE:BANKNIFTY", "showIntervalTabs": false, "displayMode": "single", "locale": "en", "theme": "dark"}
        </script>
        """
        components.html(gauge_html, height=340)

with tab_real:
    st.subheader("💰 Activate Real Money Trading Wallet")
    st.write("Ready to make real profits? Deposit real money securely with India's top certified brokers.")
    
    st.markdown("### 🏦 Choose Your Deposit Method:")
    
    col_d1, col_d2 = st.columns(2)
    with col_d1:
        st.subheader("🇮🇳 Indian Stocks & Bank Nifty")
        st.write("Deposit via UPI / NetBanking instantly through our verified partner.")
        st.markdown('[<button style="width:100%; padding:12px; background:linear-gradient(135deg, #00D09C 0%, #007d5e 100%); color:white; border:none; border-radius:8px; font-weight:bold; cursor:pointer; box-shadow: 0 4px 15px rgba(0,208,156,0.3);">💰 Deposit & Trade on Groww</button>](#)', unsafe_allowed_html=True)
        
    with col_d2:
        st.subheader("🪙 Global Crypto Market")
        st.write("Deposit Crypto or INR via P2P instantly through secure wallet.")
        st.markdown('[<button style="width:100%; padding:12px; background:linear-gradient(135deg, #FCD535 0%, #c7a400 100%); color:black; border:none; border-radius:8px; font-weight:bold; cursor:pointer; box-shadow: 0 4px 15px rgba(252,213,53,0.3);">💰 Deposit & Trade on Binance</button>](#)', unsafe_allowed_html=True)

st.markdown("---")
st.caption("Platform Version 4.0 (Animated Premium Build)")
