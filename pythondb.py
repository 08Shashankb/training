import mariadb
import sys
conn = mariadb.connect(
    user="root",
    password="incorrect",
    host="localhost",
    port=3306,
    database="employee"
)
"""
another method for inserting values
Name=input("enter your name : ")
Telephone = input("Enter Your Telephone Number : ")
Age = input("Enter Your Age : ")
Salary = input("Enter Your Salary : ")
city = input("Enter your City : ")
department = input("Enter Your Department : ")
"""

cur = conn.cursor()
conn.autocommit=True

try:
    cur.execute("create table Employees (Name varchar(40),telephone int,Age int,Salary int,City varchar(40),Department varchar(30))");
except Exception as y:
    print(y)

#Inserting values into DB-employee
cur.execute("INSERT INTO Employees (Name,telephone,Age,Salary,City,Department) VALUES ('Shashank',1234567890,22,70000,'Bangalore','DH'),('rishi',0987654321,22,50000,'Mysore','DH'),('Arjun',1234567809,22,30000,'mlore','DH')");

#executing select statment
cur.execute("select name,age,telephone from employees")
for (name,age,telephone) in cur:
    print("Name", {name},"Age",{age},"Telephone",{telephone})

