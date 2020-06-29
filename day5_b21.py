#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Continuation with List:


# In[ ]:


#organising the list:


# In[1]:


cars=['maruti','honda','kia','bmw','benz','audi', 'ferrari','ford','datsun','chevrolet','mercedes','nissan',]


# In[2]:


type(cars)


# In[ ]:


#req: I want to organise the list in an alphabetical order ---, A -Z


# In[ ]:


#2 methods are there to achive.


# In[ ]:


# temp method =====> the changes will be of temp


# In[ ]:


#permanenet approch =====> parmanently changes will be implied.


# In[ ]:


# using the temp way. sorted method implementation # b, b, validation will be shifted to next letter e, m


# In[3]:


print(sorted(cars))


# In[ ]:


print(cars) #original order defined back...!


# In[ ]:


#parmanet way....implementation  of sort method.


# In[4]:


cars.sort()


# In[5]:


print(cars)


# In[6]:


print(cars)


# In[ ]:


***sort (no orginal order will be) vs sorted (orignal list order will be there)


# In[ ]:


#req: i want to print the list in the reverse order.


# In[7]:


print(cars)


# In[8]:


cars.reverse() #using the reverse method!


# In[9]:


print(cars)


# In[ ]:


# req: I wanted to know how many elements are there is my list...!


# In[10]:


len(cars) #to know the count.


# In[ ]:


Introduction to for loops:


# In[11]:


my_student = ['kiran','ezaz','senthil','yasmeen','chandra','bushra','sushmitha','imran','akram','anand','rakesh','maaz','khaja','faizan','ramesh','ramu',]


# In[ ]:


#req: i want to appreciate all of the above students


# In[12]:


print(f"keep up the good work, {my_student[0].title()}")


# In[13]:


print(f"keep up the good work, {my_student[1].title()}")


# In[14]:


print(f"keep up the good work, {my_student[12].title()}")


# In[15]:


print(f"keep up the good work, {my_student[15].title()}")


# In[18]:


type(my_students)


# In[19]:


type(my_student)


# In[20]:


len(my_student)


# In[21]:


print(my_student.upper())


# In[22]:


print(my_student.title())


# In[ ]:


#solution


# In[23]:


for student in my_students:
    print(f"keep up the good work, {students.title()}")


# In[24]:


for student in my_student:
    print(f"keep up the good work, {students.title()}")


# In[25]:


for student in my_student:
    print(f"keep up the good work, {students.title()}")


# In[26]:


for student in my_student:
    print(f"keep up the good work, {student.title()}")


# In[ ]:


#general syntax of a for loop:


# In[27]:


for tempvar in mainvar:
    print(tempvar)


# In[28]:


for x in my_students:
    print(x) #indentation


# In[29]:


for x in my_student:
	print(x) #indentation


# In[30]:


message= ['keep up the good work,']


# In[31]:


for y in message:
	print(y) #indentation


# In[32]:


print(x+y)


# In[33]:


print(x +y)


# In[34]:


print(y+,x)


# In[35]:


print(y+x)


# In[36]:


for batman in my_students:
    print(batman)


# In[37]:


for batman in my_student:
    print(batman)


# In[ ]:





# In[38]:


1strip ()


# In[ ]:


strip ()
rstrip()


# In[ ]:


#removing of white space


# In[39]:


lang='python '


# In[40]:


lang.rstrip()


# In[41]:


lang2= ' python'


# In[42]:


print(lang2)


# In[43]:


lang2.1strip


# In[44]:


lang2.lstrip


# In[45]:


lang3 = ' python '


# In[46]:


print(lang3)


# In[47]:


lang3.strip()


# In[48]:


lang3.rstrip()


# In[49]:


lang2.strip


# In[50]:


for student in my_student:
    print({student.title()})


# In[51]:


for student in my_student:
    print(student.upper())


# In[ ]:


for student in my_student:
    print(student.upper())


# In[52]:


for student in my_student:
    print(student.title())


# In[53]:


my_student.append('ashok')


# In[54]:


print(my_student)


# In[55]:


my_student.append('kishore','chandra','rasheed','daya','praveen',)


# In[57]:


my_student.append('kishore','chandra','rasheed','daya','praveen'())


# In[58]:


for student in my_student:
    print({student.append('kishore','chandra','rasheed','daya','praveen')})


# In[59]:


for student in my_student:
    print({student.append('kishore','chandra','rasheed','daya','praveen')()})


# In[60]:


my_student.append('gautham','kishore')


# In[61]:


my_student.extend(['gautham', 'kishore']) 


# In[62]:


print(my_student)


# In[63]:


len(my_student)


# In[ ]:




