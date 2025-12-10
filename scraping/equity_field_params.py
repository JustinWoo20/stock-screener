import re
import requests
from bs4 import BeautifulSoup

# Fetch yfinance api page
url = 'https://ranaroussi.github.io/yfinance/reference/api/yfinance.EquityQuery.html'
response = requests.get(url)

# Parse
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find(id='id2')
tbody = table.find('tbody')

# Find all div elements with the class line
line_classes = tbody.find_all(class_='line')

def get_regions():
    # Obtain possible regions from yfinance documentation
    p_elements = tbody.find_all('p')
    text = p_elements[1].get_text()
    split_text = text.split(sep=', ')
    return split_text

def get_exchanges():
    # Obtain possible exchanges from yfinance documentation
    exchange_divs = line_classes[:20]
    exchange_list = []
    for e in exchange_divs:
        text = e.get_text()
        codes = re.findall(r'\b[A-Z]{2,}\b', text)
        for c in codes:
            exchange_list.append(c)

    return exchange_list

def get_industries():
    # Get a dictionary of industries from yfinance website
    industry_divs = line_classes[20:]
    sector_list = []
    industry_dict = {}
    for i in industry_divs:
        text = i.get_text(strip=True)
        sector, ind = text.split(': ')
        industries_split = ind.split(', ')
        industry_dict[sector] = industries_split
        sector_list.append(sector)

    return sector_list, industry_dict

def get_peer_groups():
    # Obtain a dictionary of yfinance peer groups
    simple_classes = tbody.find_all(class_='simple')
    simple_cl_txt = simple_classes[1].get_text()
    split_txt = simple_cl_txt.split('\n')
    peer_group_list = split_txt[1:len(split_txt) - 1]
    return peer_group_list
