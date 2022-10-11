#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Is the Python Standard Library included with PyInputPlus?

#PyInputPlus is not a part of the Python Standard Library, we must install it separately using Pip.


# In[2]:


#2. Why is PyInputPlus commonly imported with import pyinputplus as pypi?

# You can import the module with import pyinputplus as pyip so that you can enter a shorter name when calling the module’s functions.


# In[3]:


#3. How do you distinguish between inputInt() and inputFloat()?

#inputint() expects an integer value as input but inputfloat() expects a float value i.e number containing a decimal.


# In[4]:


#4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?

#By using pyip.inputint(min=0, max=99)


# In[5]:


#5. What is transferred to the keyword arguments allowRegexes and blockRegexes?

#A list of regex strings that are either explicitly allowed or denied


# In[6]:


#6. If a blank input is entered three times, what does inputStr(limit=3) do?

#The function will raise RetryLimitException.


# In[7]:


#7. If blank input is entered three times, what does inputStr(limit=3, default='hello') do?

# The function returns the value 'hello'

