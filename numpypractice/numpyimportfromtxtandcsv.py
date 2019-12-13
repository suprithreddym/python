#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
arr = np.loadtxt('test.txt')
print(arr)


# In[4]:


arr1 = np.genfromtxt('test.csv')
print(arr1)


# In[6]:


import numpy as np
np.savetxt('newtest.txt',arr)
np.savetxt('newtest.csv',arr1,delimiter=',')


# In[ ]:




