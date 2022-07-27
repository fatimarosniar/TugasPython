import mysql.connector


u_name = input("Masukan nama user :")
tgl_lahir = input("Masukan tanggal lahir (YYYY-MM-DD):")
pekerjaan = input("Pekerjaan :")
alamat = input("Masukan Alamat :")

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Tripang18",
  database="db_perpustakaan"
)

cursor = db.cursor()
sql = "INSERT INTO tbl_user (u_name, tgl_lahir, pekerjaan, alamat) VALUES (%s, %s, %s, %s)"
val = (u_name, tgl_lahir, pekerjaan, alamat)

cursor.execute(sql, val)
db.commit()

print("Data berhasil ditambahkan")
    

