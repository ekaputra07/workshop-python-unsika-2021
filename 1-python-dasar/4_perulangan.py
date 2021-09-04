# 1. Perulangan menggunakan for-in (list | string)
array = [1,2,3,4,5,6]
for angka in array:
    print(angka)

for huruf in "Hello Python":
    print(huruf)

# 2. Perulangan menggunakan for-in-range(x)
for angka in range(3):
    print(angka)

# 3. Perulangan menggunakan for-in-range(x, y)
for angka in range(10, 15):
    print(angka)

# 4. Perulangan menggunakan `while`
angka = 1
while angka < 10:
    print(angka)
    angka += 1
    
# 5. Perulangan `break`
angka = 1
while angka < 10:
    print(angka)
    angka += 1
    if angka == 5:
        break

print('--')

# 6. Perulangan `continue`
angka = 1
while angka < 10:
    angka += 1
    if angka == 2:
        continue
    print(angka)

