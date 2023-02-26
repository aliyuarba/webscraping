import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
arr = []

tahun = np.arange(2011,2023)
pemda = np.arange(1, 36)
for t in tahun: 
  for p in pemda: 
    # Mengirimkan permintaan GET ke URL yang ditentukan
    url = "https://djpk.kemenkeu.go.id/portal/data/apbd?tahun={}&provinsi=11&pemda={:02d}".format(t,p)
    
    response = requests.get(url)

    # Menggunakan BeautifulSoup untuk memproses HTML dan menyimpannya dalam variabel soup
    soup = BeautifulSoup(response.content, 'lxml')

    # Mencari elemen yang ingin diambil dari halaman web
    wil = soup.find('label', id='wilayah')
    tabel = soup.find('tbody')
    for tr in tabel.find_all('tr'):
      rows = [t,wil.text]
      if tr.text.strip() != "":
        for td in tr.find_all('td'):
          if td.text.strip() != "":
            rows.append(td.text)
        arr.append(rows)

# Membuat DataFrame dari array
df = pd.DataFrame(arr)

# Menyimpan DataFrame ke dalam file CSV
df.to_csv('jateng11-22.csv', index=False)

# Menampilkan DataFrame
print(df)
