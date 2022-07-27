# TugasPython
Username : fatima-jmmp

**Objective :**
Membuat LMS untuk perpustakaan pacmann

**Detail :**

**main.py \**
  Menu utama perpustakaan yang berisi menu :
  1. Pendaftaran User Baru (user.py)
  2. Pendaftaran Buku Baru (buku.py)
  3. Tampilan tabel User (tbl_user.py)
  4. Tampilan table Buku (tbl_buku.py)

**consql.py \**
Module untuk menghubungkan dengan MySQL, membuat database dan table 

**Cara Running :**

1. Jalan kan consql.py di terminal untuk menghubungkan, membuat database dan membuat table di My SQL
command : python consql.py
2. Jalan kan main.py di terminal untuk masuk ke menu utama perpustakaan
command : pyhon main.py
3. masukan nomor tugas sesuai yang diinginkan

**Saran dan Perbaikan:**

Masih perlu disempurnakan lagi dan perlu waktu tambahan untuk menambahkan menu:
1. Peminjaman
2. Tampilkan Daftar Peminjaman -- data 3 + (tanggal_pinjam) auto; tanggal_pengembalian (tanggal_pinjam + 3hari)
3. Cari Buku -- id_buku/nama_buku/kategori/stock(stok awal - stok pinjam)
4. Pengambilan


