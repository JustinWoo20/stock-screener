# from get_financials import *
import pandas as pd
import plotly.express as px

def get_price_targets(ticker):
    # Obtain price targets based on analyst estimates
    analyst = ticker.analyst_price_targets
    upside_potential = analyst['median'] / analyst['current']
    risk_adjusted = (analyst['low'] + analyst['high'] + analyst['mean']) / 3
    print(f'The lowest analyst estimate for {ticker.info['shortName']} is: ${analyst['low']}')
    print(f'The median analyst estimate for {ticker.info['shortName']} is: ${analyst['median']}')
    print(f'The highest analyst estimate for {ticker.info['shortName']} is: ${analyst['high']}')
    print(f'The upside potential for {ticker.info['shortName']} is: {round(upside_potential * 100, 2)}%')
    print(f'The risk-adjusted target for {ticker.info['shortName']} is ${round(risk_adjusted, 2)}')

def get_insider_stats(ticker):
    # Obtain data on insider trading
    holders = ticker.major_holders
    print(f'The percentage held by insiders: {round(holders.loc['insidersPercentHeld', 'Value'] * 100, 4)}%')
    print(f'The percentage held by institutions: {round(holders.loc['institutionsPercentHeld', 'Value'] * 100, 4)}%')
    print(ticker.insider_purchases)

def get_net_income_y(ticker, income, ticks):
    # Graphs yearly net income
    ni_year_bar = px.bar(income, x=income.index,
                         y='NetIncome', title=f'{ticker.info['shortName']} Yearly Net Income', height=500)
    ni_year_bar.update_layout(xaxis_title='Date', yaxis_title='Net Income')
    ni_year_bar.update_xaxes(tickvals=income.index,
                             ticktext=ticks)
    ni_year_bar.show()

def get_net_income_q(ticker, income, ticks):
    # Graphs quarterly net income
    net_income = income['NetIncome']
    net_income = net_income.dropna()
    ni_quarter_bar = px.bar(net_income, x= net_income.index,
                         y='NetIncome', title=f'{ticker.info['shortName']} Quarterly Net Income', height=500)
    ni_quarter_bar.update_layout(xaxis_title='Quarter', yaxis_title='Net Income')
    ni_quarter_bar.update_xaxes(tickvals=net_income.index, ticktext=ticks)
    ni_quarter_bar.show()

def get_shareholder_equity(ticker, income, balance, ticks):
    # Graph yearly shareholder equity
    se_year_bar = px.bar(balance, x=balance.index,
                         y='StockholdersEquity', title=f"{ticker.info['shortName']} Yearly Shareholder's Equity", height=500)
    se_year_bar.update_layout(xaxis_title='Date', yaxis_title="Shareholder's Equity")
    se_year_bar.update_xaxes(tickvals=income.index,
                             ticktext=ticks)
    se_year_bar.show()

def get_shareholder_equity_q(ticker, balance, ticks):
    # Graphs quarterly shareholder's equity
    shareholder_eq = balance['StockholdersEquity']
    shareholder_eq = shareholder_eq.dropna()
    se_quarter_bar = px.bar(shareholder_eq, x=shareholder_eq.index,
                         y='StockholdersEquity', title=f"{ticker.info['shortName']} Quarterly Shareholder's Equity", height=500)
    se_quarter_bar.update_layout(xaxis_title='Quarter', yaxis_title="Shareholder's Equity")
    se_quarter_bar.update_xaxes(tickvals=balance.index, ticktext=ticks)
    se_quarter_bar.show()

def get_cash_flow(ticker, cashflow, ticks):
    # Yearly operating and free cash flow graphs
    cashflow = cashflow.rename(columns={'OperatingCashFlow': 'Operating Cash Flow', 'FreeCashFlow': 'Free Cash Flow'})
    cashflow_bar = px.bar(cashflow, x=cashflow.index, y=['Operating Cash Flow', 'Free Cash Flow'],
                          title=f"{ticker.info['shortName']} Yearly Operating Cash Flow and Free Cash Flow",
                         barmode='group', height=500,)
    cashflow_bar.update_layout(xaxis_title='Date', yaxis_title='Value', legend_title_text='Cash Flow Metric')
    cashflow_bar.update_xaxes(tickvals=cashflow.index, ticktext=ticks)
    cashflow_bar.show()

def get_cashflow_q(ticker, cashflow, ticks):
    # Graph quarterly cashflow metrics
    cashflow = cashflow.rename(columns={'OperatingCashFlow': 'Operating Cash Flow', 'FreeCashFlow': 'Free Cash Flow'})
    cashflow_q_bar = px.bar(cashflow, x=cashflow.index, y=['Operating Cash Flow', 'Free Cash Flow'],
                        title=f"{ticker.info['shortName']} Quearterly OCF and FCF", barmode='group', height=500)
    cashflow_q_bar.update_layout(xaxis_title='Quarter', yaxis_title='Value')
    cashflow_q_bar.update_xaxes(tickvals=cashflow.index, ticktext=ticks)
    cashflow_q_bar.show()

def get_roic(ticker, income, balance, ticks):
    # Graph return on invested capital
    # Calculate NOPAT
    income['NOPAT'] = income.EBIT * (1 - income.TaxRateForCalcs)
    balance['invested_capital'] = balance.LongTermDebt + balance.TotalEquityGrossMinorityInterest - balance.CashAndCashEquivalents
    roic = income.NOPAT / balance.invested_capital
    roic = roic.dropna()
    roic_bar = px.bar(roic, x=roic.index, y=roic.values, title=f"{ticker.info['shortName']} ROIC", height=500)
    roic_bar.update_layout(xaxis_title='Date', yaxis_title='ROIC')
    roic_bar.update_xaxes(tickvals=roic.index, ticktext=ticks)
    roic_bar.show()

def get_fcf_margin(ticker, income, cashflow, ticks):
    # Graph yearly free cash flow margin
    fcf_margin = cashflow['FreeCashFlow'] / income['TotalRevenue']
    fcf_margin = fcf_margin.dropna()

    fcf_margin_bar = px.bar(fcf_margin, x=fcf_margin.index, y=fcf_margin.values,
                            title=f"{ticker.info['shortName']} Yearly Free Cash Flow Margin", height=500)
    fcf_margin_bar.update_layout(xaxis_title='Date', yaxis_title='Margin')
    fcf_margin_bar.update_xaxes(tickvals=fcf_margin.index, ticktext=ticks)
    fcf_margin_bar.show()


def get_fcf_margin_q(ticker, income, cashflow, ticks):
    # Graph yearly free cash flow margin
    fcf_margin = cashflow['FreeCashFlow'] / income['TotalRevenue']
    fcf_margin = fcf_margin.dropna()

    fcf_margin_bar = px.bar(fcf_margin, x=fcf_margin.index, y=fcf_margin.values,
                            title=f"{ticker.info['shortName']} Quarterly Free Cash Flow Margin", height=500)
    fcf_margin_bar.update_layout(xaxis_title='Quarter', yaxis_title='Margin')
    fcf_margin_bar.update_xaxes(tickvals=fcf_margin.index, ticktext=ticks)
    fcf_margin_bar.show()

# get_fcf_margin_q(ticker=ticker, income=income_q, cashflow=cashflow_q, ticks=quarters)


def get_oi_growth(ticker, income, ticks):
    # Graph Operating Income Growth for the previous 3 years
    loop = 1
    oig_list = []
    for oi in income.OperatingIncome.values:
        previous_oi = oi
        if loop >= 2:
            oig = (current_oi - previous_oi) / abs(previous_oi)
            oig_list.append(oig)
        loop += 1
        current_oi = oi
    # Create operating income growth dataframe
    oig = pd.DataFrame({'Operating Income Growth': oig_list}, index=income.index[:len(oig_list)])

    oig_bar = px.bar(oig, x=oig.index, y='Operating Income Growth',
                     title=f"{ticker.info['shortName']} Yearly Operating Income Growth",
                     height=500)
    oig_bar.update_layout(xaxis_title='Date')
    oig_bar.update_xaxes(tickvals=oig.index, ticktext=ticks)
    oig_bar.show()


def get_oi_q_growth(ticker, income, ticks):
    # Graph Quarterly Operating Income Growth
    loop = 1
    oig_list = []
    for oi in income.OperatingIncome.values:
        previous_oi = oi
        if loop >= 2:
            oig = (current_oi - previous_oi) / abs(previous_oi)
            oig_list.append(oig)
        loop += 1
        current_oi = oi
    # Create quarterly operating income growth dataframe
    oig = pd.DataFrame({'Operating Income Growth': oig_list}, index=income.index[:len(oig_list)])
    # Drop null values
    oig = oig.dropna()

    oig_q_bar = px.bar(oig, x=oig.index, y='Operating Income Growth',
                       title=f"{ticker.info['shortName']} Quarterly Operating Income Growth",
                       height=500)
    oig_q_bar.update_layout(xaxis_title='Quarter')
    oig_q_bar.update_xaxes(tickvals=oig.index, ticktext=ticks)
    oig_q_bar.show()

def get_operating_margin(ticker, income, ticks):
    # Graph yearly operating margin
    om = (income.OperatingIncome / income.TotalRevenue) * 100

    om_bar = px.bar(om, x=om.index, y=om.values, title=f"{ticker.info['shortName']} Yearly Operating Margin",
                   height=500)
    om_bar.update_layout(xaxis_title='Date', yaxis_title='Operating Margin')
    om_bar.update_xaxes(tickvals=income.index, ticktext=ticks)
    om_bar.show()
    return om

def get_om_trend(ticker, om_data, ticks):
    #Graph operating margin change
    loop = 1
    omt_list = []
    for om in om_data.values:
        previous_om = om
        if loop >= 2:
            omt = current_om - previous_om
            omt_list.append(omt)
        loop += 1
        current_om = om
    # Make new dataframe
    om_trend = pd.DataFrame({'Operating Margin Trend': omt_list}, index=ticks[:len(omt_list)])

    om_trend_bar = px.bar(om_trend, x=om_trend.index, y='Operating Margin Trend', title=f"{ticker.info['shortName']} Yearly Operating Margin Trend",
                          height=500)
    om_trend_bar.update_layout(xaxis_title='Date')
    om_trend_bar.update_xaxes(tickvals=om_trend.index, ticktext=ticks)
    om_trend_bar.show()

def get_operating_margin_q(ticker, income, ticks):
    # Graph yearly operating margin
    om_q = (income.OperatingIncome / income.TotalRevenue) * 100
    om_q = om_q.dropna()
    om_bar = px.bar(om_q, x=om_q.index, y=om_q.values, title=f"{ticker.info['shortName']} Quarterly Operating Margin",
                   height=500)
    om_bar.update_layout(xaxis_title='Date', yaxis_title='Operating Margin')
    om_bar.update_xaxes(tickvals=income.index, ticktext=ticks)
    om_bar.show()
    return om_q

def get_om_q_trend(ticker, om_data, ticks):
    #Graph quarterly operating margin change
    loop = 1
    omt_list = []
    for om in om_data.values:
        previous_om = om
        if loop >= 2:
            omt = current_om - previous_om
            omt_list.append(omt)
        loop += 1
        current_om = om
    # Make new dataframe
    om_trend = pd.DataFrame({'Operating Margin Trend': omt_list}, index=ticks[:len(omt_list)])

    om_trend_bar = px.bar(om_trend, x=om_trend.index, y='Operating Margin Trend',
                          title=f"{ticker.info['shortName']} Quarterly Operating Margin Trend", height=500)
    om_trend_bar.update_layout(xaxis_title='Quarter')
    om_trend_bar.update_xaxes(tickvals=om_trend.index, ticktext=ticks)
    om_trend_bar.show()

def get_gross_margin(ticker, income, ticks):
    #Graph yearly gross margin
    income['Gross Margin'] = income.GrossProfit / income.TotalRevenue

    grossmargin_bar = px.bar(income, x=income.index, y='Gross Margin',
                             title=f"{ticker.info['shortName']} Yearly Gross Margin",
                             height=500)
    grossmargin_bar.update_layout(xaxis_title='Date')
    grossmargin_bar.update_xaxes(tickvals=income.index, ticktext=ticks)
    grossmargin_bar.show()

def get_gross_q_margin(ticker, income, ticks):
    #Graph quarterly gross margin
    gross_margin = income.GrossProfit / income.TotalRevenue
    gross_margin = gross_margin.dropna()

    grossmargin_q_bar = px.bar(gross_margin, x=gross_margin.index, y=gross_margin.values,
                               title=f"{ticker.info['shortName']} Quarterly Gross Margin",
                             height=500)
    grossmargin_q_bar.update_layout(xaxis_title='Quarter', yaxis_title='Gross Margin')
    grossmargin_q_bar.update_xaxes(tickvals=income.index, ticktext=ticks)
    grossmargin_q_bar.show()
