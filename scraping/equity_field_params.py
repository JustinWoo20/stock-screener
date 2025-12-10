# TODO: Peer group
import re
import requests
from bs4 import BeautifulSoup

# Fetch yfinance api page
url = 'https://ranaroussi.github.io/yfinance/reference/api/yfinance.EquityQuery.html'
response = requests.get(url)
print(response.status_code)

# Parse
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find(id='id2')
body = table.find('tbody')

# Final all p elements
p_elements = body.find_all('p')

# Find all div elements with the class line
line_classes = body.find_all(class_='line')
# Use splicing to obtain only exchanges
exchange_divs = line_classes[:20]
industry_divs = line_classes[20:]
print(industry_divs)

def get_regions():
    # Obtain possible regions from yfinance documentation
    text = p_elements[1].get_text()
    split_text = text.split(sep=', ')
    return split_text

def get_exchanges():
    # Obtain possible exchanges from yfinance documentation
    exchange_list = []
    for e in exchange_divs:
        text = e.get_text()
        codes = re.findall(r'\b[A-Z]{2,}\b', text)
        for c in codes:
            exchange_list.append(c)

    return exchange_list

def get_industries():
    # Get a dictionary of industries from yfinance website
    sector_list = []
    industry_dict = {}
    for i in industry_divs:
        text = i.get_text(strip=True)
        sector, industries = text.split(': ')
        industries = industries.split(', ')
        industry_dict[sector] = industries
        sector_list.append(sector)

    return sector_list, industry_dict



# import re
# s = "Geeks, for; Geeks"
#
# # Using split() with a capturing group to keep the delimiters
# result = re.split(r'(,|;)', s)
#
# print(result)
#codes = re.findall(r'\b[A-Z]{2,}\b', text)

