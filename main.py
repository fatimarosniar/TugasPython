import mysql.connector

print("LIBRARY MANAGEMENT \
      \n1. Pendaftaran User Baru \
      \n2. Pendaftaran Buku Baru \
      \n3. Tampilkan Daftar User \
      \n4. Tampilkan Daftar Buku \
      \n5. Exit")

nomor_tugas = input("Masukan Nomor Tugas :")

def menu(nomor_tugas):
    if int(nomor_tugas) == 1:
        import user
    if int(nomor_tugas) == 2:
        import buku
    if int(nomor_tugas) == 3:
        import view_user
    if int(nomor_tugas) == 4:
        import view_buku
    else:
        return "others"
        
print(menu(nomor_tugas))
