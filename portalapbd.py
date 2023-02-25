import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
arr = []

tahun = np.arange(2011, 2023)
for th in tahun: 

  # Mengirimkan permintaan GET ke URL yang ditentukan
  url = "https://djpk.kemenkeu.go.id/portal/data/apbd?tahun=2021&provinsi=11&pemda=21".format(th)
  response = requests.get(url)

  # Menggunakan BeautifulSoup untuk memproses HTML dan menyimpannya dalam variabel soup
  soup = BeautifulSoup(response.content, 'lxml')


  # Mencari elemen yang ingin diambil dari halaman web
  tabel = soup.find('tbody')
  for tr in tabel.find_all('tr'):
    rows = [th]
    if tr.text.strip() != "":
      for td in tr.find_all('td'):
        if td.text.strip() != "":
          rows.append(td.text)
      arr.append(rows)

# Membuat DataFrame dari array
df = pd.DataFrame(arr)

# Menyimpan DataFrame ke dalam file CSV
df.to_csv('pwr2011-2023.csv', index=False)

# Menampilkan DataFrame
print(df)
