#!/usr/bin/env python
# coding: utf-8

# # if statement

# In[5]:


if 5>2:
    print('5 is greatest')


# # if else statement

# In[6]:


if 5<2:
    print('5 is greatest')
else:
    print('not possible')


# # elif statement

# In[8]:


x=5
y=5
if x>y:
    print('5 is greatest')
elif x==y:
    print('equal values')
else:
    print('not possible')


# # nested if
# 
# ''' Syntax:
# if (condition_1):
#     print('string')
#     if (condition_2):
#         print('text')
# 
# 
# '''

# In[11]:


if (5>6):
    print('string')
    if (6>2):
        print('text')
print('rest data')


# In[12]:


if (5<6):
    print('string')
    if (6>2):
        print('text')
print('rest data')


# In[15]:


if (5<6):
    print('string')
    if (6<2):
        print('text')
print('rest data')


# In[16]:


x=6
X=51

print(x)


# In[17]:


print(X)


# In[18]:


X=5


# In[20]:


X


# In[21]:


X=10


# In[22]:


X


# # nested if else

# In[ ]:


# syntax

if (condition_1):
    print('text1')
    if (condition_2):
        print('text2')
    else:
        print('text3')
else:
    ('rest data')


# In[23]:


if (5>2):
    print('text1')
    if (5>10):
        print('text2')
    else:
        print('text3')
else:
    print('rest data')


# In[24]:


if (5>2):
    print('text1')
    if (5>10):
        print('text2')
    else:
        print('text3')
else:
    print('rest data')
print('next data')


# In[25]:


if (5<2):
    print('text1')
    if (5>10):
        print('text2')
    else:
        print('text3')
else:
    print('rest data')
print('next data')


# In[ ]:


if (condition_1):
    print('text1')
    if (condition_2):
        print('text2')
    else:
        print('text3')
else:
    if (condition_2):
        print('text2')
    else:
        print('text3')
print('rest data')


# In[26]:


a=2
b=4
c=1
d=6


# In[27]:


if(a>b):
    print("a is greater")
    if(b>c):
        print("b is greater")
    else:
        print("c is greater")
else :
    if(c>d):
        print("c is greater than d")
    else:
        print("d is greater than c")


# # while looping

# In[28]:


# this are used to repeat a task multiple time.


# In[29]:


#first 10 no.

i=1
while i<=10:
    print(i)
    i=i+1


# In[30]:


i=5
while i<=500:
    print(i)
    i=i+5


# In[31]:


# Print table of 2

i=1
n=2
while i<=10:
    print(n,"*",i,"=",n*i)
    i=i+1


# # updating values of list using while loop

# In[33]:


l1=[1,2,3,4,5,6]


# In[34]:


i=0
while i<len(l1):
    l1[i]=l1[i]+100
    i=i+1


# In[35]:


l1


# In[36]:


i=1
while i<len(l1):
    l1[i]=l1[i]+100
    i=i+1


# In[37]:


l1


# In[42]:


l = ['a','b','c','d']
i = 0
while i<len(l):
    l[i]= l[i]*2
    i = i+1
print(l)


# In[41]:


print(l)


# In[44]:


l2 = ['a','b','c','d']
i = 0
while i<len(l2):
    l2[i]= l2[i]+2
    i = i+1
print(l2)


# In[45]:


l2 = ['a','b','c','d']
i = 0
while i<len(l2):
    l2[i]= l2[i]+'2'
    i = i+1
print(l2)


# In[ ]:




