
# coding: utf-8

# # Using Regular Expressions to search for matching information
# * Regular expressions can be useful to seek out imformation that matches your data set's information
# * For example, you could type a site name 4 different ways, but want to search for all of those data points instead of searching by each different style of input
# * Follow along in this exercise to see 3 examples of utilizing Regular Expressions. The first step is to import any necessary packages

# In[2]:


import re


# # Exercise 1: Time
# * Times after noon but before midnight in military time (12:01 - 23:59) 

# In[3]:


time= "12:01", "09:25","23:30", "11:59"
reg1=re.compile("(([1][3-9]|[2][0-3]):[0-5][0-9])|(12:[0-5][1-9])")
print(filter(reg1.match,time))


# In this example, we used a regex to filter out any times that do not match our target. (([1][2-9]|[2][0-3]):[0-5][0-9]) matched anything from 13:00 to 23:59 and our third section of (12:[0-5][1-9]) matched anything from 12:01 to 12:59.

# ## Exercise 2: Genus species names
# * Searching for names in the style of H. sapien

# In[4]:


names= "M. tuberculosis", "e. Coli", "E. coli", "Staph aureus"
reg2=re.compile("[A-Z]\\.\\s[a-z]+")
print(filter(reg2.match,names))


# In this example we used the expression [A-Z]\\.\\s[a-z]+ to indicate we wanted terms with only 1 capital letter, followed by  period, a space, and then one or more undercase letters(indicated by the plus sign at the end of the [a-z]

# ## Exercise 3: Social Security Numbers
# * Searching for numbers in the correct format xxx-xx-xxxx

# In[5]:


numbers= "123-12-1234", "Bob", "234-234-234", "999-88-7777", "Using this to find SS numbers to commit fraud is illegal"
reg3=re.compile("[0-9]{3}-[0-9]{2}-[0-9]{4}")
print(filter(reg3.match,numbers))


# In this last example, we used the expression [0-9]{3}-[0-9]{2}-[0-9]{4} to filter out anything that didn't follow the xxx-xx-xxxx format, including the dashes. Only numbers were allowed to fill the "x" spaces in the example.
# 
# With these 3 examples, you should have a firmer grasp on the benefits of using Regular Expressions to find terms in a series of strings. 
