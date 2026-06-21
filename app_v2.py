import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
from twilio.rest import Client

st.set_page_config(page_title="AI Crypto Dashboard", layout="wide")

st.title("🚀 AI Crypto Trading Signal Dashboard")
st.write("Bitcoin (BTC) Real-Time Data, Advanced Indicators & AI Signals")

# Fetching keys safely from Streamlit Secrets
try:
    TWILIO_SID = st.secrets["TWILIO_SID"]
    TWILIO_TOKEN = st.secrets["TWILIO_TOKEN"]
    TO_WHATSAPP = st.secrets["TO_WHATSAPP"]
    FROM_WHATSAPP = "whatsapp:+14155238886"
except Exception:
    st.warning("⚠️ Twilio Secrets config nahi mile. Dashboard settings mein Secrets set karein.")

def send_whatsapp_alert(signal_text, price):
    try:
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        message_body = f"⚠️ *CRITICAL AI CRYPTO ALERT* ⚠️\n\n📌 *Asset:* BTC/USDT\n💰 *Price:* ${price:,.2f}\n📢 *Signal:* {signal_text}"
        client.messages.create(body=message_body, from_=FROM_WHATSAPP, to=TO_WHATSAPP)
        return True
    except Exception as e:
        st.sidebar.error(f"WhatsApp Error: {e}")
        return False

# Binance Data Fetch
url = "https://api.binance.com/api/v3/klines"
params = {"symbol": "BTCUSDT", "interval": "1d", "limit": "100"}

try:
    response = requests.get(url, params=params).json()
    columns = ['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time', 'Asset Volume', 'Trades', 'Buy Base', 'Buy Quote', 'Ignore']
    df = pd.DataFrame(response, columns=columns)
    df['Date'] = pd.to_datetime(df['Open Time'], unit='ms')
    df['Close'] = df['Close'].astype(float)
    df['SMA_5'] = df['Close'].rolling(window=5).mean()

    latest_close = float(df['Close'].iloc[-1])
    st.metric(label="💰 Latest BTC Price", value=f"${latest_close:,.2f}")

    if st.button("📲 Test Send WhatsApp Alert"):
        if send_whatsapp_alert("⚪ Dashboard Testing Signal Active!", latest_close):
            st.toast("WhatsApp Alert Sent Successfully! Check phone.")

    st.subheader("📊 Price Chart")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df['Date'].iloc[-30:], df['Close'].iloc[-30:], color='cyan', label='BTC')
    ax.plot(df['Date'].iloc[-30:], df['SMA_5'].iloc[-30:], color='orange', label='SMA 5')
    ax.legend()
    st.pyplot(fig)
except Exception as e:
    st.error(f"Error: {e}")
  
