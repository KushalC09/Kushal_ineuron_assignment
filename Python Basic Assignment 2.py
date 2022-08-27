#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1.What are the two values of the Boolean data type? How do you write them?

#Two boolean Values are True and False
1==1  #True if statement is true 
2<1   #False if statement is false


# In[4]:


#2. What are the three different types of Boolean operators?

#the three different types of Boolean operators are AND, OR , NOT


# In[ ]:


#3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).

# 1 denotes true 0 denotes false

#Truth Table for AND
A B output
0 0 0
0 1 0
1 0 0
1 1 1

#Truth Table for OR
A B output
0 0 0
0 1 1
1 0 1
1 1 1

#Truth Table for NOT
A output
0 1
1 0


# In[7]:


#4. What are the values of the following expressions?

(5 > 4) and (3 == 5)
#ANS = False


# In[9]:


not (5 > 4)
#ANS = False


# In[11]:


(5 > 4) or (3 == 5)
#ANS = True


# In[13]:


not ((5 > 4) or (3 == 5))
#ANS = False


# In[14]:


(True and True) and (True == False)
#ANS = False


# In[15]:


(not False) or (not True)
#ANS = True


# In[16]:


#5. What are the six comparison operators?

#the six comparison operators are :
#Equal  x == y
#Not equal  x != y
#Greater than  x > y
#Less than  x < y
#Greater than or equal to  x >= y
#Less than or equal to  x <= y


# In[17]:


#6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.

#The difference is that the equal to ('==') operator checks whether the two given operands are equal or not wheather the assignment operators assign the value to the variable on the left.


# In[18]:


#7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')

The three blocks are:
    
#1)if spam == 10:
print('eggs')

#2)if spam > 5:
print('bacon')

#3)else:
print('ham')
print('spam')
print('spam')


# In[5]:


#8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

spam = int(input("Enter a integer value = "))
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")


# In[ ]:


#9.If your programme is stuck in an endless loop, what keys you’ll press?

#If program is stuck in endless loop we will press ctrl+c.
    
   
    
    


# In[1]:


#10. How can you tell the difference between break and continue?

#The difference is when the loop execute the break statement , it exit from the current loop and hand control to the next loop
#whereas, the continue statement will move the execution to the start of the loop.


# In[7]:


#11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

#Ans = In a for loop, there is no diffference between range(10), range(0, 10), and range(0, 10, 1) for every expression the output is same(0
1
2
3
4
5
6
7
8
9)


# In[5]:


#12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

#for loop:
for i in range(1,11):
    print(i)


# In[7]:


#12.
#while loop:
i = 0
while i<10:
    i+=1
    print(i)


# In[ ]:


#13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

#After importing spam function can be called with spam.bacon().


# In[ ]:




