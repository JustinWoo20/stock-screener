
# from src import initial_screen, get_financials, financial_metrics, technical_indicators
from src import get_financials
from src import initial_screen

sector_list = ['Basic Materials', 'Communication Services', 'Consumer Cyclical', 'Consumer Defensive',
               'Energy', 'Financial Services', 'Healthcare', 'Industrials', 'Real Estate', 'Technology', 'Utilities']

# Initial screen src
stock_dict = initial_screen.screen_stocks()
# for stock in stock_dict.values():
#     print(stock)

for stock in stock_dict.values():
    # get_financials src
    ticker = get_financials.get_ticker(stock)
    income_y, income_q, balance_y, balance_q, cashflow_y, cashflow_q = get_financials.financial_statements(ticker)
    years, quarters = get_financials.useful_variables(income_y, income_q)
    print(ticker)
    print(income_y)

    # # financial_metrics src
    # financial_metrics.get_price_targets(ticker=ticker)
    # financial_metrics.get_insider_stats(ticker=ticker)
    # financial_metrics.get_net_income_y(ticker=ticker, income=income_y, ticks=years)
    # financial_metrics.get_net_income_q(ticker=ticker, income=income_q, ticks=quarters)
    # financial_metrics.get_shareholder_equity(ticker=ticker, income=income_y, balance=balance_y, ticks=years)
    # financial_metrics.get_shareholder_equity_q(ticker=ticker, balance=balance_q, ticks=quarters)
    # financial_metrics.get_cash_flow(ticker=ticker, cashflow=cashflow_y, ticks=years)
    # financial_metrics.get_cashflow_q(ticker=ticker, cashflow=cashflow_q, ticks=quarters)
    # financial_metrics.get_roic(ticker=ticker, income=income_y, balance=balance_y, ticks=years)
    # financial_metrics.get_fcf_margin(ticker=ticker, income=income_y, cashflow=cashflow_y, ticks=years)
    # financial_metrics.get_fcf_margin_q(ticker=ticker, income=income_q, cashflow=cashflow_q, ticks=quarters)
    # financial_metrics.get_oi_growth(ticker=ticker, income=income_y, ticks=years)
    # financial_metrics.get_oi_q_growth(ticker=ticker, income=income_q, ticks=quarters)
    # om = financial_metrics.get_operating_margin(ticker=ticker, income=income_y, ticks=years)
    # financial_metrics.get_om_trend(ticker=ticker, om_data=om, ticks=years)
    # om_q = financial_metrics.get_operating_margin_q(ticker=ticker, income=income_q, ticks=quarters)
    # financial_metrics.get_om_q_trend(ticker=ticker, om_data=om_q, ticks=quarters)
    # financial_metrics.get_gross_margin(ticker=ticker, income=income_y, ticks=years)
    # financial_metrics.get_gross_q_margin(ticker=ticker, income=income_q, ticks=quarters)
    # # break
    #
    # # technical_indicators src
    # history1, history3 = technical_indicators.get_historical_prices(ticker=ticker)
    # technical_indicators.plot_closing(ticker=ticker, history=history3)
    # rsi = technical_indicators.get_rsi(ticker=ticker, history=history3)
    # technical_indicators.plot_rsi_price(ticker=ticker, history=history3, r=rsi)
    # macd_df = technical_indicators.get_macd(ticker=ticker, history=history1)
    # technical_indicators.plot_price_indicators(ticker=ticker, history=history1, m=macd_df)
    # history_stoch = technical_indicators.get_stoch_osc(ticker=ticker, history=history1)
    # technical_indicators.plot_price_stoch(ticker=ticker, history=history_stoch)
    # break


