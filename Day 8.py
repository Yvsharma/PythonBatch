#!/usr/bin/env python
# coding: utf-8

# # Q1) Python Program to Check Leap Year

# In[ ]:





# # for loop

# In[1]:


lis=['apple','orange','banana']


# In[2]:


for i in lis:
    print(i)


# # nested

# In[3]:


lis2=['book','chair','phone']


# In[6]:


for i in lis:
    for j in lis2:
        print(i,j)


# # Q2) Python Program to make star pattern 

# Number pattern
# 
# Triangle pattern
# 
# Star (*) or asterisk pattern
# 
# Pyramid pattern
# 
# Inverted pyramid pattern
# 
# Half pyramid pattern
# 
# Diamond Shaped pattern
# 
# Characters or alphabets pattern
# 
# Square pattern

# In[12]:


for i in range(5):
    print(i*'*')


# # Q3) Python program to calculate the sum of all the odd numbers within the given range of 10.

# In[13]:


given_range = 10
sum = 0
 
for i in range(given_range):
        if i%2!=0:
                sum+=i
print(sum)


# In[14]:


given_range = input()
sum = 0
 
for i in range(given_range):
        if i%2!=0:
                sum+=i
print(sum)


# In[15]:


given_range = int(input())
sum = 0
 
for i in range(given_range):
        if i%2!=0:
                sum+=i
print(sum)


# # function

# In[16]:


a='good'
def my_fun():
    print('you are '+ a)


# In[17]:


my_fun()


# In[18]:


a='good'
def my_fun():
    a="poor"
    print('you are '+ a)


# In[19]:


my_fun()


# In[28]:


#global keyword
a='good'
def my_fun():
    global a
    a='good'
    print('you are '+ a)


# In[29]:


my_fun()


# In[ ]:




