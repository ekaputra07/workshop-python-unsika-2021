# Package / Paket = kumpulan file Python, kumpulan module yang kita bisa pakai berulang-ulang, bisa diinstall
# Package bisa dibuat oleh siapa saja dan bisa digunakan oleh siapa saja
# Paket bisa diupload ke Python Package Index: https://pypi.org/, orang lain bisa download (install) dan menggunakannya.

# 1. Cara instalasi Package dengan `pip` (Package Installer for Python)
# 2. Cara menggunakan pip dengan requirements.txt
# 3. Mengimport dan menggunakan Package
import requests

hasil = requests.get('https://www.upkoding.com')

print(hasil.status_code)
print(hasil.text)
