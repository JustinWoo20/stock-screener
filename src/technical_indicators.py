from get_financials import ticker
import ta
import pandas as pd
import plotly.express as px

def get_historical_prices(ticker):
    # Retrieve stock price history from past year and 3 years
    one_year = ticker.history(period='1y')
    three_year = ticker.history(period='3y')
    return one_year, three_year
history1, history3 = get_historical_prices(ticker=ticker)

def plot_closing(ticker, history3):
    # Plot 3 year closing Price
    price_plot = px.line(history3, x=history3.index, y=history3.Close, title=f"{ticker.info['shortName']} 3 Year Closing Price", height=500)
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
rsi = get_rsi(ticker=ticker, history=history3)