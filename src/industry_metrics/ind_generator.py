# Used to create columns in industry_labels.csv
from scraping.yfinance_scraper import get_industries
import shutil
import sqlite3

# Columns for reference
# db_columns = ['Industry', 'pb_ratio', 'de_ratio', 'yoy_revenue', 'gross_margin', 'ttmpe', 'forwardpe']
conn = sqlite3.connect('../../data/blank_templates/industry_blank.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS industries")
cursor.execute("""CREATE TABLE IF NOT EXISTS industries (
               Industry TEXT NOT NULL,
               pb_ratio INTEGER,
               de_ratio INTEGER,
               revenue_growth INTEGER,
               gpm INTEGER,
               ttmpe INTEGER,
               forwardpe INTEGER)""")

sectors, industries = get_industries()
industry_list =[]
for industry in industries.values():
    for i in industry:
        industry_list.append(i)

rows = [(i,) for i in industry_list]
cursor.executemany("INSERT INTO industries (Industry) Values (?)", rows)
conn.commit()
# Copy template to blank db
shutil.copy(src='../../data/blank_templates/industry_blank.db', dst='../../data/industry_averages.db')
conn.close()