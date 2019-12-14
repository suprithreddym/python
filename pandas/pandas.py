#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
s = pd.Series()
print(s)


# In[ ]:


data = np.array(['a','b','c','d'])
print(data)
a_1 = pd.Series(data)
print(a_1)


# In[ ]:


a_2 = pd.Series(data,index=[100,101,102,103])
print(a_2)


# In[ ]:


#pandas with dictionaries
a_3 = {'a':1,'b':2,'c':3}
a_4 = pd.Series(a_3)
print(a_4)


# In[ ]:


a_5 = pd.Series(a_3,index=['b','c','d','a'])
print(a_5)


# In[ ]:


#Create a Series from Scalar
a_6 = pd.Series(5, index=[1,2,3,4,5])
print(a_6)


# In[ ]:


#Accessing Data from Series with Position
a_7 = pd.Series([5,6,7,8,9], index=[1,2,3,4,5])
print(a_7)


# In[ ]:


a_8 = pd.Series([5,6,7,8,9], index=['a','b','c','d','e'])
print(a_8)
print(a_8[4])
print(a_8[:3])
print(a_8[-3:])


# In[ ]:


#Retrieve Data Using Label (Index)
print(a_8['a'])


# In[ ]:


print(a_8[['a','c','e']])


# In[ ]:


print(a_8[['a','c','f']])


# In[ ]:


print(a_8['f'])


# In[ ]:


#dataframes
df = pd.DataFrame()
print(df)


# In[ ]:


a_1 = pd.DataFrame([1,2,3,4])
print(a_1)


# In[ ]:


a_2 = [['suppu',24],['sumanth',20],['sunitha',49],['siva',55]]
a_3 = pd.DataFrame(a_2,columns=['name','age'])
print(a_3)


# In[ ]:


#Create a DataFrame from Dict of ndarrays / Lists
a_4 = {'name':['suppu','soumya','akki','bharath','jayanth'],'age':[24,24,24,23,24]}
a_5 = pd.DataFrame(a_4,index=['rank1','rank2','rank3','rank4','rank5'])
print(a_5)


# In[ ]:


#Create a DataFrame from List of Dicts
a_6 = [{'a':1,'b':2,'c':3},{'a':2,'b':5,'c':10,'d':15}]
a_7 = pd.DataFrame(a_6)
print(a_7)


# In[ ]:


a_8 = pd.DataFrame(a_6,index=['first','second'])
print(a_8)


# In[ ]:


a_9 = pd.DataFrame(a_6,index=['first','second'],columns=['a','b'])
print(a_9)


# In[ ]:


#Create a DataFrame from Dict of Series
a_10 = {'one':pd.Series([1,2,3,4], index=['a','b','c','d']),
       'two': pd.Series([1,2,3],index=['a','b','c'])}
a_11 = pd.DataFrame(a_10)
print(a_11)


# In[ ]:


print(a_11['one'])


# In[ ]:


#adding column
a_11['three'] = pd.Series([4,5,6],index=['a','c','b'])
print(a_11)


# In[ ]:


#addding two columns
a_11['four'] = a_11['one'] + a_11['two']
print(a_11)


# In[ ]:


#delete column
del a_11['one']
print(a_11)


# In[ ]:


#delete using pop
a_11.pop('two')
print(a_11)


# In[ ]:


#loc function Selection by Label
print(a_11.loc['b'])


# In[ ]:


#iloc Selection by integer location
print(a_11.iloc[2])


# In[ ]:


#slicing rows
a_12 = {'one':pd.Series([1,2,3,4], index=['a','b','c','d']),
       'two': pd.Series([1,2,3],index=['a','b','c'])}
a_13 = pd.DataFrame(a_12)
print(a_13[2:4])


# In[ ]:


#ading rows
a_14 = pd.DataFrame([[1,2],[3,4],[5,6]],columns=['a','b'])
print(a_14)
print('--------')
a_15 = pd.DataFrame([[6,7],[8,9]],columns=['a','b'],index=[3,4])
a_14 = a_14.append(a_15)
print(a_14)


# In[ ]:


print(a_14.drop(3))


# In[ ]:


#panel
import numpy as np
import pandas as pd
a_16 = np.random.rand(2,4,5)
a_17 = pd.Panel(a_16)
print(a_17)


# In[ ]:


a_18 = {'item1':pd.DataFrame(np.random.rand(4,3)),
       'item2':pd.DataFrame(np.random.rand(4,2))}
a_19 = pd.Panel(a_18)
print(a_19)


# In[ ]:


#empty panel
a_20 = pd.Panel()
print(a_20)


# In[ ]:


import pandas as pd
a_21 = pd.read_excel('pandas.xlsx')
print(a_21)


# In[12]:


a_22 = pd.read_csv('pandas.csv')
print(a_22)


# In[ ]:


import pandas as pd
a_23 = a_21.to_excel('pandasnew.xlsx')
print(a_23)


# In[ ]:


import pandas as pd
a_24 = a_22.to_csv('pandasnew.csv')
print(a_24)


# In[8]:


import xml.etree.ElementTree as ET
tree = ET.parse('test.xml')
print(tree)


# In[10]:


import imageio
a_25 = imageio.imread('image.jpg')


# In[14]:


pd.isnull(a_22).any()
print(a_22.shape)


# In[16]:


a_26 = a_22.dropna(how='any',axis=0)
pd.isnull(a_26).any()
print(a_26.shape)


# In[35]:


#pandas fillna()
import pandas as pd
import numpy as np
a_27 = {'one':pd.Series([1,2,5],index = ['a','b','e']),
       'two':pd.Series([1,2,3,4],index= ['a','b','c','d'])}
tabel = pd.DataFrame(a_27)
print("Before\n",tabel)
tabel.fillna(-999,inplace=True) #or
#tabel['one'] = tabel['one'].replace(np.nan, -999)
#tabel['two'].fillna(-999,inplace=True)
print("after\n",tabel)


# In[39]:


import pandas as pd
import numpy as np
a_27 = {'one':pd.Series([1,2,5],index = ['a','b','e']),
       'two':pd.Series([1,2,3,4],index= ['a','b','c','d'])}
tabel = pd.DataFrame(a_27)
print("Before\n",tabel)
from sklearn.impute import SimpleImputer
a_28 = SimpleImputer(missing_values=np.nan,strategy = 'mean')
a_28.fit(tabel)
a_29 = a_28.transform(tabel.values)
print("after\n",pd.DataFrame(a_29,columns=['one','two']))


# In[47]:


a_30 = {'customer_id':pd.Series([1,2,3,4,5]),
       'loan_type':pd.Series(['Home loan','personal loan','education loan','Home loan','credit loan']),
       'income':pd.Series(['30k','25k','15k','40k','35k'])}
a_31 = pd.DataFrame(a_30)
a_31 = pd.get_dummies(a_31,prefix_sep='_',drop_first = True)
print(a_31)


# In[55]:


import pandas as pd
import numpy as np
a_31 = {'customer_id':pd.Series([1,2,3,4,5]),
       'loan_type':pd.Series(['Home loan','personal loan','education loan','Home loan','credit loan']),
       'income':pd.Series(['30k','25k','15k','40k','35k'])}
a_32 = pd.DataFrame(a_31)
print(a_32)
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
a_33 = a_32.apply(labelencoder.fit_transform)
print(a_33)


# In[56]:


from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder()
a_34 = onehotencoder.fit_transform(a_32).toarray()
print(a_34)


# In[61]:


#standard scaling
import numpy as np
from sklearn import preprocessing
a_34 = np.array([[-100.3],[27.5],[0],[-200.9],[1000]])
standardscaler = preprocessing.StandardScaler()
a_36 = standardscaler.fit_transform(a_34)
print(a_36)


# In[63]:


#minmaxscalar
minmaxscaler=preprocessing.MinMaxScaler(feature_range=(1,2))
a_37 = minmaxscaler.fit_transform(a_34)
print(a_37)


# In[64]:


#robustscalar
robust_scaler = preprocessing.RobustScaler()
a_38 = robust_scaler.fit_transform(a_34)
print(a_38)


# In[65]:


from sklearn import preprocessing
a_39 = np.array([[1,2,3,4],[5,6,7,8],[10,11.5,12,13]])
normalized_data = preprocessing.normalize(a_39)
print(normalized_data)


# In[ ]:




