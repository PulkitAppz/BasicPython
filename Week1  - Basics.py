#!/usr/bin/env python
# coding: utf-8

# # Hello, Python World!

# In[ ]:


# This tutorial uses Python 3, because it more semantically correct and supports newer features.
# Lets Start with printing "Hello, Python World!"
print("Hello, Python World!")


# # Indentation
Python uses indentation for blocks, instead of curly braces. Both tabs and spaces are supported, but the standard indentation requires standard Python code to use four spaces. For example:
# In[ ]:


x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")


# # Variables and Types

# As we know that there are different data types like Integer ,character , Float etc. Python is completely object oriented, and not "statically typed". You do not need to declare variables before using them, or declare their type. Every variable in Python is an object.

# # Numbers

# In[ ]:


myNumber = 7  #This is integer variable
myfloat = 7.0 #This is float variable
myfloat1 = float(7) #This is float variable
mystring = 'hello' #This is String variable
mystring1 = "hello" #This is String variable
print(myNumber)
print(myfloat)
print(myfloat1)
print(mystring)
print(mystring1)


# The difference between the two is that using double quotes makes it easy to include apostrophes (whereas these would terminate the string if using single quotes)

# In[ ]:


mystring = "Don't worry about apostrophes"
print(mystring)


# Assignments can be done on more than one variable "simultaneously" on the same line like this

# In[ ]:


a, b = 3, 4


# String Concatenation

# In[ ]:


hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)


# # Lists

# In[ ]:


mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3


# # Basic Operators

# Arithmetic Operators

# In[ ]:


number = 1 + 2 * 3 / 4.0


# In[ ]:


remainder = 11 % 3


# In[ ]:


squared = 7 ** 2
cubed = 2 ** 3


# Using Operators with Strings

# In[ ]:


helloworld = "hello" + " " + "world" #String Concatenation 


# Python also supports multiplying strings to form a string with a repeating sequence:

# In[ ]:


lotsofhellos = "hello " * 10


# Using Operators with Lists

# In[ ]:


even_numbers = [2,4,6,8]
odd_numbers = [1,3,5]
all_numbers = odd_numbers + even_numbers
# this will join the above two list and this will not add these value at respective Index.


# Just as in strings, Python supports forming new lists with a repeating sequence using the multiplication operator:

# In[ ]:


print([1,2,3] * 3)


# # String Formatting

# Python uses C-style string formatting to create new, formatted strings. The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".

# In[ ]:


# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name) 
# %s is used to print the name variable above. Now just get in bit detail, what if we use %d instead of %s? This will give error because "name" variable is str i.e. string.
# The below  snippet explains the difference
name = "John"
age = 23
print("%s is %d years old." % (name, age))


# # Here are some basic argument specifiers you should know:
# 
# %s - String (or any object with a string representation, like numbers)
# 
# %d - Integers
# 
# %f - Floating point numbers
# 
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# 
# %x/%X - Integers in hex representation (lowercase/uppercase)
# 

# # Basic String Operations

# In[ ]:


astring = "Hello_world!"
print(len(astring)) # print length of astring


# In[ ]:


print(astring.index("o")) # prints index of 'o' character  i.e 4
print(astring.count("l")) # prints number of l in astring
print(astring[3:7]) # prints value from index 3 to 7-1 = 6th index


# The below statement prints the characters of string from 3 to 7 skipping one character. This is extended slice syntax. The general form is [start:stop:step].

# In[ ]:


print(astring[3:7:2])
# Explaination : The output will be "l_". Just get bit deeper here 3 is starting index, 7 is stopping index and 2 is step.
# Here if we do not have 2 in above example then output is "lo_w", now if we add step in it i.e. 2 then o in "lo_w" is at first step and "_" at second step after starting value. So the output will be starting value and step value i.e. "l_"


# # Excercise 
# 

# In[ ]:


print(astring[3:7])
print(astring[3:7:1])


# Why above two statements provide same output? (If still having problem solving this. Kindly, open an issue I will explain again.)
# 

# In[ ]:


print(astring[::-1]) 
#Explaination: The above statement prints reverese string.If we do not provide any value like this [:] or [::] it will simply print the string but if we add "-1" in step then it means we are going in reverse direction with step "one".  


# In[ ]:


print(astring.upper())
print(astring.lower())


# In[ ]:


print(astring.split(" "))
# this will split and output will be array(LIST).


# # Conditions

# In[ ]:


x = 3
print(x == 2) # prints out False
print(x == 3) # prints out True
print(x < 4) # prints out True


# Notice that variable assignment is done using a single equals operator "=", whereas comparison between two variables is done using the double equals operator "==". The "not equals" operator is marked as "!=".

# # Boolean operators

# In[ ]:


name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")
    
# In "AND" all the conditions need to be true whereas in "OR" if one of the condition need to be true. 


# # The "in" operator

# The "in" operator could be used to check if a specified object exists within an iterable object container, such as a list:

# In[ ]:


name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")


# # "if" statement using code blocks:

# In[ ]:


statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass


# # The 'is' operator

# Unlike the double equals operator "==", the "is" operator does not match the values of the variables, but the instances themselves. For example:

# In[ ]:


x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False


# # The "not" operator

# In[ ]:


print(not False) # Prints out True
print((not False) == (False)) # Prints out False


# # --------------------------------END(week 1)-----------------------------------

# WEEK 2 content:

# # 1.Loops

# # 2. "break" and "continue" statements

# # 3. Functions

# # 4. Classes and Objects

# # 5. Dictionaries

# In[ ]:




