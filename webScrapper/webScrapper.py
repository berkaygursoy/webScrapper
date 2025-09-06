import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://example.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

basliks = soup.find_all("span")

titles = [h.get_text(strip=True) for h in basliks]

df = pd.DataFrame(titles, columns=["Başlıklar"])
df.to_excel("example_basliklar.xlsx", index=False)

print("Haber başlıkları 'exapmle_basliklar.xlsx' dosyasına kaydedildi.")
