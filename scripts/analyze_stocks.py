from src import initial_screen, get_financials, financial_metrics, technical_indicators

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

    # financial_metrics src
    price_targets = financial_metrics.get_investor_confidence(ticker=ticker)
    ni_y = financial_metrics.get_net_income_y(ticker=ticker, income=income_y, ticks=years)
    ni_q = financial_metrics.get_net_income_q(ticker=ticker, income=income_q, ticks=quarters)
    se_y = financial_metrics.get_shareholder_equity(ticker=ticker, income=income_y, balance=balance_y, ticks=years)
    se_q = financial_metrics.get_shareholder_equity_q(ticker=ticker, balance=balance_q, ticks=quarters)
    cf_y = financial_metrics.get_cash_flow(ticker=ticker, cashflow=cashflow_y, ticks=years)
    cf_q = financial_metrics.get_cashflow_q(ticker=ticker, cashflow=cashflow_q, ticks=quarters)
    roic = financial_metrics.get_roic(ticker=ticker, income=income_y, balance=balance_y, ticks=years)
    fcf_margin_y = financial_metrics.get_fcf_margin(ticker=ticker, income=income_y, cashflow=cashflow_y, ticks=years)
    fcf_margin_q = financial_metrics.get_fcf_margin_q(ticker=ticker, income=income_q, cashflow=cashflow_q, ticks=quarters)
    oi_growth_y = financial_metrics.get_oi_growth(ticker=ticker, income=income_y, ticks=years)
    oi_growth_q = financial_metrics.get_oi_q_growth(ticker=ticker, income=income_q, ticks=quarters)
    om, om_graph = financial_metrics.get_operating_margin(ticker=ticker, income=income_y, ticks=years)
    omt_y = financial_metrics.get_om_trend(ticker=ticker, om_data=om, ticks=years)
    om_q, om_q_graph = financial_metrics.get_operating_margin_q(ticker=ticker, income=income_q, ticks=quarters)
    omt_q = financial_metrics.get_om_q_trend(ticker=ticker, om_data=om_q, ticks=quarters)
    gm = financial_metrics.get_gross_margin(ticker=ticker, income=income_y, ticks=years)
    gm_q = financial_metrics.get_gross_q_margin(ticker=ticker, income=income_q, ticks=quarters)

    # technical_indicators src
    history1, history3 = technical_indicators.get_historical_prices(ticker=ticker)
    closing_price = technical_indicators.plot_closing(ticker=ticker, history=history3)
    rsi, rsi_plot = technical_indicators.get_rsi(ticker=ticker, history=history3)
    rsi_price_plot = technical_indicators.plot_rsi_price(ticker=ticker, history=history3, r=rsi)
    macd_df, macd_plot = technical_indicators.get_macd(ticker=ticker, history=history1)
    macd_indicators = technical_indicators.plot_macd_price_indicators(ticker=ticker, history=history1, m=macd_df)
    history_stoch, stoch_plot = technical_indicators.get_stoch_osc(ticker=ticker, history=history1)
    stoch_indicator_plot = technical_indicators.plot_price_stoch(ticker=ticker, history=history_stoch)

# Put charts into excel file


