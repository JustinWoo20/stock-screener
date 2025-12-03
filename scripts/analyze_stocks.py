import datetime
from src import initial_screen, get_financials, financial_metrics, technical_indicators
import kaleido
import pandas as pd
import matplotlib.figure as mplfig
import plotly.graph_objects as go
from io import BytesIO

sector_list = ['Basic Materials', 'Communication Services', 'Consumer Cyclical', 'Consumer Defensive',
               'Energy', 'Financial Services', 'Healthcare', 'Industrials', 'Real Estate', 'Technology', 'Utilities']
debug_dict = {'Fair Isaac': 'FICO',
              'Wix.com': 'WIX',
              'Next Technology Holding': 'NXTT',
              'Electro-Sensors': 'ELSE',
              'Tuya': 'TUYA', 'Yalla': 'YALA',
              'Full Truck Alliance': 'YMM',
              'Quantum Computing': 'QUBT',
              'M-tron Industries': 'MPTI',
              'GitLab': 'GTLB'}


# Initial screen src
stock_dict, sector = initial_screen.screen_stocks()
print(f"Stocks retreived: \n"
      f"{stock_dict}")
# for stock in stock_dict.values():
#     print(stock)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter(f"../outputs/{sector}_{datetime.date.today()}.xlsx", engine='xlsxwriter')

for stock in stock_dict.values():
    figs = []

    # get_financials src
    ticker = get_financials.get_ticker(stock)
    income_y, income_q, balance_y, balance_q, cashflow_y, cashflow_q = get_financials.financial_statements(ticker)
    years, quarters = get_financials.useful_variables(income_y, income_q)

    # financial_metrics src
    try:
        price_targets = financial_metrics.get_investor_confidence(ticker=ticker)
    except KeyError:
        print(f"No investor confidence data available for {ticker.info['symbol']}")
        print("Starting analysis of the next stock.")
        continue
    ni_y = financial_metrics.get_net_income_y(ticker=ticker, income=income_y, ticks=years)
    figs.append(ni_y)
    ni_q = financial_metrics.get_net_income_q(ticker=ticker, income=income_q, ticks=quarters)
    figs.append(ni_q)
    se_y = financial_metrics.get_shareholder_equity(ticker=ticker, income=income_y, balance=balance_y, ticks=years)
    figs.append(se_y)
    se_q = financial_metrics.get_shareholder_equity_q(ticker=ticker, balance=balance_q, ticks=quarters)
    figs.append(se_q)
    cf_y = financial_metrics.get_cash_flow(ticker=ticker, cashflow=cashflow_y, ticks=years)
    figs.append(cf_y)
    cf_q = financial_metrics.get_cashflow_q(ticker=ticker, cashflow=cashflow_q, ticks=quarters)
    figs.append(cf_q)
    roic = financial_metrics.get_roic(ticker=ticker, income=income_y, balance=balance_y, ticks=years)
    figs.append(roic)
    fcf_margin_y = financial_metrics.get_fcf_margin(ticker=ticker, income=income_y, cashflow=cashflow_y, ticks=years)
    figs.append(fcf_margin_y)
    fcf_margin_q = financial_metrics.get_fcf_margin_q(ticker=ticker, income=income_q, cashflow=cashflow_q, ticks=quarters)
    figs.append(fcf_margin_q)
    oi_growth_y = financial_metrics.get_oi_growth(ticker=ticker, income=income_y, ticks=years)
    figs.append(oi_growth_y)
    oi_growth_q = financial_metrics.get_oi_q_growth(ticker=ticker, income=income_q, ticks=quarters)
    figs.append(oi_growth_q)
    om, om_graph = financial_metrics.get_operating_margin(ticker=ticker, income=income_y, ticks=years)
    figs.append(om_graph)
    omt_y = financial_metrics.get_om_trend(ticker=ticker, om_data=om, ticks=years)
    figs.append(omt_y)
    om_q, om_q_graph = financial_metrics.get_operating_margin_q(ticker=ticker, income=income_q, ticks=quarters)
    figs.append(om_q_graph)
    omt_q = financial_metrics.get_om_q_trend(ticker=ticker, om_data=om_q, ticks=quarters)
    figs.append(omt_q)
    gm = financial_metrics.get_gross_margin(ticker=ticker, income=income_y, ticks=years)
    figs.append(gm)
    gm_q = financial_metrics.get_gross_q_margin(ticker=ticker, income=income_q, ticks=quarters)
    figs.append(gm_q)

    # technical_indicators src
    history1, history3 = technical_indicators.get_historical_prices(ticker=ticker)
    closing_price = technical_indicators.plot_closing(ticker=ticker, history=history3)
    figs.append(closing_price)
    rsi, rsi_plot = technical_indicators.get_rsi(ticker=ticker, history=history3)
    figs.append(rsi_plot)
    rsi_price_plot = technical_indicators.plot_rsi_price(ticker=ticker, history=history3, r=rsi)
    figs.append(rsi_price_plot)
    macd_df, macd_plot = technical_indicators.get_macd(ticker=ticker, history=history1)
    figs.append(macd_plot)
    macd_indicators = technical_indicators.plot_macd_price_indicators(ticker=ticker, history=history1, m=macd_df)
    figs.append(macd_indicators)
    history_stoch, stoch_plot = technical_indicators.get_stoch_osc(ticker=ticker, history=history1)
    figs.append(stoch_plot)
    stoch_indicator_plot = technical_indicators.plot_price_stoch(ticker=ticker, history=history_stoch)
    figs.append(stoch_indicator_plot)

    # Convert quick statistics to excel writer object
    price_targets.to_excel(writer, sheet_name=f"{ticker.info['symbol']}")

    worksheet = writer.sheets[f"{ticker.info['symbol']}"]

    # Starting row for images
    row = 20
    # Save images to system RAM
    for i, fig in enumerate(figs):
        buf = BytesIO()
        if isinstance(fig, go.Figure):
            fig.write_image(buf, format='png')
        elif isinstance(fig, mplfig.Figure):
            fig.savefig(buf, format='png')
        else:
            print("Unknown figure type:", type(fig))
            break

        buf.seek(0)

        # Inset images
        worksheet.insert_image(row, 1, f"fig_{i}.png", {"image_data": buf})

        row += 25
    # Close excel writer
    print(f"{ticker.info['symbol']} finished.")

writer.close()
