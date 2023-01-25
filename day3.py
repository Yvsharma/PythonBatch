#!/usr/bin/env python
# coding: utf-8

# # Q1)Write a program to prompt the user for days and rate per day to compute total pay. Use 50 days and a rate of 3.5 per day to test the program. Total pay is equal to (days* Rate per day). You should use input to read a string and float() to convert the string to a number.

# # Q2) write a program to find the square root of a no. given by user

# In[1]:


#solution1

days=50
rate_perday=3.5
print(float(days*rate_perday))


# In[2]:


#solution2

a=int(input('enter a no. : '))
b=a**0.5
print(b)


# In[3]:


#boolean

x= 5
y= 10
x>y


# In[4]:


#if else


# In[5]:


x= 5
y= 10
if x<y:
    print('x is greater')


# In[8]:


x= int(input('enter a no. :'))
y= int(input('enter a no. :'))
if x<y:
    print('y is greater')
else:
    print( 'x is greater')


# In[9]:


x= int(input('enter a no. :'))
y= int(input('enter a no. :'))
if x<y:
    print('Y is greater')
elif x==y:
     print('x is equal to y')
else:
    print('X is greater')


# # Data structures

# # 1) list 2)Tuple 3)Dictionary 4) Set

# # Tuple

# In[10]:


tup1=(1,2,'python')


# In[11]:


type (tup1)


# In[12]:


tup1[1]


# In[16]:


tup2=(1,'2a',True,'5b',False,'CETPA')


# In[17]:


tup2[0]


# In[18]:


tup2[1]


# In[19]:


tup2[-1]


# In[20]:


tup2[1:5]


# In[21]:


#type changing 
tup2[1]='222'


# In[22]:


#basic operations


#length
len(tup2)


# In[23]:


#concatenation tuple

tup1=(1,2,3)
tup2=(4,5,6)
tup1+tup2


# In[24]:


tup2+tup1


# In[25]:


#repeating tuple element
tup1*2


# In[26]:


#repeating & concatenating
tup1=(1,2,3)
tup2=(1,'cetpa',3)


# In[27]:


tup2*2+tup1*3


# In[28]:


#min and max

tup3=(2,22,24,68,35,45,35,225)
min(tup3)


# In[29]:


max(tup3)


# # List

# In[30]:


L1=[1,'a',True]


# In[31]:


type(L1)


# In[32]:


L1=[1,'a',2,'b',3,'c']


# In[33]:


#extracting
L1[1]


# In[34]:


L1[2:5]


# In[35]:


#modify
L1[2]=100


# In[36]:


L1


# In[37]:


L1[1]=50


# In[38]:


L1


# In[39]:


#popping (it removes last value) ( .pop)

L1.pop()


# In[40]:


L1


# In[41]:


#appending ( .append)

L1.append('c')
L1


# In[42]:


#reversing ( .reverse())

L1


# In[43]:


L1.reverse()
L1


# In[44]:


L1


# In[45]:


L1.reverse()


# In[46]:


L1


# In[47]:


#sorting ( sequence)
L3= ['red','black','white','pink']


# In[48]:


L3.sort()


# In[49]:


L3


# In[50]:


L1.sort()


# In[51]:


#inserting element at a specific index

L3.insert(1,'blue')


# In[52]:


L3


# In[53]:


# basic operations

#repeating

L3*3


# In[54]:


#concat
L1


# In[55]:


L3


# In[56]:


L1+L3


# In[ ]:




