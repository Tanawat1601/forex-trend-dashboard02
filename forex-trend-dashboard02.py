import streamlit as st
import pandas as pd
from datetime import datetime

flags = {
    "EUR": "🇪🇺", "USD": "🇺🇸", "JPY": "🇯🇵",
    "GBP": "🇬🇧", "CHF": "🇨🇭", "AUD": "🇦🇺",
    "CAD": "🇨🇦", "NZD": "🇳🇿"
}

# ตัวอย่างข้อมูล
data = [
    {"Symbol": "EURUSD", "EMA": "Uptrend", "RSI": 65, "MACD": "Bullish", "Trend": "↑ Strong Up"},
    {"Symbol": "USDJPY", "EMA": "Uptrend", "RSI": 70, "MACD": "Bullish", "Trend": "↑ Strong Up"},
    {"Symbol": "GBPUSD", "EMA": "Downtrend", "RSI": 45, "MACD": "Bearish", "Trend": "↓ Weak Down"},
    {"Symbol": "USDCHF", "EMA": "Uptrend", "RSI": 68, "MACD": "Bullish", "Trend": "↑ Moderate Up"},
    {"Symbol": "GBPJPY", "EMA": "Downtrend", "RSI": 39, "MACD": "Bearish", "Trend": "↓ Strong Down"},
    {"Symbol": "CHFJPY", "EMA": "Sideway", "RSI": 52, "MACD": "Neutral", "Trend": "→ Sideway"}
]

for d in data:
    base, quote = d["Symbol"][:3], d["Symbol"][3:]
    d["Pair"] = f"{flags.get(base, '')} {base} / {flags.get(quote, '')} {quote}"
    if "↑" in d["Trend"]:
        d["Trend Icon"] = "🟢⬆️"
    elif "↓" in d["Trend"]:
        d["Trend Icon"] = "🔴⬇️"
    else:
        d["Trend Icon"] = "⚠️➡️"

df = pd.DataFrame(data)
df['Last Checked'] = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

st.set_page_config(page_title="Forex Trend Overview", layout="wide")
st.title("📈 Forex Trend Dashboard (USD / CHF / GBP)")
st.markdown(f"**Updated:** {df['Last Checked'][0]}")
st.dataframe(df.drop(columns=["Last Checked"]), use_container_width=True)

st.markdown("---")
st.subheader("📢 แนวทางการตีความ:")
st.markdown("""
- 🟢 **↑ Strong Up**: แนวโน้มขาขึ้นแข็งแรง เหมาะสำหรับหาโอกาส Buy  
- 🔴 **↓ Strong Down**: แนวโน้มขาลงชัดเจน ระวังการ Buy สวนเทรนด์  
- ⚠️ **→ Sideway**: ยังไม่ชัดเจน ควรรอดูเพิ่มเติมก่อนเข้าออเดอร์  
""")
