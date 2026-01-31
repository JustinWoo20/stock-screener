# Work into main analyze stocks script
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default = 'browser'
import yfinance as yf
from src import initial_screen

ticker = yf.Ticker('FICO')

def get_actual_hist_eps(ticker):
    historic = ticker.get_earnings_history()
    df_historic = pd.DataFrame(historic)
    # Convert to quarters for a cleaner looking xaxis
    df_historic.index = df_historic.index.to_period('Q').astype(str)
    df_historic = df_historic.reset_index()
    df_historic = df_historic.rename(columns={'epsActual': 'eps', 'epsEstimate': 'eps estimate'})
    historic_bar = px.bar(df_historic, x='quarter', y=['eps', 'eps estimate'],
                          title=f'{ticker.info['shortName']} EPS vs. Estimated', barmode='group', height=500)
    historic_bar.update_layout(xaxis_title='Date', yaxis_title='EPS')
    return df_historic, historic_bar

def get_hist_forward_eps(ticker, eps_previous):
    # Obtain only previous eps data from history dataframe
    eps_previous = eps_previous[['quarter', 'eps']]
    # Obtain eps estimates for the next 2 quarters
    estimates = ticker.get_earnings_estimate()
    estimates = estimates.reset_index()
    estimates = estimates.rename(columns={'period': 'quarter', 'avg': 'eps'})
    eps_estimate = estimates[['quarter', 'eps']]
    # Drop eps year data
    eps_estimate = eps_estimate.drop([2, 3])
    # Clean up eps_estimate column data
    eps_estimate.loc[0, 'quarter'] = '2026Q1'
    eps_estimate.loc[1, 'quarter'] = '2026Q2'
    # Combine historical and estimates
    # eps_combined = pd.concat([eps, eps_estimate], ignore_index=True)

    # Plot data
    eps_bar = go.Figure()
    eps_bar.add_trace(go.Bar(x=eps_previous.quarter, y=eps_previous.eps,
                             marker_color='blue', name='Historic eps'))
    eps_bar.add_trace(go.Bar(x=eps_estimate.quarter, y=eps_estimate.eps,
                             marker_color='green', name='Forward eps'))
    eps_bar.update_layout(title_text=f'{ticker.info['shortName']} Historical eps and forward eps',
                          height=500)
    return eps_bar

def get_eps_trends(ticker):
    trends = ticker.get_eps_trend()
    trends_tran = trends.transpose()
    trends_tran = trends_tran.rename(columns={'0q': 'Current Quarter',
                                          '+1q': 'Next Quarter',
                                          '0y': 'Current Year',
                                          '+1y': 'Next Year',}).reset_index(names='period')
    quarter_trend = trends_tran[['period', 'Current Quarter', 'Next Quarter']]
    yearly_trend = trends_tran[['period', 'Current Year', 'Next Year']]

    quarter_line = px.line(quarter_trend, x='period', y=['Current Quarter', 'Next Quarter'],
                           height=500, title=f'Analysts predicted quarterly eps trends for {ticker.info['shortName']}')

    year_line = px.line(yearly_trend, x='period', y=['Current Year', 'Next Year'],
                        height=500, title=f'Analysts predicted yearly eps trends for {ticker.info['shortName']}')

    return quarter_line, year_line

def get_year_eps(ticker):
    info = ticker.info
    try:
        trailing_eps = info['trailingEps']
        print(f'Trailing EPS: {trailing_eps}')
    except KeyError:
        trailing_eps= info['epsTrailingTwelveMonths']
        print(f'Trailing EPS: {trailing_eps}')
    eps_current_year = info['epsCurrentYear']
    print(f'Current year predicted eps: {eps_current_year}')
    forward_eps = info['forwardEps']
    print(f'Forward eps: {forward_eps}')
    return trailing_eps, eps_current_year, forward_eps

def compare_pe(ticker):
    info = ticker.info
    trailing_pe = info['trailingPE']
    print(f'Trailing P/E: {trailing_pe}')
    forward_pe = info['forwardPE']
    print(f'Forward P/E: {forward_pe}')

compare_pe(ticker=ticker)