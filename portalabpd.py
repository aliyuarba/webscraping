import requests
from bs4 import BeautifulSoup

# Mengirimkan permintaan GET ke URL yang ditentukan
url = "https://djpk.kemenkeu.go.id/portal/data/apbd?tahun=2022&provinsi=11&pemda=21"
response = requests.get(url)

# Menggunakan BeautifulSoup untuk memproses HTML dan menyimpannya dalam variabel soup
soup = BeautifulSoup(response.content, 'lxml')

# Mencari elemen yang ingin diambil dari halaman web
tabel = soup.find('tbody')

# Menampilkan hasil
print(tabel.prettify())
