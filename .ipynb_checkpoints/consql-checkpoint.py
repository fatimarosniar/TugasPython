import mysql.connector
import pandas as pd

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: {err}")
    return connection

host = "localhost"
user = "root"
pw = "Tripang18"

# koneksi ke server
connection = create_server_connection(host, user, pw)

# Membuat database mysql_python
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database berhasil dibuat")
    except Error as err:
        print(f"Error: {err}")      

create_database_query = "CREATE DATABASE db_perpustakaan"
create_database(connection, create_database_query)

# koneksi ke database'
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name)
        print("MySQL database connection successfull")
    except Error as err:
        print(f"Error: {err}")
    return connection

host = "localhost"
user = "root"
pw = "Tripang18"
db = "db_perpustakaan"

connection = create_db_connection(host, user, pw, db)

# Membuat Table user
create_table_user ="""USE db_perpustakaan;
                    CREATE TABLE tbl_user(
                    id_user INT AUTO_INCREMENT PRIMARY KEY,
                    u_name VARCHAR(20),
                    tgl_lahir VARCHAR(10),
                    pekerjaan VARCHAR(20),
                    alamat VARCHAR(50)
                    );"""
create_database(connection, create_table_user)

host = "localhost"
user = "root"
pw = "Tripang18"
db = "db_perpustakaan"
connection = create_db_connection(host, user, pw, db)

#Membuat Table buku
create_table_buku ="""USE db_perpustakaan;
                    CREATE TABLE tbl_buku(
                    id_buku INT AUTO_INCREMENT PRIMARY KEY,
                    nama_buku VARCHAR(50),
                    kategori VARCHAR(20),
                    stock INT(10)
                    );"""
create_database(connection, create_table_buku)


