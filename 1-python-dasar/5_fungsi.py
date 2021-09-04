# 1. Fungsi sederhana
def hello():
    print('hello')

hello()

# 2. Fungsi dengan parameter
def hello_nama(nama):
    print(f'hello {nama}')

hello_nama('Python 3')

# 3. Fungsi dengan return value

def hello_nama2(nama):
    return f'hello {nama}'

nama = hello_nama2('Python 2')
print(nama)

# 4. Task: Buatlah sebuah fungsi untuk menghitung umur dengan parameter tahun lahir

def umur(tahun_lahir):
    return 2021 - tahun_lahir

umur_sekarang = umur(1990)
print(umur_sekarang)