#!/usr/bin/env python
# coding: utf-8

# In[4]:


#1. Write a Python Program to Find LCM?

def lcm(x, y):

   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm
lcm(60,60)


# In[6]:


#2. Write a Python Program to Find HCF?

def hcf(x,y):

    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

hcf(60,90)


# In[8]:


#3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

dec = int(input("Enter a decimal value = "))
print('binary value = ',bin(dec))
print('octal value = ',oct(dec))
print('hexadecimal value = ',hex(dec))


# In[10]:


#4. Write a Python Program To Find ASCII value of a character?

char = str(input("enter a value = "))
print("ASCII value is", ord(char))


# In[1]:


#5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")


# In[ ]:




