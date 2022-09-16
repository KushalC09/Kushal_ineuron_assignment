#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. What does an empty dictionary's code look like?

#dict = {} denotes empty dictionary.


# In[1]:


#2. What is the value of a dictionary value with the key 'foo' and the value 42?

dict = {'foo' : 42}


# In[5]:


dict.values()

#ans = dict_values([42])


# In[6]:


#3. What is the most significant distinction between a dictionary and a list?

#List - items in list are Ordered
#Dictionary : items in dictionary are unordered


# In[7]:


#4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

spam = {'bar': 100}


# In[9]:


spam['foo']

#It will give you keyerror.


# In[15]:


#5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

spam = {'cat' : '' }

spam
#spam will give output {'cat': ''}.


# In[14]:


spam.keys()

#spam.keys() will give output dict_keys(['cat']).


# In[16]:


#6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?

spam = {'cat' : '' }

spam
#spam will give output {'cat': ''}.

spam.keys()

#spam.keys() will give output dict_keys(['cat']).


# In[19]:


#7. What is a shortcut for the following code?

if 'colour' not in spam:
    spam['colour'] = 'black'


# In[20]:


spam['colour']
#Ans = 'black'


# In[ ]:


#8. How do you "pretty print" dictionary values using which module and function?

#Using pprint() function we can "pretty print" dictionary values.

