#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
a_1 = pd.Series(np.arange(1,51))
print(a_1.ndim)


# In[ ]:


print(a_1.axes)


# In[ ]:


print(a_1.values)


# In[ ]:


print(a_1.head(6))


# In[ ]:


print(a_1.tail(6))


# In[ ]:


print(a_1.index)


# In[ ]:


a_2 = {'odd':np.arange(1,100,2),
      'even':np.arange(0,100,2)}
print(a_2)
a_3=pd.DataFrame(a_2)
print(a_3.sum())


# In[ ]:


print(a_3.mean())


# In[ ]:


print(a_3.min())


# In[ ]:


print(a_3.dtypes)


# In[ ]:


a_4 = pd.DataFrame(np.random.rand(5,4),columns=['col1','col2','col3','col4'])
print(a_4)
for key,value in a_4.iteritems():
    print(key,value)


# In[ ]:


for key,value in a_4.iterrows():
    print(key,value)


# In[ ]:


for key in a_4.itertuples():
    print(key)


# In[ ]:


#groupby
worldcup = {'team':['india','australia','ws','india','ws','us','nz','wi','england','india'],
           'rank':[7,4,5,6,7,8,9,2,4,5],
           'year':[1995,1994,1996,2000,2005,2010,2015,2016,2019,2000]}
a_5 = pd.DataFrame(worldcup)
print(a_5)
print(a_5.groupby('team').groups)


# In[ ]:


print(a_5.groupby(['team','rank']).groups)


# In[ ]:


a_5.describe()


# In[ ]:


a_6 = a_5.groupby('team')
for name,group in a_6:
    print(name)
    print(group)


# In[ ]:


print(a_6.get_group('india'))


# In[ ]:


print(a_5.groupby(['team','rank']).count())


# In[ ]:


import pandas as pd
world_champions = {'Team':['IND','AUS','WI','PAK','SRI'],
                  'Rank':[2,3,7,8,4],
                  'Year':[2011,2015,1979,1992,1996],
                  'points':[874,787,753,673,855]}
chockers = {'Team':['SA','NZ','ZB'],
           'Rank':[1,5,9],
           'points':[895,764,656]}
a_7 = pd.DataFrame(world_champions)
a_8 = pd.DataFrame(chockers)
print(pd.concat([a_7,a_8]))


# In[ ]:


print(pd.concat([a_7,a_8],axis=1))


# In[ ]:


print(a_7.append(a_8))


# In[ ]:


print(a_7)


# In[ ]:


print(a_7.merge(a_8))


# In[ ]:


world_champions = {'Team':['IND','AUS','WI','PAK','SRI'],
                  'Rank':[2,3,7,8,4],
                  'Year':[2011,2015,1979,1992,1996],
                  'points':[874,787,753,673,855]}
chockers = {'Team':['IND','AUS','WI','PAK','SRI','ZB'],
           'Rank':[2,3,7,8,4,9],
           'played':[11,10,11,9,8,5]}
a_9 = pd.DataFrame(world_champions)
a_10 = pd.DataFrame(chockers)
print(pd.merge(a_9,a_10))


# In[ ]:


print(pd.merge(a_9,a_10, on = 'Team'))


# In[ ]:


print(pd.merge(a_7,a_8,on = 'Team',how = 'left'))


# In[ ]:


print(pd.merge(a_7,a_8,on = 'Team',how = 'right'))


# In[ ]:


print(pd.merge(a_9,a_10,on='Team',how = 'inner'))


# In[ ]:


print(pd.merge(a_9,a_10,on = 'Team',how = 'outer'))


# In[ ]:




