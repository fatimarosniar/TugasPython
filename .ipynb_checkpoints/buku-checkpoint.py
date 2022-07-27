import mysql.connector
import pandas as pd

nama_buku = input("Masukan nama buku :")
kategori = input("Masukan kategori buku:")
stock = int(input("Masukan stock buku :"))


db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Tripang18",
  database="db_perpustakaan"
)

cursor = db.cursor()
sql = "INSERT INTO tbl_buku (nama_buku, kategori, stock) VALUES (%s, %s, %s)"
val = (nama_buku, kategori, stock)

cursor.execute(sql, val)
db.commit()

print("Data berhasil ditambahkan")