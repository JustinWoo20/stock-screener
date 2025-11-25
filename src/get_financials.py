import yfinance as yf

def get_ticker(stock_symbol):
    stock = yf.Ticker(stock_symbol)
    return stock
ticker = get_ticker(stock_symbol='FICO')

def financial_statements(ticker):
    income_yearly = ticker.get_income_stmt()
    income_yearly = income_yearly.transpose()
    income_quarterly = ticker.get_income_stmt(freq='quarterly')
    income_quarterly = income_quarterly.transpose()
    balance_yearly = ticker.get_balance_sheet()
    balance_yearly = balance_yearly.transpose()
    balance_quarterly = ticker.get_balance_sheet(freq='quarterly')
    balance_quarterly = balance_quarterly.transpose()
    cashflow_yearly = ticker.get_cash_flow()
    cashflow_yearly = cashflow_yearly.transpose()
    cashflow_quarterly = ticker.get_cash_flow(freq='quarterly')
    cashflow_quarterly = cashflow_quarterly.transpose()
    return income_yearly, income_quarterly, balance_yearly, balance_quarterly, cashflow_yearly, cashflow_quarterly
income_y, income_q, balance_y, balance_q, cashflow_y, cashflow_q = financial_statements(ticker)

def useful_variables(year_data, quarter_data):
    years = year_data.index.tolist()
    years = [d.strftime('%Y-%m-%d') for d in years]
    quarters = quarter_data.index.to_period('Q').astype(str)
    return years, quarters
years, quarters = useful_variables(income_y, income_q)