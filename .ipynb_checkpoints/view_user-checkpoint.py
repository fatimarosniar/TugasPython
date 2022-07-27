import mysql.connector
import pandas as pd

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Tripang18",
  database="db_perpustakaan"
)

cursor = db.cursor()
sql = "SELECT * FROM tbl_user"
cursor.execute(sql)

results = cursor.fetchall()
df = pd.DataFrame(results)
df.columns =['id_user', 'u_name', "tgl_lahir", 'pekerjaan', 'alamat']
print(df)

    