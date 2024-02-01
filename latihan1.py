#Tugas 1

sistem =['saya', 'pergi', 'ke', 'lppi', 'kemang']
engineer = ['tidak', 'jualan', 'karena', 'banjir']
engineer[0] = 'tetap'

print (sistem[0], engineer[0], sistem[1], engineer[2], engineer[3])

#Tugas 2

a = 6
b = 7
c = 8

if (c > a):
    if (b > c):
        print("True")
    else:
        print("False")

# Tugas siswa
nama_satu = [80, 70]
nama_dua = [55, 70]
nama_tiga = [80, 90]
nama_empat = [75, 60]
nama_lima = [90, 70]

def tentukan_kategori(nilai_siswa):
    if all(nilai > 60 for nilai in nilai_siswa):
        return "LULUS"
    else:
        return "GAGAL"

for i, nilai_siswa in enumerate([nama_satu, nama_dua, nama_tiga, nama_empat, nama_lima], start=1):
    print(f"Nilai siswa ke-{i}: {nilai_siswa}")
    print("Kategori: ", tentukan_kategori(nilai_siswa))
    print()

# Tugas UAS

name = input("Masukkan nama : ")
hobby = input("Masukkan hobby : ")
email = input("Masukkan email : ")
telp = input("Masukkan no. tlp : ")
nilai = int(input("Masukkan nilai : ")) 


if nilai >= 70:
    status = "LULUS"
else:
    status = "GAGAL"


print("\nRekap Informasi Siswa:")
print("Nama   :", name)
print("Hobby  :", hobby)
print("Email  :", email)
print("No. Tlp:", telp)
print("Nilai  :", nilai)
print("Status :", status)

#Tugas UTS UAS

name = input("Masukkan nama : ")
hobby = input("Masukkan hobby : ")
email = input("Masukkan email : ")
telp = input("Masukkan no. tlp : ")
nilaiuts = int(input("Masukkan nilai UTS : "))
nilaiuas = int(input("Masukkan nilai UAS : "))


if (nilaiuts + nilaiuas) <= 125:
    status = 'Gagal'
elif nilaiuts <= 60 or nilaiuas <= 60 :
    status = 'Gagal'
else:
    status = 'LULUS'



print("\nRekap Informasi Siswa:")
print("Nama       :", name)
print("Hobby      :", hobby)
print("Email      :", email)
print("No. Tlp    :", telp)
print("Nilai UTS    :", nilaiuts)
print("Nilai UAS    :", nilaiuas)
print("Status     :", status)

# Tugas Biner

input_huruf = input("Masukkan huruf: ")

for huruf in input_huruf:
    decimal_value = ord(huruf)
    print(f"Karakter '{huruf}' memiliki nilai desimal: {decimal_value}")

binary_values = [bin(ord(huruf))[2:] for huruf in input_huruf]
octal_values = [oct(ord(huruf))[2:] for huruf in input_huruf]
hexadecimal_values = [hex(ord(huruf))[2:] for huruf in input_huruf]
ascii_values = [ord(huruf) for huruf in input_huruf]

print("Nilai Biner:", binary_values)
print("Nilai Okta:", octal_values)
print("Nilai Heksadesimal:", hexadecimal_values)
print("Nilai ASCII:", ascii_values)


# Tugas Perulangan

s = 12

while s <= 19:
    if s <= 15:
        print(s)
    elif s > 18:
        print("Selesai")
        print(s)
    s += 1