#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. What are escape characters, and how do you use them?

#Escape carecters are used To insert characters that are illegal in a string,
#An escape character is a backslash \ followed by the character you want to insert
#Example = "Those dogs are \"pitbull\" by breed".


# In[2]:


#2. What do the escape characters n and t stand for?

# \n stands for new line
# \t stands for new tab


# In[1]:


#3. What is the way to include backslash characters in a string?

#Use the syntax "\\" within the string literal to represent a single backslash.


# In[2]:


#4.The string "howls's Moving Castle" is a correct value. Why isn't the single quote character in the word Howl's not escaped a problem?

#As you've used double quotes to mark the beginning and end of the string, so we can use single quote in middle.


# In[3]:


#5. How do you write a string of newlines if you don't want to use the n character?

#Multiline strings allow you to use newlines in strings without the \n escape character.


# In[4]:


#6. What are the values of the given expressions?

#'Hello, world!'[1]  = e
#'Hello, world!'[0:5] = Hello
#'Hello, world!'[:5]  = Hello
#'Hello, world!'[3:]  = lo, world!


# In[5]:


#7. What are the values of the following expressions?

#'Hello'.upper()   =    HELLO
#'Hello'.upper().isupper()  = True
#'Hello'.upper().lower()  = hello


# In[6]:


#8. What are the values of the following expressions?

#'Remember, remember, the fifth of July.'.split()  = ['Remember,', 'remember,', 'the', 'fifth', 'of', 'July.']
#'-'.join('There can only one.'.split())    =   'There-can-only-one.'


# In[9]:


#9. What are the methods for right-justifying, left-justifying, and centering a string?

#The rjust(), ljust(), and center() string methods are used respectively.


# In[ ]:


#10. What is the best way to remove whitespace characters from the start or end?

# .strip() , .lstrip(), rstrip() are used to remove the whitespace.

