import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://www.bls.gov/ooh/healthcare/print/home.htm")
soup = BeautifulSoup(page.content, 'html.parser')
on_print = soup.find(id="ooh-print-container")
printed_table = on_print.find_all(id="landing-page-table")

data = []
table = soup.find('table', attrs={'class': 'display'})
table_body = table.find('tbody')

rows = table_body.find_all('tr')
header_row = [td.get_text(strip=True) for td in rows[0].find_all('th')]
if header_row:
    rows.append(header_row)
    rows = rows[1:]
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])