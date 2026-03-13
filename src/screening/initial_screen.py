import sqlite3
import yfinance as yf

def get_names(ticker):
    name = (ticker.get('shortName') or
            ticker.get('longName') or
            ticker.get('displayName') or
            'Unknown')
    return name

def choose_category():
    # Choose to import sector or industry data
    category = input('Would you like to screen by sector or industry?\n'
                     'Please type "Sector" or "Industry"\n').title()
    if category == 'Sector':
        conn = sqlite3.connect('../data/sector_averages.db')

    elif category == 'Industry':
        conn = sqlite3.connect('../data/industry_averages.db')

    else:
        print('Please enter a valid input')
        return None

    cursor = conn.cursor()

    return conn, cursor, category

def screen_stocks(cur, ind_sec):
    #Initial screen to find possible undervalued stocks
    if ind_sec == 'Sector':
        target = input("Enter your target sector: \n").title()
        row = cur.execute("""SELECT pb_ratio, de_ratio, yoy_revenue, gross_margin, ttmpe, forwardpe 
                                FROM sectors WHERE Sector = ?""", (target,)).fetchone()
    elif ind_sec == 'Industry':
        target = input('Enter your target industry: \n')
        row = cur.execute("""SELECT pb_ratio, de_ratio, yoy_revenue, gross_margin, ttmpe, forwardpe 
                                FROM industries WHERE Industry = ?""", (target,)).fetchone()
    else:
        print('Please enter a valid input')
        return None

    pb, de, rev, grossmarg, ttmpe, forwardpe = row

    ind_sec = ind_sec.lower()


    query = yf.EquityQuery('and', [
        yf.EquityQuery('is-in', ['exchange', 'NYQ', 'NMS', 'ASE', 'NCM']),
        yf.EquityQuery('is-in', [f'{ind_sec}', f"{target}"]),
        yf.EquityQuery('LT', ['pricebookratio.quarterly', pb]),
        yf.EquityQuery('LT', ['totaldebtequity.lasttwelvemonths', de]),
        yf.EquityQuery('GTE', ['totalrevenues1yrgrowth.lasttwelvemonths', rev]),
        yf.EquityQuery('GTE', ['grossprofitmargin.lasttwelvemonths',grossmarg]),
        yf.EquityQuery('GTE', ['altmanzscoreusingtheaveragestockinformationforaperiod.lasttwelvemonths', 2.8]),
    ])

    # Create a list of stock tickers from screened stocks
    response = yf.screen(query, sortField='pricebookratio.quarterly', sortAsc=True, size=100)
    print(f'Number of stocks retrieved: {response['total']}')
    data = response['quotes']
    stock_dict = {get_names(stocks): stocks['symbol'] for stocks in data}

    return stock_dict, target, ttmpe, forwardpe
