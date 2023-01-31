#!/usr/bin/env python
# coding: utf-8

# ### Q1) A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# ### Ask user for their salary and year of service and print the net bonus amount.

# In[2]:


serviceyear = int(input("Enter the year of service: "))
salary = int(input("Enter the Salary: "))
if serviceyear > 5:
    bonus = (salary *5)/100
    Netamount = bonus + salary
    print(Netamount)

else :

    print("Not Qualified")
    
print('congrasts')


# ### Q2)Take values of length and breadth of a rectangle from user and check if it is square or not.

# In[4]:


length = float(input("Enter the length: " ))
breadth = float(input("Enter the breadth: "))
if(length == breadth):
    print("This is a Square ")
else:
    print("This is not a Square")


# ### Q3) Take two int values from user and print greatest among them.

# In[5]:


num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
if num1>num2:
    print(num1,"is greater")
elif num1==num2 :
    print("They are equal")
else:
    print(num2," is greater")


# ### Q4) A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100.Judge and print total cost for user.

# In[7]:


quantity=int(input())
cost=100*quantity
if cost>1000:
    discount=0.1*cost
    finalcost=cost-discount
    print(finalcost)
elif cost<1000:
    print(cost)


# ### Q5) A school has following rules for grading system:
# ### a. Below 25 - F 
# ### b. 25 to 45 - E 
# ### c. 45 to 50 - D
# ### d. 50 to 60 - C
# ### e. 60 to 80 - B
# ### f. Above 80 - A
# ### Ask user to enter marks and print the corresponding grade.

# In[11]:


marks=int(input('Enter marks '))
if marks>=0 and marks<25:
    print('Grade F')
elif marks>=25 and marks<45:
    print('Grade E')
elif marks>=45 and marks<50:
    print('Grade is D',marks)
elif marks>=50 and marks<60:
    print('Grade is C')
elif marks>=60 and marks<80:
    print('Grade is B')
elif marks>=80 and marks<=100:
    print('Grade is A')
elif marks>100 or marks<0:
    print('please enter valid marks')


# In[ ]:




