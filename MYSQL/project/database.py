import mysql.connector as sql

krishna=sql.connect(host="localhost",user="root",password="root",port=3306, database="wd5")
car=krishna.cursor()
print("database connected")