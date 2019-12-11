#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,10]])
a_1 = a[[0,1,2],[1,1,1]]
print(a_1)


# In[ ]:


a_2= np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 
rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]]) 
a_3 = a_2[rows,cols] 

print(rows)
print(cols)
print('The corner elements of this array are:' )
print(a_3)


# In[ ]:


#slicing
a_4 = np.array([[1,2,3],[8,9,10],[4,5,6],[10,20,30]])
a_5 = a_4[1:4,1:3]
print(a_5)


# In[ ]:


#advanced sclicing
a_6= np.array([[1,2,3],[8,9,10],[4,5,6],[10,20,30]])
a_7=a_6[1:4,[1,2]]
print(a_7)


# In[ ]:


#boolean array indexing
a_8 = np.array([[1,2,3],[8,9,10],[4,5,6],[10,20,30]])
print(a_8[a_8>5])


# In[ ]:


a_9 = np.array([4,5,6,np.nan])
print(a_9[~np.isnan(a_9)])


# In[ ]:


a_10 = np.array([10, 1+2j, 3+5j], dtype='complex')
print(a_10[np.iscomplex(a_10)])


# In[ ]:


#broadcasting
import numpy as np
a_11 = np.array([[1,2,3],[2,3,4]])
a_12 = np.array([[4,5,6],[1,2,3]])
print(a_11)
a_13 = a_11 * a_12
print(a_13)


# In[ ]:


a_14 = a_11 + a_12
print(a_14)


# In[ ]:


a_15 = np.arange(0,60,5)
a_15 = a_15.reshape(3,4)
print(a_15)
print('\n')
for x in np.nditer(a_15):
    print(x)


# In[ ]:


a_16 = np.arange(0,60,5)
a_17 = a_16.reshape(3,4)
print(a_17)
#transpose
a_18 = a_17.T
print(a_18)
for y in np.nditer(a_18):
    print(y)


# In[ ]:


#sorting c type
a_19 = a_18.copy(order = 'c')
print(a_19)
for a_20 in np.nditer(a_19):
    print(a_20)


# In[ ]:


#sorting f type
a_19 = a_18.copy(order = 'F')
print(a_19)
for a_20 in np.nditer(a_19):
    print(a_20)


# In[ ]:


#modifying array
a_21 = np.arange(0,60,5)
a_21 = a_21.reshape(3,4)
print(a_21)
for x in np.nditer(a_21, op_flags = ['readwrite']):
    x[...] = 2*x
print(a_21)


# In[ ]:


a_22 = np.arange(0,60,5)
a_22 = a_22.reshape(3,4)
print(a_22)
for x in np.nditer(a_22, flags = ['external_loop'] , order = 'F'):
    print(x)


# In[ ]:


#broadcasting iteration
a_23 = np.array([1,2,3,4], dtype = int)
for x,y in np.nditer([a_22,a_23]):
    print("{}:{}".format(x,y))


# In[ ]:


#flat will give specific element in aray
import numpy as np
a_24 = np.arange(16).reshape(4,4)
a_25 = a_24.flat[1]
print(a_25)


# In[ ]:


#Flatten will make array one dimension (default order 'C')
a_26 = a_24.flatten()
print(a_26)


# In[ ]:


a_27 = a_24.flatten(order='F')
print(a_27)


# In[ ]:


#ravel is same as flatten
a_28 = a_24.ravel()
print(a_28)


# In[ ]:


a_29 = a_24.ravel(order='F')
print(a_29)


# In[ ]:


#roll axis
import numpy as np
a_30 = np.arange(8).reshape(2,2,2)
print(a_30)


# In[ ]:


#along width to along depth
a_31 = np.rollaxis(a_30,2)
print(a_31)


# In[ ]:


#along width to height
a_32 = np.rollaxis(a_30,2,1)
print(a_32)


# In[ ]:


#swapaxis along depth to width
a_33 = np.swapaxes(a_30,2,0)
print(a_33)


# In[ ]:


a_34 = np.arange(4).reshape(1,4)
print(a_34)
print('\n')
a_35 = np.broadcast_to(a_34,(4,4))
print(a_35)


# In[ ]:


#expand dims
a_36 = np.arange(8).reshape(4,2)
print(a_36)
print('\n')
a_37 = np.expand_dims(a_36, axis = 0)
print(a_37)
print('\n')
a_38 = np.expand_dims(a_36, axis = 1)
print(a_38)
print('\n')
print(a_37.ndim,a_38.ndim)
print('\n')
print(a_37.shape,a_38.shape)


# In[ ]:


#squeez
a_39 = np.arange(9).reshape(1,3,3)
print(a_39)
print('\n')
a_40 = np.squeeze(a_39)
print(a_40)
print('\n')
print(a_39.shape, a_40.shape)


# In[ ]:


#concatinate
a_41 = np.array([[1,2],[3,4]])
print(a_41)
print('\n')
a_42 = np.array([[5,6],[7,8]])
print(a_42)
print('\n')
a_43 = np.concatenate((a_41,a_42))
print(a_43)
print('\n')
a_44 = np.concatenate((a_42,a_41), axis =1)
print(a_44)
print(a_43.shape, a_44.shape)


# In[ ]:


#stack
a_45 = np.array([[1,2],[3,4]])
print(a_45)
print('\n')
a_46 = np.array([[5,6],[7,8]])
print(a_46)
print('\n')
a_47 = np.stack((a_45,a_46))
print(a_47)
print('\n')
a_48 = np.stack((a_45,a_46), axis =1)
print(a_48)
print(a_47.shape, a_48.shape)


# In[ ]:


a_49 = np.array([[1,2],[3,4]])
print(a_49)
print('\n')
a_50 = np.array([[5,6],[7,8]])
print(a_50)
print('\n')
#hstack same as conactinate axis 1
a_51 = np.hstack((a_49,a_50))
print(a_51)
print('\n')
#vstack same as concatinate axis 0
a_52 = np.vstack((a_49,a_50))
print(a_52)


# In[ ]:


#split
a_53 = np.arange(9)
print(a_53)
print('\n')
#split equally
a_54 = np.split(a_53,3)
print(a_54)
print('\n')
#split at specified position
a_55 = np.split(a_53,[5,8])
print(a_55)


# In[ ]:


a_55 = np.arange(16).reshape(4,4)
print(a_55)
a_56 = np.hsplit(a_55,2)
print(a_56)


# In[ ]:


a_58 = np.vsplit(a_55,2)
print(a_58)


# In[ ]:


#resize
a_59 = np.array([[1,2,3],[4,5,6]])
print(a_59)
print('\n')
a_60 = np.resize(a_59,(3,2))
print(a_60)
print('\n')
#Observe that first row of a is repeated in b since size is bigger 
a_61 = np.resize(a_59,(3,3))
print(a_61)


# In[ ]:


#append
a_62 = np.append(a_59,[[7,8,9]],axis=0)
print(a_62)
print('\n')
a_63 = np.append(a_59,[[7,8,9],[5,5,5]],axis=1)
print(a_63)


# In[ ]:


#insert array is flattend without axis
a_64 = np.insert(a_59,2,[3,3,3])
print(a_64)
# array with axis
a_65 = np.insert(a_59,1,[3], axis=0)
print(a_65)
a_66 = np.insert(a_59,1,[3], axis=1)
print(a_66)


# In[ ]:


#delete
a_67 = np.arange(12).reshape(3,4)
print(a_67)
print('\n')
#delete without passing axis
a_68 = np.delete(a_67,5)
print(a_68)
print('\n')
#delete with axis row
a_69 = np.delete(a_67,1, axis = 0)
print(a_69)
#delete with axis column
a_70 = np.delete(a_67,1, axis = 1)
print(a_70)


# In[86]:


#finding unique values
a_71 = np.array([5,2,6,2,7,5,6,8,2,9]) 
a_72 = np.unique(a_71)
print(a_72)
print('\n')
#Unique array and Indices array
a_72,indices = np.unique(a_71, return_index = True)
print(indices)


# In[ ]:




