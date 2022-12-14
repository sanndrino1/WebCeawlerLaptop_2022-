
#use test;
import mysql.connector
import mysql.connector as mc

mydb = mysql.connector.connect(
  host="localhost",
  user="test",
  password="test"
)

print(mydb)


mydb = mysql.connector.connect(
  host="localhost",
  user="test",
  password="test"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)