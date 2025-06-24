import streamlit as st
import pandas as pd
from datetime import datetime

# ธงชาติ Emoji
flags = {
    "EUR": "🇪🇺", "USD": "🇺🇸", "JPY": "🇯🇵",
    "GBP": "🇬🇧", "CHF": "🇨🇭", "AUD": "🇦🇺",
    "CAD": "🇨🇦", "NZD": "🇳🇿"
}

# TF dropdown
tf = st.selectbox("🕒 เลือก Timeframe", ["M15", "H1", "H4", "D1"], index=1)

# ตัวอย่างข้อมูลแต่ละ TF (ใส่ข้อมูลจำลองหรือดึงจาก API ในอนาคต)
data_tf = {
    "M15": [
        {"Symbol": "EURUSD", "EMA": "Uptrend", "RSI": 61, "MACD": "Bullish", "Trend": "↑ Strong Up"},
        {"Symbol": "USDJPY", "EMA": "Downtrend", "RSI": 42, "MACD": "Bearish", "Trend": "↓ Strong Down"}
    ],
    "H1": [
        {"Symbol": "EURUSD", "EMA": "Uptrend", "RSI": 65, "MACD": "Bullish", "Trend": "↑ Strong Up"},
        {"Symbol": "USDJPY", "EMA": "Uptrend", "RSI": 70, "MACD": "Bullish", "Trend": "↑ Strong Up"}
    ],
    "H4": [
        {"Symbol": "EURUSD", "EMA": "Sideway", "RSI": 52, "MACD": "Neutral", "Trend": "→ Sideway"},
        {"Symbol": "USDJPY", "EMA": "Uptrend", "RSI": 60, "MACD": "Bullish", "Trend": "↑ Moderate Up"}
    ],
    "D1": [
        {"Symbol": "EURUSD", "EMA": "Downtrend", "RSI": 47, "MACD": "Bearish", "Trend": "↓ Weak Down"},
        {"Symbol": "USDJPY", "EMA": "Uptrend", "RSI": 69, "MACD": "Bullish", "Trend": "↑ Strong Up"}
    ]
}

# เตรียมข้อมูลตาราง
data = data_tf[tf]
for d in data:
    base, quote = d["Symbol"][:3], d["Symbol"][3:]
    d["Pair"] = f"{flags.get(base, '')} {base} / {flags.get(quote, '')} {quote}"
    if "↑" in d["Trend"]:
        d["Trend Icon"] = "🟢⬆️"
    elif "↓" in d["Trend"]:
        d["Trend Icon"] = "🔴⬇️"
    else:
...         d["Trend Icon"] = "⚠️➡️"
... 
... df = pd.DataFrame(data)
... df['Last Checked'] = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
... 
... # UI
... st.set_page_config(page_title="Check the Trend by Nagraph", layout="wide")
... st.markdown(f"<h1 style='text-align:center;'>📈 Check the Trend by Nagraph</h1>", unsafe_allow_html=True)
... st.markdown(f"<div style='text-align:center;'>⏱ TF: <strong>{tf}</strong> | Updated: {df['Last Checked'][0]}</div>", unsafe_allow_html=True)
... st.markdown("---")
... 
... # จัดแสดงตาราง
... display_df = df[["Pair", "EMA", "RSI", "MACD", "Trend Icon", "Trend"]]
... display_df.columns = ["คู่เงิน", "แนวโน้ม EMA", "RSI", "MACD", "📍ทิศทาง", "คำอธิบาย"]
... 
... def style_row(row):
...     if "Strong Up" in row["คำอธิบาย"]:
...         return ["background-color: #d4edda"] * len(row)
...     elif "Strong Down" in row["คำอธิบาย"]:
...         return ["background-color: #f8d7da"] * len(row)
...     elif "Sideway" in row["คำอธิบาย"]:
...         return ["background-color: #fff3cd"] * len(row)
...     return ["" for _ in row]
... 
... st.dataframe(display_df.style.apply(style_row, axis=1), use_container_width=True)
... 
... # Legend
... st.markdown("---")
... st.subheader("🧭 แนวทางการตีความ")
... st.markdown("""
... - 🟢⬆️ **↑ Strong Up** = เทรนด์ขาขึ้นแข็งแรง เหมาะกับ Buy  
... - 🔴⬇️ **↓ Strong Down** = เทรนด์ขาลงชัดเจน ระวัง Buy สวน  
... - ⚠️➡️ **→ Sideway** = เทรนด์ไม่ชัด ควรรอดูต่อ  
... """)
... st.markdown("<div style='text-align:center; font-size:12px; color:gray;'>By Nagraph | Powered by Streamlit</div>", unsafe_allow_html=True)
