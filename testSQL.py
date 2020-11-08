import mysql.connector

# connect to server?
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Bobbobb0bbob!",
    database="testdb"
)


# Initialise cursor
mycursor = mydb.cursor()

# Create Database
'''
#mycursor.execute("CREATE Database testingdb")
mycursor.execute("SHOW DATABASES")

for db in mycursor:
    print(db)
'''

# Create Table
'''
#mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")
mycursor.execute("SHOW TABLES")

for tb in mycursor:
    print(tb)
'''


# Add to Database
'''
sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
student1 = [("Richmond", 24),
            ("Gary", 25),
            ("Keith", 26),
            ("Dave", 27),
            ("Bob", 28),
            ("Jim", 29)]

mycursor.executemany(sqlFormula, student1)  # for many
# mycursor.execute(sqlFormula, student1) #for one
mydb.commit()
'''

# Show the whole database / column of a database
'''
#mycursor.execute("SELECT * FROM students")
mycursor.execute("SELECT age FROM students")
# fetches everything that was found in the previous statement
myresult = mycursor.fetchall()
mycursor.execute("SELECT age FROM students")
myresult = mycursor.fetchone()  # returns the first entry

for row in myresult:
    print(row)
'''


# Return everything where age = 25
'''
mycursor.execute("SELECT * FROM students WHERE age =25")
myresult = mycursor.fetchall()
for result in myresult:
    print(result)
'''

# LIKE - return things that include "a"
'''
sql = "SELECT * FROM students WHERE name LIKE '%a%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for result in myresult:
    print(result)
'''

# SQL injection - USe palceholders so dont get hacked
'''
sql = "SELECT * FROM students WHERE name LIKE %s"
mycursor.execute(sql, ("Gary",))
myresult = mycursor.fetchall()
for result in myresult:
    print(result)
'''

# Update values
'''
sql = "UPDATE students SET age = 13 WHERE name = 'Gary'"
mycursor.execute(sql)
mydb.commit()
'''

# Limit results
'''
sql = "SELECT * FROM students LIMIT 5 OFFSET 2"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for result in myresult:
    print(result)
'''

# Order results
'''
sql = "SELECT * FROM students ORDER BY age"
#sql = "SELECT * FROM students ORDER BY age DESC" #Descending
mycursor.execute(sql)
myresult = mycursor.fetchall()
for result in myresult:
    print(result)
'''

# Delete row
'''
sql = "DELETE FROM students WHERE name = "Gary"
mycursor.execute(sql)
mydb.commmit
'''

# Delete table
'''
sql = "DROP TABLE IF EXISTS students"
mycursor.execute(sql)
mydb.commmit
'''
