#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. What exactly is []?
#[]denotes the empty list value which contains no item.


# In[2]:


#2. In a list of values stored in a variable called spam, how would you assign the value 'hello'; as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)

spam = [2, 4, 6, 8, 10]
spam.insert(2,'hello')


# In[3]:


spam


# In[4]:


#Let's pretend the spam includes the list ['a','b','c','d'] for the next three queries.


# In[6]:


#3. What is the value of spam[int(int('3' * 2) / 11)]?
spam[int(int('3' * 2) / 11)]

#Ans = 6


# In[8]:


#4What is the value of spam[-1]?
spam[-1]

#Ans = 10


# In[10]:


#5. What is the value of spam[:2]?
spam[:2]

#Ans = [2, 4]


# In[11]:


bacon = [3.14, 'cat', 11, 'cat',True]


# In[13]:


#6. What is the value of bacon.index('cat')?

bacon.index('cat')

#Ans = 1


# In[14]:


#7. How does bacon.append(99) change the look of the list value in bacon?

bacon.append(99)

#Ans = By adding 99 to the list [3.14, 'cat', 11, 'cat', True, 99]


# In[16]:


#8. How does bacon.remove('cat') change the look of the list in bacon?

bacon.remove('cat')

#Ans = By removing cat from the list [3.14, 11, 'cat', True, 99]


# In[18]:


#9. What are the list concatenation and list replication operators?

#List concatenation operator is '+' and list replication operator is '*'. 


# In[19]:


#10. What is difference between the list methods append() and insert()?

#The element passed as an append() is appended to the end of the list, The element passed as the insert() can be inserted at any desired index.


# In[20]:


#11. What are the two methods for removing items from a list?

#the two methods for removing items from a list are pop() and remove.


# In[21]:


#12. Describe how list values and string values are identical.

#Lists are similar to strings, which are ordered collections of characters,  both are sequences.


# In[22]:


#13. What's the difference between tuples and lists?

# Tuples are immutable whereas, list is mutable
#The list is better for performing operations, such as insertion and deletion, while Tuple data type is appropriate for accessing the elements
#Lists consume more memory while, tuple consume less memory than list.
#The unexpected changes and errors are more likely to occur in list, while in tuple it is hard to take place.


# In[3]:


#14. How do you type a tuple value that only contains the integer 42?
tuple=(42,)


# In[7]:


type(tuple)


# In[1]:


#15. How do you get a list value's tuple form? How do you get a tuple value's list form?

#list value's tuple form:
l = ['list']
a = tuple(l)
print(a)

#Ans=('list',)


# In[2]:


#Tuple's value List form:
t = ('tuple',)
a = list(t)
print(a)

#Ans=['tuple']


# In[3]:


#16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?

#Variables will contain references to list values rather than list values themselves.


# In[ ]:


#17. How do you distinguish between copy.copy() and copy.deepcopy()?

#copy() create reference to original object. If you change copied object - you change the original object.
#copy.deepcopy() creates new object and does real copying of original object to new one.

