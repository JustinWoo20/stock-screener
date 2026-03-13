# Used to create columns in sector_blank.db
from scraping.yfinance_scraper import get_industries
import shutil
import sqlite3

# Columns for reference
# db_columns = ['Industry', 'pb_ratio', 'de_ratio', 'yoy_revenue', 'gross_margin', 'ttmpe', 'forwardpe']
conn = sqlite3.connect('../../data/blank_templates/sector_blank.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS sectors")
cursor.execute("""CREATE TABLE IF NOT EXISTS sectors (
               Sector TEXT NOT NULL,
               pb_ratio INTEGER,
               de_ratio INTEGER,
               yoy_revenue INTEGER,
               gross_margin INTEGER,
               ttmpe INTEGER,
               forwardpe INTEGER)""")

sectors, industries = get_industries()

rows = [(s,) for s in sectors]
cursor.executemany("INSERT INTO sectors (Sector) Values (?)", rows)
conn.commit()
print(cursor.execute("SELECT Sector FROM sectors").fetchall())
# Copy template to blank db
shutil.copy(src='../../data/blank_templates/sector_blank.db', dst='../../data/sector_averages.db')
conn.close()