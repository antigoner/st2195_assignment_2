import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO
import requests
url = "https://en.wikipedia.org/wiki/Delimiter-separated_values"
session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0', "Accept-Language": "en-US,en;q=0.5"})
response = session.get(url,timeout=10)
response_content = response.content
soup = BeautifulSoup(response_content, 'html.parser')
table = soup.find('pre')
table_text = table.text
print(table_text)
df = pd.read_csv(StringIO(table_text))
df.to_csv('pythoncsv.csv')
