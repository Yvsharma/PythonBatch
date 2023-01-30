#!/usr/bin/env python
# coding: utf-8

# # write a program to find a number is -ve, +ve or zero?

# In[6]:


num=float(input('enter a number = '))
if num>0:
    print('+ve number', num)
elif num<0:
    print('-ve number', num)
else:
    print('zero')


# # write a program to find a number is odd or even? `

# In[1]:


num1=int(input('enter a number = '))
if num1%2==0:
    print('even number', num1)
elif num1%2!=0:
    print('odd number', num1)
else :
    print('zero')


# In[2]:


#list []

l1=[1,'a','python']
l1[1]


# In[3]:


l1[1:]


# In[4]:


#modifying

l1[1]=100


# In[5]:


l1


# In[6]:


#pop
l1.pop()


# In[51]:


l1.pop(0)
l1


# In[7]:


l1


# In[10]:


#append
l1.append('class')


# In[11]:


l1


# In[12]:


l1.append('classes','floor')


# In[13]:


l1


# In[14]:


#revese
l1


# In[15]:


l1.reverse()


# In[16]:


l1


# In[17]:


#sorting
l2=['a','x','f','dd','yy','aa']


# In[18]:


l2.sort()


# In[19]:


l2


# In[20]:


#inserting at specific index
l2.insert(2,'red')


# In[21]:


l2


# In[22]:


#basic operations

#repeating element
l1


# In[23]:


l1*2


# In[24]:


#concatenating list
l1


# In[25]:


l2


# In[26]:


l1+l2


# In[27]:


l2+l1


# # Dictionary

# In[28]:


#it is an ordered collection of Key and value (pair) 
#enclosed by {}

#is is mutable


# In[29]:


fruit={'Apple':80,'banana':60,'orange':40}


# In[30]:


fruit


# In[31]:


type(fruit)


# In[34]:


#dict_keys

fruit.keys()


# In[35]:


#dict_values
fruit.values()


# In[36]:


#dict_items

fruit.items()


# In[37]:


#modifications

#adding pair
fruit['Mango']=50


# In[38]:


fruit


# In[39]:


#changing an existing element

fruit['Apple']=100


# In[40]:


fruit


# In[41]:


# dictionary functions

fruit1={'Apple': 100, 'banana': 60}
fruit2={'orange': 40, 'Mango': 50}


# In[42]:


fruit1+fruit2


# In[43]:


#update

fruit1.update(fruit2)


# In[44]:


fruit1


# In[45]:


fruit2


# In[46]:


fruit1


# In[47]:


#pop

fruit1.pop('orange')


# In[48]:


fruit1


# In[49]:


fruit1.pop()


# # Set

# In[53]:


# it is an unordered and unindexed collection of element
# with{}

#duplicates are not allowed

S1={1,2,5,'aa',2}


# In[55]:


S1


# In[56]:


S1[1]


# In[57]:


type(S1)


# In[58]:


#set operations

#adding

S1.add('hello')


# In[59]:


S1


# In[60]:


S1.add('2b')


# In[61]:


S1


# In[62]:


#removing

S1.remove(5)


# In[63]:


S1


# In[64]:


#update
S1.update([10,20,80])


# In[65]:


S1


# In[67]:


S1.update('20','d')


# In[68]:


S1


# In[69]:


S1.update('2b','22')


# In[70]:


S1


# In[71]:


S1.update(22,10)


# In[72]:


S1.update([22,10])


# In[73]:


S1


# In[77]:


#set functions

#union of two sets

s2={1,2,3}
s3={'a','b','c'}


# In[78]:


s3.union(s2)


# In[79]:


s4={1,2,3,4}
s5={'a','b','c','d'}


# In[80]:


s5.union(s4)


# In[81]:


s6={1,2,4}
s7={'a','d'}
s6.union(s7)


# In[83]:


#intersection

set1={1,2,3,4,5,6}
set2={5,6,7,8,9,2}


# In[85]:


set1.intersection(set2)


# In[ ]:




