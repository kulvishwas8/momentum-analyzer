
import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import date

# 💾 Cache NSE tickers


@st.cache_data
def load_nse_tickers():
    url = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"
    df = pd.read_csv(url)
    tickers = df['SYMBOL'].dropna().unique().tolist()
    return [symbol + ".NS" for symbol in tickers]


# 🎯 App Config
st.set_page_config(page_title="Momentum Analyzer",
                   page_icon="📈", layout="wide")
st.markdown("""
<style>
    .big-font {font-size:22px !important;}
    .highlight {background-color:#f0f8ff;padding:10px;border-radius:10px;}
    .price-badge {font-size:18px;color:#006400;background-color:#e6ffe6;padding:6px 12px;border-radius:8px;display:inline-block;margin-bottom:10px;}
</style>
""", unsafe_allow_html=True)

# 📌 Title and Intro
st.title("📈 Stock Price Momentum Analyzer")
st.write('Momentum bets on continuation. If a stock is up, buy more. If down, sell.'
         ' A 2011 study(https://workdrive.zoho.in/file/p7jlh988388faded74137aa1f8be6b25eb3c4) '
         'showed this strategy works well with a one month lookback.')


# 📅 Date Range
START = '2024-01-01'
TODAY = date.today().strftime('%Y-%m-%d')

# 📋 Load tickers and set defaults
tickers = load_nse_tickers()
default_stocks = [s for s in ['RELIANCE.NS'] if s in tickers]

# 🧠 User Inputs
selected_stocks = st.multiselect(
    "🔍 Choose NSE stocks:", options=tickers, default=default_stocks)
lookback = st.slider("⏱️ Lookback period (trading days)",
                     min_value=5, max_value=20, value=20)

# 🚀 Run Analysis
if selected_stocks:
    for stock in selected_stocks:
        st.markdown(f"---\n### 📌 {stock} Momentum Analysis")

        try:
            data = yf.download(stock, start=START, end=TODAY)
            if isinstance(data.columns, pd.MultiIndex):
                data.columns = data.columns.droplevel(1)
            data = data.iloc[1:]
            data.reset_index(inplace=True)
            data = data[(data != 0).all(axis=1)]
            prices = data['Close']

            # 🏷️ Show current price
            current_price = prices.iloc[-1] if not prices.empty else None
            if current_price:
                st.markdown(
                    f'<div class="price-badge">Current Price: ₹{current_price:.2f}</div>', unsafe_allow_html=True)

            # 📊 Momentum Calculation
            if len(prices) >= lookback:
                momentum = prices.iloc[-1] / prices.iloc[-lookback] - 1
                st.metric(label="📊 Momentum", value=f"{momentum:.2%}")
                if momentum > 0:
                    st.success("✅ Momentum is strong")
                else:
                    st.warning("⚠️ Momentum is weak")
                st.line_chart(prices)
            else:
                st.error(f"Not enough data to compute momentum for {stock}")

        except Exception as e:
            st.error(f"❌ Error fetching data for {stock}: {e}")
else:
    st.info("👈 Please select at least one stock to begin analysis.")

st.write('DISCLAIMER:The purpose of application is to make user aware of a concept.'
         'It should not be construed as a financial advice in any way')


