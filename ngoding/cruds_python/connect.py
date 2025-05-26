import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="admin"
)

if db.is_connected():
  print("Berhasil terhubung ke database")