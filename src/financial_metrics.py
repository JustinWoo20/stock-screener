from get_financials import ticker

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

def get_netincome_y(ticker, income, ticks):
    # Graphs yearly net income
    ni_year_bar = px.bar(income, x=income.index,
                         y='NetIncome', title=f'{ticker.info['shortName']} Yearly Net Income', height=500)
    ni_year_bar.update_layout(xaxis_title='Date', yaxis_title='Net Income')
    ni_year_bar.update_xaxes(tickvals=income.index,
                             ticktext=years)
    ni_year_bar.show()
get_netincome_y(ticker=ticker,income=income_y,ticks=years)