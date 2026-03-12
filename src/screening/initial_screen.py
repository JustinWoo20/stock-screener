import yfinance as yf
import pandas as pd

def choose_category():
    # Choose to import sector or industry data
    category = input('Would you like to screen by sector or industry?\n'
                     'Please type "Sector" or "Industry"\n').title()
    if category == 'Sector':
        data = pd.read_csv('../data/sector_averages.csv', index_col=0)
    elif category == 'Industry':
        data = pd.read_csv('../data/industry_averages.csv', index_col=0)
    else:
        print('Please enter a valid input')
        return None

    cols = ['P/B', 'D/E', 'Y/Y Revenue Growth', 'Gross Profit Margin', 'Trailing P/E', 'Forward P/E', ]
    data[cols] = data[cols].apply(pd.to_numeric, errors='coerce')
    return data, category

def screen_stocks(averages, ind_sec):
    #Initial screen to find possible undervalued stocks
    if ind_sec == 'Sector':
        target = input("Enter your target sector: \n").title()

    elif ind_sec == 'Industry':
        target = input('Enter your target industry: \n')
    ind_sec = ind_sec.lower()

    query = yf.EquityQuery('and', [
        yf.EquityQuery('is-in', ['exchange', 'NYQ', 'NMS', 'ASE', 'NCM']),
        yf.EquityQuery('is-in', [f'{ind_sec}', f"{target}"]),
        yf.EquityQuery('LT', ['pricebookratio.quarterly', averages.loc[f"{target}", 'P/B']]),
        yf.EquityQuery('LT', ['totaldebtequity.lasttwelvemonths', averages.loc[f"{target}", 'D/E']]),
        yf.EquityQuery('GTE', ['totalrevenues1yrgrowth.lasttwelvemonths',
                               averages.loc[f"{target}", 'Y/Y Revenue Growth']]),
        yf.EquityQuery('GTE', ['grossprofitmargin.lasttwelvemonths',
                               averages.loc[f"{target}", 'Gross Profit Margin']]),
        yf.EquityQuery('GTE', ['altmanzscoreusingtheaveragestockinformationforaperiod.lasttwelvemonths', 2.8]),
    ])

    # Create a list of stock tickers from screened stocks
    response = yf.screen(query, sortField='pricebookratio.quarterly', sortAsc=True, size=100)
    print(f'Number of stocks retrieved: {response['total']}')
    data = response['quotes']
    try:
        stock_dict = {stocks['displayName']: stocks['symbol'] for stocks in data}
    except KeyError:
        stock_dict = {stocks['shortName']: stocks['symbol'] for stocks in data}

    return stock_dict, target

