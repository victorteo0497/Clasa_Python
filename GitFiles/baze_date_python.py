#!/usr/bin/python3

import MySQLdb

### Part 0 ### Connecting to DB

db = MySQLdb.connect('localhost', 'root', '1804', 'Python')

if db == None:
	print("Error connecting to database")
else:
	print("All good")

cursor = db.cursor()
cursor.execute("SELECT VERSION();")
data = cursor.fetchall()

print(data)


## Part 1 ### Creating a table and checking it

try:
	cursor.execute("DROP TABLE IF EXISTS HOP")
	cursor.execute("""CREATE TABLE HOP (
			         	NAME CHAR(20) NOT NULL,
			         	AGE INT,
			         	GENDER CHAR(1),
			         	INTEREST CHAR(20));	
			   	""")
	print("TABLE CREATED")
except Exception:
	print("Operation failed")
	db.rollback()

### Part 2 ### Addding data in the table 

sql = """INSERT INTO HOP (NAME, AGE, GENDER, INTEREST) VALUES ("Victor", "23", "M", "Python")"""

try:
	cursor.execute(sql)
	db.commit()
except Exception:
	print("Can't add to database #2")
	db.rollback()

### Part 3 ### Adding data to the table via scripting

sql_query = (("Ramon", 24, "M", "Programare"),("Adi", 23, "M", "Retele"),("Gloria", 34, "F", "Apple"))

for user in sql_query:
	try:
		cursor.execute('INSERT INTO HOP (NAME, AGE, GENDER, INTEREST) VALUES ("%s", "%d", "%s", "%s")' % (user[0], user[1], user[2], user[3]))
		db.commit()
	except Exception:
		print("Operation for not working...")	
		cursor.rollback()

cursor.execute("SELECT * FROM HOP;")
data_table = cursor.fetchall()
print(data_table)

db.close()












