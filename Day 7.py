#!/usr/bin/env python
# coding: utf-8

# # Q1) wap ask user his/her name and print a msg with name and wap in a way that it will never end asking name

# In[2]:


while True:
    name=input('Enter name : ')
    print('Hello ',name )


# In[ ]:


a=3
while a==3:
    name=input('Enter name : ')
    print('Hello ',name )
    


# Q2) Maths,Science, English ask user for marks 
# find the avg
# if avg >80 print grade A
# 80>avg>60 print grade B
# 60>avg>40 print grade C
# avg<40 print try again
# 
# * if user enter no. >100 program will show please enter the corret 
# no. with subj.

# In[2]:


math=int(input('enter no. of maths : '))
science=int(input('enter no. of science : '))
english=int(input('enter no. of english : '))
avg=(math+science+english)/3
if math>100:
    print('enter correct no.of math')
elif science>100:
    print('enter correct no.of science')
elif english>100:
    print('enter correct no. of english')
elif avg>80:
    print('grade a')
elif avg<80 and avg>60:
    print('grade b')
elif avg>40 and avg<60:
    print ('grade c')
else:
    print('practice more')


# In[ ]:


math=int(input('enter no. of maths : '))
science=int(input('enter no. of science : '))
english=int(input('enter no. of english : '))
avg=(math+science+english)/3
if math>100 or science>100 or english>100:
    print('enter correct no.')
elif avg>80:
    print('grade a')
elif avg<80 and avg>60:
    print('grade b')
elif avg>40 and avg<60:
    print ('grade c')
else:
    print('practice more')


# In[1]:


math=int(input('enter no. of maths : '))
science=int(input('enter no. of science : '))
english=int(input('enter no. of english : '))
avg=(math+science+english)/3
if math>100:
    print('enter correct no.of math')
elif science>100:
    print('enter correct no.of science')
elif english>100:
    print('enter correct no. of english')
elif avg>80:
    print('grade a')
elif avg<80 and avg>60:
    print('grade b')
elif avg>40 and avg<60:
    print ('grade c')
else:
    print('practice more')


# In[3]:


math=int(input('enter no. of maths : '))
science=int(input('enter no. of science : '))
english=int(input('enter no. of english : '))
avg=(math+science+english)/3
if math>100:
    print('enter correct no.of math')
    if science>100:
        print('enter correct no.of science')
elif science>100:
    print('enter correct no.of science')
elif english>100:
    print('enter correct no. of english')
elif avg>80:
    print('grade a')
elif avg<80 and avg>60:
    print('grade b')
elif avg>40 and avg<60:
    print ('grade c')
else:
    print('practice more')


# # Some common topics

# In[4]:


import random

print(random.randrange(1, 10))


# In[5]:


#check string 

txt = "The best things in life are free!"
print("free" in txt)


# In[6]:


txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


# In[7]:


txt = "The best things in life are!"
if "free" in txt:
  print("Yes, 'free' is present.")


# In[8]:


txt = "The best things in life are free!"
print("expensive" not in txt)


# In[9]:


txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


# In[10]:


# -ve indexing
b = "Hello, World!"
print(b[-5:-2])


# In[11]:


b = "Hello, World!"
print(b[-2:-5])


# # Modifying string

# In[13]:


# Upper case
a = "Hello, World!"
print(a.upper())


# In[14]:


# Lower case
a = "Hello, World!"
print(a.lower())


# In[15]:


# Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


# In[16]:


# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))


# In[17]:


# Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


# # String Format

# In[18]:


age = 36
txt = "My name is John, I am " + age
print(txt)


# In[19]:


# The format() method takes the passed arguments, 
# formats them, and places them in the string where the placeholders {} are:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


# In[20]:


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


# In[ ]:




