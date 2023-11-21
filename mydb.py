import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'Nastavnikdezen14$'

	)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE barbarossa")

print("All done")
