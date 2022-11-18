#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

a = int(input("enter a value :"))
if a == 0:
    print("a is zero")
elif a > 0:
    print("a is positive")
else:
    print("a is negative")


# In[6]:


#2. Write a Python Program to Check if a Number is Odd or Even?

a = int(input("enter a value :"))

if a== 0:
    print(" a is zero")
elif a%2 == 0:
    print("a is Even")
else :
    print("a is Odd")


# In[7]:


#3. Write a Python Program to Check Leap Year?

a = int(input("enter a year = "))
if a%4==0:
    print("It is Leap year")
else:
    print("It is not a leap year")


# In[35]:


#4. Write a Python Program to Check Prime Number?

num = int(input("enter a value = "))
if num > 0:
    for i in range(2,num):
        if (num%i) == 0:
            print("It is not a prime number ")
            break
    else:
        print("It is prime number")
else:
    print("It is not a prime number")
    


# In[41]:


#5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?


for i in range(1,1000+1):
    if i > 0:
        for j in range(2,i):
            if (i%j) == 0:
                break
        else:
            print(i)
 


# In[ ]:




