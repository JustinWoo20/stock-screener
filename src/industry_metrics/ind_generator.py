# Used to create columns in industry_labels.csv
import csv
from scraping.yfinance_scraper import get_industries
file_header = ['', 'P/B', 'D/E', 'Y/Y', 'Revenue Growth', 'Gross Profit Margin', 'Trailing P/E', 'Forward P/E']

sectors, industries = get_industries()
industry_list =[]
for industry in industries.values():
    for i in industry:
        industry_list.append(i)

with open('../../data/blank_templates/industry_labels.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(file_header)
    for item in industry_list:
        writer.writerow([item])