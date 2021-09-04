# 1. Kondisi selalu berdasarkan logika Benar atau Salah (True atau False)

# 2. Kondisi menggunakan `==`
angka = 10
if angka == 10:
    print('Hello Python')


# 3. Kondisi menggunakan `and`
angka2 = 12
if angka == 10 and angka2 == 12:
    print('Hello Python2')

# 4. Kondisi menggunakan `or`
angka3 = 15
if angka == 10 or angka3 == 13:
    print('Hello Python3')

# 5. Kondisi menggunakan `is` dan `is not`

# 6. Kondisi menggunakan `in` untuk (string | list)
array = [1,2,3,4,5,6]

if 5 in array:
    print("5 ada di array")

if "P" in "Python":
    print("P ada di Python")

# 7. Multi-Kondisi menggunakan if-elif-else
umur = 18
if umur == 17:
    print('umur 17')
else:
    print('umur bukan 17')


umur = 59
if umur > 50:
    print('umur > 50')
    if umur == 60:
        print('hore saya 60')
elif umur < 50:
    print('umur < 50')
else:
    print('umur 50')