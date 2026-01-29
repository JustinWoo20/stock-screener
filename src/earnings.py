# TODO: Find previous P/E ratios and see if they are expected to rise or fall
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default = 'browser'
import yfinance as yf
# from src import get_financials
# from src import initial_screen

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
    historic_bar.show()
    return df_historic, historic_bar

eps_previous, historic_bar = get_actual_hist_eps(ticker)

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
    eps_bar.show()
    return eps_bar

get_hist_forward_eps(ticker=ticker, eps_previous=eps_previous)