# Get stocks in industry and take the average of each
import csv
import yfinance as yf

# sector = yf.Sector('technology')
# # print(sector.industries)
# industry = yf.Industry('agricultural-inputs')
# # print(industry.name)

# with open('data/industry_copy.csv') as csvfile:
#     industry_reader = csv.reader(csvfile)
#     next(industry_reader, None)
#     for row in industry_reader:
#         ind = row[0]
query = yf.EquityQuery('and', [
yf.EquityQuery('is-in', ['exchange', 'NYQ', 'NMS', 'ASE', 'NCM']),
yf.EquityQuery('is-in', ['industry', f"Agricultural Inputs"])],)

# Run the stock query
response = yf.screen(query, size=250)
data = response['quotes']
print(f'Number of stocks retrieved: {response["total"]}')
stock_dict = {stocks['shortName']: stocks['symbol'] for stocks in data}
print(stock_dict)
print(len(stock_dict))

# Calculate average P/B ratio per industry
total = 0
missing_pb = 0
for stock in stock_dict.values():
    # Find the sum of all the P/B ratios
    ticker = yf.Ticker(stock)
    ticker_info = ticker.info
    stock_symbol = ticker_info['shortName']
    try:
        pb = ticker_info['priceToBook']
        print(f"stock symbol: {stock_symbol}, PB: {pb}")
        total += pb
    except KeyError:
        print(f'stock symbol: {stock_symbol}, PB: No value found')
        missing_pb += 1
    # if pb is not None:
    #     total += ticker_info['priceToBook']
    # else:
    #     missing_pb += 1

print(missing_pb)
average_pb = total / len(stock_dict) - missing_pb # Divide by the number of stocks in the dictionary to find the average
# print(f"Industry: {ind}, P/B: {average_pb}")
print(average_pb)
