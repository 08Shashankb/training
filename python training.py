#!/usr/bin/env python
# coding: utf-8

# In[3]:


name=input("enter your name : ")
while len(name)==0 or name.isalpha()==False:
    name=input("Enter Valid Name : ")
    
telephone=input("Enter Telephone Number : ")
while len(telephone)!=10 or telephone.isnumeric()==False:
    telephone=input("Enter Valid Telephone Number : ")

age=input("Enter Your Age : ")
while  age.isnumeric()==False or int(age)<20 or int(age)>99:
    age=(input("Enter Correct Age : "))
         
salary=input("Enter your salary : ")
while salary.isnumeric()==False or int(salary)<0 or salary=="" :
    salary=input("Enter Valid salary: ")
    
city=input("Enter your city: ")
while city.isalpha()==False or len(city)==0 :
    city=input("Enter valid City name: ")
    
department=input("Enter Your Department: ")
while department.isalpha()==False or len(department)==0 :
    department=input("Enter Valid Department: ")
    

print(" ")    
print("Employee Details")
print("Name: "+name)
print("telephone: " + telephone)
print("Age: "+ age)
print("Salary: Rs"+salary)
print("City: "+city)
print("Department: "+department)
            


# In[ ]:


import datetime as dt
first_name=input("Enter your First Name: ")
last_name=input("Enter your Last Name: ")
today=dt.date.today()
DOB=input("Enter your DOB: ")
age=today.year-int(DOB[0:4])
Telephone=input("Enter your Telephone Number: ")
Email= input("Enter your Email: ")
Address=input("Enter your Address:")
Company=input("Enter your Company Name: ")
Company_Add=input("Enter your Company Address: ")
Service_years_Available=60-age
print("Name : ", first_name + " " + last_name)
print("age : " , age)
print("Telephone: ",Telephone)
print("Email: ",Email)
print("Address: ",Address)
print("Company: ",Company)
print("Company Address: ", Company_Add)
print("Service Available: ",Service_years_available)


# In[ ]:


a="shashank"
for i in range(0,len(a)):
    print(a[i])


# In[ ]:


a=[1,2,3,8,4,7]
b=sorted(a)
print(b)
print(a)


# In[ ]:


a={'Py':'python','dict':'Dictionary','Key3':'Value3','Key4':'Value4','Key5':'Value5','Key6':'Value6','Key7':'Value7','Key8':'Value8'}

i=input()
while i in a:
    print(a[i])
    break;


# In[ ]:


a=int(input("Enter Salary : "))
b=int(input("Enter Service in Years : "))
if b<3:
    print("not Eligible")
if b>=3 and b<5:
    a=a*1.05
    print(a)
elif b>=5 and b<10:
    a=a*1.1
    print(a)
elif b>=10:
    a=a*1.15
    print(a)


# In[ ]:


a=25
b=int(input("Enter total classes attended : " ))
if b//a>=0.75:
    print("Eligible for Exams")
else:
    print("Not Eligible")


# In[ ]:


a=list(input())
a.sort()
b=a[:-1]
print(b[-1])


# 
