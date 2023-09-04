# Meminta pengguna untuk memasukkan suhu dalam fahrenheit
fahrenheit = int(input("Masukkan suhu dalam Fahrenheit: "))

# Menghitung suhu dalam Celcius
celcius = (fahrenheit - 32) * 5/9

# Menampilkan hasil konversi
print(fahrenheit, 'Derajat Fahrenheit = ', celcius, 'Derajat Celcius')