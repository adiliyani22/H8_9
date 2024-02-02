#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Membuat file txt

f = open("demofile.txt")

print(f.readline())

f.close()


# In[20]:


#Menampilkan kalimat pada txt

f = open("gitToday/puisi.txt")

print(f.readline())

f.close()


# In[30]:


#Menampilkan text pakai array

f = open("gitToday/puisi.txt")

puisi = f.readlines()
print(puisi[0])
print(puisi[1])

f.close()


# In[31]:


#Menambahkan kalimat

with open("gitToday/puisi.txt", 'a') as f:

    f.write("\nBaris tambahan untuk puisi.\n")

with open("gitToday/puisi.txt", 'r') as f:
    content = f.read()
    print(content)


# In[46]:


#Membuat text pada file .txt

f = open("gitToday/puisi.txt", 'w')

f.write("Pelatihan kita di LPPI Kemang\ndengan waktu yang telah ditentukan!!")
f.close()

f = open("gitToday/puisi.txt", 'r')
print(f.read())


# In[56]:


#Menambahkan text yang sudah ada

f = open("gitToday/puisi.txt", 'r+')
baca = f.readlines()
kalimat_tambahan = "dari pagi, sampai sore\n"
baca.insert(1, kalimat_tambahan)
f.seek(0)

f.writelines(baca)
f.seek(0)
print(f.read())


# In[94]:


#Input program Hitungan Desimal, Biner, Oktal, Hexa

print("Selamat Datang di Program Hitungan")
print("===================================")

nama = input("Nama : ")
ruang = input("Ruang : ")
skema = input("Skema : ")

teks = "Nama : {}\nRuang : {}\nSkema : {}\n".format(nama, ruang, skema)

f = open("gitToday/handling.txt", "a")
f.write(teks)

for char in nama:
    nilai_ascii = ord(char)
    nilai_desimal = nilai_ascii
    nilai_biner = bin(nilai_ascii)[2:]
    nilai_oktal = oct(nilai_ascii)[2:]
    nilai_heksa = hex(nilai_ascii)[2:]

    teks_perhitungan = "Huruf '{}' memiliki nilai ASCII: {}\n"\
                       "Nilai Desimal: {}\n"\
                       "Nilai Biner: {}\n"\
                       "Nilai Oktal: {}\n"\
                       "Nilai Heksadesimal: {}\n".format(char, nilai_ascii, nilai_desimal, nilai_biner, nilai_oktal, nilai_heksa)

    f.write(teks_perhitungan)
    print(teks_perhitungan)
    
f.close()


# In[95]:


#Install mysql connector

pip install mysql-connector-python


# In[129]:


#DATA ACAK

import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="root",
database="sakila"
)


mycursor = mydb.cursor()
mycursor.execute("select * from actor")
myresult = mycursor.fetchall()

for row in myresult:
    print (row)


# In[120]:


#INSERT TABEL

import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="root",
database="sakila"
)


mycursor = mydb.cursor()
mycursor.execute("INSERT INTO actor (first_name, last_name) VALUES ('Adi', 'Liyani')")
mycursor.execute("INSERT INTO actor (first_name, last_name) VALUES ('Kris', 'Ganteng')")
mydb.commit()
mycursor.execute("select * from actor")
myresult = mycursor.fetchall()

for row in myresult:
    print (row)


# In[99]:


#Install Pandas

pip install pandas openpyxl


# In[121]:


#Import Pandas (merapihkan tabel)

import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sakila"
)

mycursor = mydb.cursor()

#mycursor.execute("INSERT INTO actor (first_name, last_name) VALUES ('adi', 'liyani')")
#mydb.commit()
mycursor.execute("select * from actor")
myresult = mycursor.fetchall()

column_names = [i[0] for i in mycursor.description]
df = pd.DataFrame(myresult, columns=column_names)

print(df)


# In[122]:


#UPDATE TABEL

import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sakila"
)

mycursor = mydb.cursor()

#mycursor.execute("INSERT INTO actor (first_name, last_name) VALUES ('adi', 'liyani')")
#mydb.commit()

mycursor.execute("UPDATE actor SET first_name = 'ADI' WHERE actor_id = '208'")
mydb.commit()

mycursor.execute("select * from actor")
myresult = mycursor.fetchall()

column_names = [i[0] for i in mycursor.description]
df = pd.DataFrame(myresult, columns=column_names)

print(df)


# In[123]:


#DELETE TABEL

import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sakila"
)

mycursor = mydb.cursor()

#mycursor.execute("INSERT INTO actor (first_name, last_name) VALUES ('adi', 'liyani')")
#mydb.commit()

#mycursor.execute("UPDATE actor SET first_name = 'ADI' WHERE actor_id = '202'")
#mydb.commit()

mycursor.execute("DELETE FROM actor WHERE actor_id = 208")
mydb.commit()

mycursor.execute("select * from actor")
myresult = mycursor.fetchall()

column_names = [i[0] for i in mycursor.description]
df = pd.DataFrame(myresult, columns=column_names)

print(df)


# In[131]:


#Melihat tipedata

import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sakila"
)

mycursor = mydb.cursor()

#mycursor.execute("INSERT INTO actor (first_name, last_name) VALUES ('adi', 'liyani')")
#mydb.commit()
mycursor.execute("select * from actor")
myresult = mycursor.fetchall()

column_names = [i[0] for i in mycursor.description]
df = pd.DataFrame(myresult, columns=column_names)

print(df)

df.dtypes


# In[146]:


#Melihat data kosong

df['actor_id'].isnull()


# In[142]:


#cek total data

df.shape


# In[166]:


#Mencetak last name yang mempunyai karakter "BE"

import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sakila"
)

mycursor = mydb.cursor()

sql_query = "SELECT first_name, last_name FROM actor WHERE last_name LIKE '%BE%'"
mycursor.execute(sql_query)

result = mycursor.fetchall()
column_names = [i[0] for i in mycursor.description]
df = pd.DataFrame(result, columns=column_names)

print(df)

mycursor.close()
mydb.close()


# In[179]:


#Mencetak city dan address jika city_id<60

import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="sakila"
)
mycursor = mydb.cursor()
mycursor.execute("select city.city_id,city,address from city inner join address on city.city_id = address.city_id order by city.city_id asc")
myresult = mycursor.fetchall()

columns = []
for asc in mycursor.description:
    columns.append(asc[0])


df = pd.DataFrame(myresult, columns=columns)
print(df)
mycursor.close()

n=1
while n<60:
    selected=df.loc[df['city_id'] == n, ['city', 'address']]
    print(selected)
    n=n+1

