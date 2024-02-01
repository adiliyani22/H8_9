#!/usr/bin/env python
# coding: utf-8

# In[4]:


age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

print (age, Age, aGe, AGE, a_g_e, _age, age_, _AGE_)


# In[ ]:





# In[10]:


a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print (a[1])


# In[12]:


MLB_team = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners'
}

print(MLB_team['Minnesota'])
print(MLB_team['Colorado'])


# In[40]:


a = 2
b = 3
c = 1

if a > c:
    print(a)
if a < b:
    print("Betul")


# In[41]:


if a > b or a > c:
    print('Tampil')


# In[45]:


if (a > b) & (a > c):
    print ('tampil')
else :
    print('gak')


# In[60]:


sistem =['saya', 'pergi', 'ke', 'lppi', 'kemang']
engineer = ['tidak', 'jualan', 'karena', 'banjir']
engineer[0] = 'tetap'

print (sistem[0], engineer[0], sistem[1], engineer[2], engineer[3])


# In[77]:


a = 6
b = 7
c = 8

if (c > a):
    if (b > c):
        print("True")
    else:
        print("False")


# In[83]:


nama_satu = [80, 70]
nama_dua = [55, 70]
nama_tiga = [80, 90]
nama_empat = [75, 60]
nama_lima = [90, 70]

batas_lulus = 150

def tentukan_kategori(jumlah_nilai):
    if jumlah_nilai >= batas_lulus:
        return "LULUS"
    else:
        return "GAGAL"

for i, nilai_siswa in enumerate([nama_satu, nama_dua, nama_tiga, nama_empat, nama_lima], start=1):
    jumlah_nilai = sum(nilai_siswa)
    print(f"Nilai siswa ke-{i}: {nilai_siswa}")
    print("Jumlah Nilai Siswa: ", jumlah_nilai)
    print("Kategori: ", tentukan_kategori(jumlah_nilai))
    print()


# In[84]:


nama_satu = [80, 70]
nama_dua = [55, 70]
nama_tiga = [80, 90]
nama_empat = [75, 60]
nama_lima = [90, 70]

def tentukan_kategori(nilai_siswa):
    if all(nilai >= 60 for nilai in nilai_siswa):
        return "LULUS"
    else:
        return "GAGAL"

for i, nilai_siswa in enumerate([nama_satu, nama_dua, nama_tiga, nama_empat, nama_lima], start=1):
    print(f"Nilai siswa ke-{i}: {nilai_siswa}")
    print("Kategori: ", tentukan_kategori(nilai_siswa))
    print()


# In[90]:


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


# In[94]:


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


# In[120]:


# Menerima input desimal dari pengguna
decimal_input = int(input("Masukkan nilai desimal: "))

# Mengonversi desimal ke biner, oktal, heksadesimal, dan ASCII
binary_value = bin(decimal_input)[2:]
octal_value = oct(decimal_input)[2:]
hexadecimal_value = hex(decimal_input)[2:]
ascii_value = chr(decimal_input)
#ascii_values = [ord(char) for char in decimal_input]  # Mengonversi setiap karakter ke ASCII

# Menampilkan hasil konversi
print("Nilai biner:", binary_value)
print("Nilai oktal:", octal_value)
print("Nilai heksadesimal:", hexadecimal_value)
print("Nilai ASCII:", ascii_value)


# In[121]:


# Menerima input huruf dari pengguna
input_huruf = input("Masukkan huruf: ")

# Menampilkan nilai desimal
for huruf in input_huruf:
    decimal_value = ord(huruf)
    print(f"Karakter '{huruf}' memiliki nilai desimal: {decimal_value}")

# Menampilkan nilai biner, oktal, heksadesimal, dan ASCII
binary_values = [bin(ord(huruf))[2:] for huruf in input_huruf]
octal_values = [oct(ord(huruf))[2:] for huruf in input_huruf]
hexadecimal_values = [hex(ord(huruf))[2:] for huruf in input_huruf]
ascii_values = [ord(huruf) for huruf in input_huruf]

# Menampilkan hasil konversi
print("Nilai Biner:", binary_values)
print("Nilai Okta:", octal_values)
print("Nilai Heksadesimal:", hexadecimal_values)
print("Nilai ASCII:", ascii_values)

