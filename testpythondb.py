

import mariadb
import sys
conn = mariadb.connect(
    user="root",
    password="incorrect@el1",
    host="localhost",
    port=3306,
    database="employee"
)



cur = conn.cursor()
conn.autocommit=True

try:

    cur.execute('CREATE TABLE employee (first_name VARCHAR(30),last_name VARCHAR(50),phone int,age varchar(30),email varchar(50),salary int,department varchar(20),ID varchar(20),Manager varchar(30),city varchar(30))')

except Exception as y:

    print(y)    


fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
phone = input("Enter your phone no: ")
age = input("Enter your Age: ")
email = input("Enter your emailID: ")
sal = input("Enter your salary: ")
depart = input("Enter your department name: ")
ID = input("Enter your ID: ")
manager = input("Enter your Manager: ")
city = input("Enter your city: ")


cur.execute('INSERT INTO employee (first_name, last_name,phone,age,email,salary,department,ID,Manager,city) VALUES (%s,%s,%d,%d,%s,%d,%s,%d,%s,%s)',(fname,lname,phone,age,email, sal,depart,ID, manager, city))

cur.execute('SELECT * from employee;')
"""
myresult=cur.fetchall()
print(myresult)
"""
for (first_name, last_name,phone,age,email,salary,department,ID,Manager,city) in cur:
    print(first_name,last_name,phone,age,email,salary,department,ID,Manager,city)
cur.close()

