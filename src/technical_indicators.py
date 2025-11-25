# from get_financials import ticker
import matplotlib.pyplot as plt
import ta
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def get_historical_prices(ticker):
    # Retrieve stock price history from past year and 3 years
    one_year = ticker.history(period='1y')
    three_year = ticker.history(period='3y')
    return one_year, three_year
# history1, history3 = get_historical_prices(ticker=ticker)

def plot_closing(ticker, history):
    # Plot 3 year closing Price
    price_plot = px.line(history, x=history.index, y=history.Close, title=f"{ticker.info['shortName']} 3 Year Closing Price", height=500)
    price_plot.update_layout(xaxis_title='Date', yaxis_title='Closing Price')
    price_plot.show()

def get_rsi(ticker, history):
    # Plot rsi
    rsi_object = ta.momentum.RSIIndicator(close=history.Close, window=14)
    rsi = rsi_object.rsi()

    rsi_plot = px.line(history, x=history.index, y=rsi.values, title=f"{ticker.info['shortName']} 14-Day RSI", height=500)
    rsi_plot.update_layout(xaxis_title='Date', yaxis_title='RSI')
    rsi_plot.add_hline(y=70, line_dash='dash', line_color='red')
    rsi_plot.add_hline(y=30, line_dash='dash', line_color='green')
    rsi_plot.show()
    return rsi

def plot_rsi_price(ticker, history, r):
    plt.figure(figsize=(14, 8), dpi=120)
    plt.xticks(fontsize=14, rotation=45)
    plt.yticks(fontsize=14)
    plt.title(f"{ticker.info['shortName']} 14-Day RSI and Price")

    ax1 = plt.gca()
    ax2 = ax1.twinx()

    ax1.set_xlim([history.index.min(), history.index.max()])
    ax1.set_ylim([0, r.max() + 5])
    ax2.set_ylim([history.Close.min() - 30, history.Close.max() + 30])

    ax1.plot(history.index, r.values, color='red')
    ax2.plot(history.index, history.Close, color='green')
    ax1.axhline(y=70, linestyle='--', color='blue', alpha=0.5)
    ax1.axhline(y=30, linestyle='--', color='red', alpha=0.5)
    ax1.set_xlabel('Date')
    ax1.set_ylabel('RSI', color='red')
    ax2.set_ylabel('Price', color='green')
    plt.show()

def get_macd(ticker, history):
    # Obtain macd line, signal line, and histogram
    macd_object = ta.trend.MACD(close=history.Close, window_slow=26, window_fast=12, window_sign=9)
    macd = macd_object.macd()
    signal_line = macd_object.macd_signal()
    histogram = macd_object.macd_diff()
    # Put into dataframe
    macd_df = pd.DataFrame({'MACD': macd, 'Signal': signal_line, 'Histogram': histogram}, index=history.index)
    #Plot
    macd_plot = px.line(macd_df, x=macd_df.index, y=['MACD', 'Signal'], title=f"{ticker.info['shortName']} MACD", height=500)
    macd_plot.update_layout(xaxis_title='Date', yaxis_title='MACD')
    macd_plot.show()
    return macd_df

def plot_price_indicators(m, ticker, history):
    # Find indicators
    history['bullish_signal'] = (m.MACD > m.Signal) & (m.MACD.shift(1) < m.Signal.shift(1))
    history['bearish_signal'] = (m.MACD < m.Signal) & (m.MACD.shift(1) > m.Signal.shift(1))
    buy_dates = history[history['bullish_signal']].index
    sell_dates = history[history['bearish_signal']].index

    # Plot closing price with indicators
    price_signals = go.Figure()
    price_signals.add_trace(go.Scatter(x=history.index, y=history.Close, mode='lines', name='Closing Price'))
    price_signals.add_trace(
        go.Scatter(x=buy_dates, y=history.loc[buy_dates, 'Close'], mode='markers', marker_symbol='triangle-up',
                   marker_color='green', name='Buy Signal', marker_size=12))
    price_signals.add_trace(
        go.Scatter(x=sell_dates, y=history.loc[sell_dates, 'Close'], mode='markers', marker_symbol='triangle-down',
                   marker_color='red', name='Sell Signal', marker_size=12))
    price_signals.update_layout(yaxis_title='Price', xaxis_title='Date', height=600,
                                title=f"{ticker.info['shortName']} Closing Price with MACD Indicators")
    price_signals.show()

def get_stoch_osc(ticker, history):
    stoch = ta.momentum.StochasticOscillator(high=history['High'], close=history['Close'], low=history['Low'],
                                             window=14, smooth_window=3)
    history['%K'] = stoch.stoch()
    history['%D'] = stoch.stoch_signal()
    history_copy = history.copy()
    stoch_plot = px.line(history, x=history.index, y=['%K', '%D'],
                         title=f"{ticker.info['shortName']} 14-Day Stochastic Oscillator", height=500)
    stoch_plot.update_layout(xaxis_title='Date', yaxis_title='Stochastic Oscillator')
    stoch_plot.add_hline(y=80, line_dash='dash', line_color='red')
    stoch_plot.add_hline(y=20, line_dash='dash', line_color='green')
    stoch_plot.show()
    return history_copy

def plot_price_stoch(ticker, history):
    #Find buy and sell signals
    history['bullish_stoch'] = (history['%K'] > history['%D']) & (history['%K'].shift(1) < history['%D'].shift(1))
    history['bearish_stoch'] = (history['%K'] < history['%D']) & (history['%K'].shift(1) > history['%D'].shift(1))
    buy_dates_s = history[history['bullish_stoch']].index
    sell_dates_s = history[history['bearish_stoch']].index

    price_stoch = go.Figure()
    price_stoch.add_trace(go.Scatter(x=history.index, y=history.Close, mode='lines', name='Closing Price'))
    price_stoch.add_trace(go.Scatter(x=buy_dates_s, y=history.loc[buy_dates_s, 'Close'], mode='markers',
                                     marker_symbol='triangle-up', marker_color='green', name='Buy Signal',
                                     marker_size=12))
    price_stoch.add_trace(go.Scatter(x=sell_dates_s, y=history.loc[sell_dates_s, 'Close'], mode='markers',
                                     marker_symbol='triangle-down', marker_color='red', name='Sell Signal',
                                     marker_size=12))
    price_stoch.update_layout(yaxis_title='Price', xaxis_title='Date', height=600,
                              title=f'{ticker.info['shortName']} Closing Price with Stochastic Oscillator Indicators')
    price_stoch.show()
