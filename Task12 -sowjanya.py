#!/usr/bin/env python
# coding: utf-8

# **while loops and their use in programming.**
# 1. Write a Python program that uses a while loop to print the numbers from `A` to `P`.
# 
# 2. Modify the program to print only the even numbers from `1 to 20 except mutiple of 3` using a while loop.
# 
# 3. Create a program that prompts the user for an integer input and then uses a while loop to print the countdown from `that number to 1`.
# 
# 
# 4. Write a Python program that uses a while loop to repeatedly ask the user to enter a number. If the user enters 0, exit the loop using the `break` statement. Otherwise, continue prompting for numbers.
# 
# 5. Create a program that uses a while loop to print the numbers from 1 to 20, but skip printing the numbers 5, 10, and 15 using the `continue` statement.
# 
# 6. Write a Python program that simulates a simple password entry system. Ask the user to enter a password, and use a while loop to repeatedly prompt for the password until the correct password "abc123" is entered. Once the correct password is entered, exit the loop.
# 
# 7. Calculate and print the sum of all the positive integers entered by the user.
# 
# 
# 
# .

# **1)Write a Python program that uses a while loop to print the numbers from A to P.**

# In[2]:


a=0
while a <=15:
    print(chr(65+a))
    a=a+1
    
    
    

    


# **2. Modify the program to print only the even numbers from `1 to 20 except mutiple of 3` using a while loop.**
# 

# In[3]:


a=1
while a <= 20:
    if a%2==0 and a%3!=0:
        print(a)
    a=a+1
            


# 3) **Create a program that prompts the user for an integer input and then uses a while loop to print the countdown from that number to 1.**

# In[6]:


a = int(input("enter the value : "))
while a >= 1:
    print(a)
    a=a-1


# 4.**Write a Python program that uses a while loop to repeatedly ask the user to enter a number. If the user enters 0, exit the loop using the break statement. Otherwise, continue prompting for numbers.**

# In[1]:


a= int(input("enter the number: "))
print(a)

while a:
    a=int(input("enter the number: "))
    if a == 0:
        break
    else:
        print(a)
        continue


# 5)**Create a program that uses a while loop to print the numbers from 1 to 20, but skip printing the numbers 5, 10, and 15 using the continue statement.**

# In[28]:


a=1
while a<=20:
    if a in [5,10,15]:
        pass
        a=a+1
    else:
        print(a)
        a=a+1


# 6)**Write a Python program that simulates a simple password entry system. Ask the user to enter a password, and use a while loop to repeatedly prompt for the password until the correct password "abc123" is entered. Once the correct password is entered, exit the loop.**

# In[27]:


a= input("enter the password: ")
while (a != "abc123"): 
        a=input("enter the password: ")


# 7) **Calculate and print the sum of all the positive integers entered by the user.**
# 

# In[29]:


num = int(input("how many numbers you want to add: "))
total=0
while num>0:
    b=int(input("enter the number : "))
    if(b>0):
        total += b
        num=num-1
        
                
    else:
        print("enter positive numbers only")
        
        
print("the sum of integers",total)  
    
    


# 
