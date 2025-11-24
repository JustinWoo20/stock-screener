import yfinance as yf
import pandas as pd

# Import sector data for comparison
sector_data = pd.read_csv('../data/sector_averages.csv', index_col=0)
cols = ['P/B', 'D/E', 'Y/Y Revenue Growth (S&P)', 'Gross Profit Margin']
sector_data[cols] = sector_data[cols].apply(pd.to_numeric, errors='coerce')

sector_list = ['Basic Materials', 'Communication Services', 'Consumer Cyclical', 'Consumer Defensive',
               'Energy', 'Financial Services', 'Healthcare', 'Industrials', 'Real Estate', 'Technology', 'Utilities']

# Initial screener params
def screen_stocks():
    #Initial screen to find possible undervalued stocks
    target_sector = input("Enter the sector you are looking for from one of the following options: \n"
                          f"{sector_list}: \n").title()

    tech_query = yf.EquityQuery('and', [
    yf.EquityQuery('is-in', ['exchange', 'NYQ', 'NMS', 'ASE', 'NCM']),
    yf.EquityQuery('is-in', ['sector', f"{target_sector}"]),
    yf.EquityQuery('LT', ['pricebookratio.quarterly', sector_data.loc[f"{target_sector}", 'P/B']]),
    yf.EquityQuery('LT', ['totaldebtequity.lasttwelvemonths', sector_data.loc[f"{target_sector}", 'D/E']]),
    yf.EquityQuery('GTE', ['totalrevenues1yrgrowth.lasttwelvemonths', 4]),
    yf.EquityQuery('GTE', ['grossprofitmargin.lasttwelvemonths',
                           sector_data.loc[f"{target_sector}", 'Gross Profit Margin']]),
    yf.EquityQuery('GTE', ['altmanzscoreusingtheaveragestockinformationforaperiod.lasttwelvemonths', 2.8]),
                  ])

    # Create a list of stock tickers from screened stocks
    response = yf.screen(tech_query, sortField='pricebookratio.quarterly', sortAsc=True, size=100)
    print(f'Number of stocks retrieved: {response['total']}')
    data = response['quotes']
    try:
        stock_dict = {stocks['displayName']: stocks['symbol'] for stocks in data}
    except KeyError:
        stock_dict = {stocks['shortName']: stocks['symbol'] for stocks in data}

    print(stock_dict)

screen_stocks()