#!/usr/bin/env python
# coding: utf-8

# In[7]:


#1. Write a Python Program to Find the Factorial of a Number?
num = int(input("enter a value = "))
factorial = 1
if num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# In[8]:


#2. Write a Python Program to Display the multiplication Table?

num = int(input("enter a value = "))
num > 0
for i in range(1,11):
    print(num ,'x' , i ,'=' ,num*i)


# In[13]:


#3. Write a Python Program to Print the Fibonacci sequence?

nterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1


# In[3]:


#4. Write a Python Program to Check Armstrong Number?

num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# In[2]:


#5. Write a Python Program to Find Armstrong Number in an Interval?

sum = 0
for i in range(0,1000+1):
    sum = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if i == sum:
        print(i)
    
    
    


# In[12]:


#6. Write a Python Program to Find the Sum of Natural Numbers?

num = int(input("enter a value = "))

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
   print("The of natural no. sum is", sum)


# In[ ]:




