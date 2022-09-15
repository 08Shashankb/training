import cal
f_name=input("Enter Your First Name: ")
l_name=input("Enter Your Last Name: ")

s=cal.salary()
a=cal.hra(s)
b=cal.dh(s)
c=cal.bonus(s)
total=s+a+b+c
print("Total Salary is: ",total)






    
