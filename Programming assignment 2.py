#!/usr/bin/env python
# coding: utf-8

# In[10]:


#1. Write a Python program to convert kilometers to miles?

km = float(input("km = "))
conver_fac = 0.62137
print("miles = ", km*conver_fac)


# In[2]:


#2. Write a Python program to convert Celsius to Fahrenheit?

Celsius = float(input("Celsius = "))

print("Fahrenheit = ", Celsius*1.8+32)


# In[14]:


#3. Write a Python program to display calendar?

import calendar
yy = int(input("year : "))
m = int(input("month : "))
print(calendar.month(yy,m))


# In[16]:


#4. Write a Python program to solve quadratic equation?

import cmath

a = 1
b = 6
c = 5
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print("the solutions are {0} and {1}".format(sol1,sol2))


# In[18]:


#5. Write a Python program to swap two variables without temp variable?

a = 10
b = 20 

a,b = b,a

print("swaped vaue of a",a)
print("swaped vaue of b",b)


# In[ ]:




