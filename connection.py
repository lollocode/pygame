import mysql.connector, ast

f = open("./db/db-config.json", "r")

mydb = mysql.connector.connect(**ast.literal_eval(f.read()))
mycursor = mydb.cursor()