#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a = np.array([1,2,3])
print(a)


# In[4]:


import numpy as np
a_2 = np.array([3,4,5], dtype='complex')
print(a_2)


# In[3]:


import numpy as np
a_1 = np.array([2,5,6], ndmin=3)
print(a_1)


# In[8]:


import numpy as np
a_3 = np.dtype('i4')
print(a_3)


# In[11]:


import numpy as np
a_4 = np.array([[1,2,3],[5,6,7]])
print(a_4.shape)


# In[12]:


a_5 = a_4.reshape(3,2)
print(a_5)


# In[14]:


a_6 = np.arange(15)
print(a_6)


# In[21]:


a_7 = np.arange(24)
a_7.ndim

a_8=a_7.reshape(2,4,3)
print(a_8)


# In[22]:


a_9 = a_8.itemsize
print(a_9)


# In[24]:


a_10 = np.empty([3,2])
print(a_10)


# In[25]:


a_11 = np.zeros(6)
print(a_11)


# In[26]:


a_12 = np.zeros(6, dtype=np.int)
print(a_12)


# In[28]:


a_13 = np.zeros(6, dtype=[('x','i4'),('y','i4')])
print(a_13)


# In[30]:


a_14 = np.ones(6)
print(a_14)


# In[31]:


#as array is used for converting tuple into array
a_15 = np.asarray((1,2,3))
print(a_15)


# In[38]:


a_16 = range(5) 
it = iter(a_16)
a_17 = np.fromiter(it, dtype = int) 
print(a_17)


# In[39]:


a_18 = np.linspace(15,20,2)
print(a_18)


# In[41]:


a_19 = np.linspace(15,20,5, endpoint = True )
print(a_19)


# In[42]:


a_20 = np.linspace(15,20,5, endpoint = False )
print(a_20)


# In[43]:


#retstep here is 1.25
a_21 = np.linspace(15,20,5, retstep = True )
print(a_21)


# In[45]:


#default base is 10
a_22 = np.logspace(1.0,2.0,num=10 )
print(a_22)


# In[46]:


a_23 = np.logspace(1.0,2.0,num=10, base=2)
print(a_23)


# In[47]:


x = np.arange(20)
a_24 = slice(2,15,3)
print(x[a_24])


# In[48]:


x = np.arange(20)
a_25 = x[2:15:3]
print(a_25)


# In[52]:


a_26 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a_26[1:])


# In[61]:


a_27 = np.array([[1,2,3],[4,5,6],[7,8,9]])
#items in first column
print(a_27[...,0])
#items in second row
print(a_27[1,...])
#items from second column
print(a_27[...,1:])


# In[ ]:




