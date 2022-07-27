import mysql.connector
import pandas as pd

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Tripang18",
  database="db_perpustakaan"
)

cursor = db.cursor()
sql = "SELECT * FROM tbl_buku"
cursor.execute(sql)

results = cursor.fetchall()
df = pd.DataFrame(results)
df.columns =['id_buku', 'nama_buku', "kategori", 'stock']
print(df)