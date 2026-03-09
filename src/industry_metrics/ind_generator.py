# Used to create columns in industry_labels.csv
import csv
from yfinance_scraper import get_industries

sectors, industries = get_industries()
industry_list =[]
for industry in industries.values():
    for i in industry:
        industry_list.append(i)

with open('../data/industry_averages.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for item in industry_list:
        writer.writerow([item])