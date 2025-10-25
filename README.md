# momentum-analyzer
Momentum bets on continuation. If a stock is up, buy more. If down, sell.A 2011 study(https://workdrive.zoho.in/file/p7jlh988388faded74137aa1f8be6b25eb3c4) showed this strategy works well with a one month lookback.'
  Time Series Momentum Analyzer

A sleek Streamlit app that helps you analyze short-term momentum for NSE-listed stocks using a proven time-series momentum strategy.

##  Live App

 [Launch the App](https://kulvishwas8-momentum-analyzer.streamlit.app)

##  What It Does

This app calculates the **momentum** of selected NSE stocks over a user-defined lookback period (default: 20 trading days). It helps identify whether a stock is showing **positive momentum** (likely to continue rising) or **negative momentum** (likely to decline), based on historical price trends.

##  Features

- Searchable NSE stock list (auto-loaded from NSE India)
- Momentum calculation using 1-month lookback (adjustable)
- Live current price display for each selected stock
- Interactive price charts
- Visual momentum signal (Strong or Weak)
- Smart caching for faster performance

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kulvishwas8/momentum-analyzer.git
   cd momentum-analyzer
