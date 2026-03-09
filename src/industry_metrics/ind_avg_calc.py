import csv
import time
import yfinance as yf

def get_totals(ticker_dict):
    # Calculate numerators for each metric
    total_pb = 0
    missing_pb = 0
    total_de = 0
    missing_de = 0
    total_rev_growth = 0
    missing_rev_growth = 0
    total_gpm = 0
    missing_gpm = 0
    total_trailing_pe = 0
    missing_trailing_pe = 0
    total_forward_pe = 0
    missing_forward_pe = 0
    # Create a ticker object for each stock
    for symbol in ticker_dict.values():
        ticker = yf.Ticker(symbol)
        ticker_info = ticker.info
        # Calculate the numerator for each metric
        try:
            pb = ticker_info['priceToBook']
            total_pb += pb
        except KeyError:
            missing_pb += 1

        try:
            de = ticker_info['debtToEquity']
            total_de += de
        except KeyError:
            missing_de += 1

        try:
            rev_growth = ticker_info['revenueGrowth']
            total_rev_growth += rev_growth
        except KeyError:
            missing_rev_growth += 1

        try:
            gpm = ticker_info['grossMargins']
            total_gpm += gpm
        except KeyError:
            missing_gpm += 1

        try:
            trailing_pe = ticker_info['trailingPE']
            total_trailing_pe += trailing_pe
        except KeyError:
            missing_trailing_pe += 1
        except TypeError:
            missing_trailing_pe += 1

        try:
            forward_pe = ticker_info['forwardPE']
            total_forward_pe += forward_pe
        except KeyError:
            missing_forward_pe += 1
        except TypeError:
            missing_forward_pe += 1

    numerator_dict = {'total_pb': total_pb, 'total_de': total_de, 'total_rev_growth': total_rev_growth,
                      'total_gpm': total_gpm, 'total_trailing_pe': total_trailing_pe,
                      'total_forward_pe': total_forward_pe, }

    denominator_dict = {'missing_pb': missing_pb, 'missing_de': missing_de, 'missing_rev_growth': missing_rev_growth,
                        'missing_gpm': missing_gpm, 'missing_trailing_pe': missing_trailing_pe,
                        'missing_forward_pe': missing_forward_pe}

    return numerator_dict, denominator_dict

def calculate_denominators(sums_dict, ticker_dict):
    pb_denominator = len(ticker_dict) - sums_dict['missing_pb']
    de_denominator = len(ticker_dict) - sums_dict['missing_de']
    rev_denominator = len(ticker_dict) - sums_dict['missing_rev_growth']
    gpm_denominator = len(ticker_dict) - sums_dict['missing_gpm']
    trailing_pe_denominator = len(ticker_dict) - sums_dict['missing_trailing_pe']
    forward_pe_denominator = len(ticker_dict) - sums_dict['missing_forward_pe']
    denominators_dict = {'pb': pb_denominator, 'de': de_denominator, 'rev_growth': rev_denominator,
                         'gpm': gpm_denominator, 'trailing_pe': trailing_pe_denominator,
                         'forward_pe': forward_pe_denominator}
    return denominators_dict

def get_names(ticker):
    try:
        name = ticker['shortName']
        print(name)
    except KeyError:
        name = ticker['longName']
        print(name)
    except:
        name = ticker['displayName']
        print(name)
    return name

rows_to_add = []

with open('../../data/blank_templates/industry_labels.csv') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    rows = list(reader)
    for r in rows:
        ind = r[0]
        # Query finding stocks in various American stock exchanges
        try:
            query = yf.EquityQuery('and', [
            yf.EquityQuery('is-in', ['exchange', 'NYQ', 'NMS', 'ASE', 'NCM']),
            yf.EquityQuery('is-in', ['industry', f"{ind}"])],)
        except ValueError:
            r = [f"{ind}", 0, 0, 0, 0, 0, 0]
            rows_to_add.append(r)
            continue
        # Run the stock query
        response = yf.screen(query, size=250)
        print(f'Number of stocks retrieved in {ind}: {response["total"]}')
        data = response['quotes']
        # Create a dictionary with names and tickers
        stock_dict = {get_names(ticker=stocks): stocks['symbol'] for stocks in data}
        print(stock_dict)
        # Call functions to get numerator and denominators
        numerators, missing_values = get_totals(ticker_dict=stock_dict)
        denominators = calculate_denominators(sums_dict=missing_values, ticker_dict=stock_dict)
        #  Calculate averages
        averages = [num / den if den!=0  else None for num, den in zip(numerators.values(), denominators.values())]
        rows_to_add.append([ind] + averages)
        time.sleep(1) # Prevent errors with yahoo finance

with open('../../data/industry_averages.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    for r in rows_to_add:
        writer.writerow(r)
