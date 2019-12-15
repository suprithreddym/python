#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd


# In[ ]:


import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5])
plt.show()


# In[ ]:


x= range(11)
plt.plot(x,[x1**2 for x1 in x ])
plt.show()


# In[ ]:


plt.plot(x,[x1 for x1 in x])
plt.plot(x,[x1*x1 for x1 in x])
plt.plot(x,[x1*x1*x1 for x1 in x])
plt.show()


# In[ ]:


plt.plot([1,2,3,4],[5,6,7,8])


# In[ ]:


x=range(5)
plt.figure()
plt.plot(x,[x1 for x1 in x],
         x,[x1*2 for x1 in x],
         x,[x1*4 for x1 in x])
plt.grid(True)
plt.show()


# In[ ]:


x=range(5)
plt.figure()
plt.plot(x,[x1 for x1 in x],
         x,[x1*2 for x1 in x],
         x,[x1*4 for x1 in x])
plt.grid(True)
plt.axis([-1,5,-1,10])
plt.show()


# In[ ]:


x=range(5)
plt.figure()
plt.plot(x,[x1 for x1 in x],
         x,[x1*2 for x1 in x],
         x,[x1*4 for x1 in x])
plt.grid(True)
plt.xlim(-1,5)
plt.xlim(-1,10)
plt.show()


# In[ ]:


x=range(5)
plt.figure()
plt.plot(x,[x1 for x1 in x],
         x,[x1*2 for x1 in x],
         x,[x1*4 for x1 in x])
plt.grid(True)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()


# In[ ]:


x=range(5)
plt.figure()
plt.plot(x,[x1 for x1 in x],
         x,[x1*2 for x1 in x],
         x,[x1*4 for x1 in x])
plt.grid(True)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('polynomial graph')
plt.show()


# In[ ]:


x=range(5)
plt.figure()
plt.plot(x,[x1 for x1 in x],label='linear')
plt.plot(x,[x1*2 for x1 in x],label = 'square')
plt.plot(x,[x1*4 for x1 in x],label = 'quarted')
plt.grid(True)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('polynomial graph')
plt.legend(loc=5)
plt.show()


# In[ ]:


import numpy as mp
x=np.arange(5)
plt.figure()
plt.plot(x,x,label='linear')
plt.plot(x,x*x,label = 'square')
plt.plot(x,x*x*x,label = 'cube')
plt.grid(True)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('polynomial graph')
plt.legend()
plt.show()


# In[ ]:


import numpy as mp
x=np.arange(5)
plt.figure()
plt.plot(x,x,label='linear')
plt.plot(x,x*x,label = 'square')
plt.plot(x,x*x*x,label = 'cube')
plt.grid(True)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('polynomial graph')
plt.legend()
plt.savefig('plot.jpg')
plt.show()


# In[ ]:


#color controlling
y = np.arange(1,3)
plt.plot(y,'y')
plt.plot(y+5,'m')
plt.plot(y+10,'k')
plt.show()


# In[ ]:


#control style
y = np.arange(1,3)
plt.plot(y,ls='--',c='y')
plt.plot(y+5,'-.')
plt.plot(y+10,':')
plt.show()


# In[ ]:


a_1 = np.random.rand(100,100)
plt.hist(a_1)
plt.show()


# In[ ]:


a_1 = np.random.rand(100,100)
plt.hist(a_1,bins =5)
plt.show()


# In[ ]:


#Bar chart
plt.bar([1,2,3],[1,4,9])
plt.show()


# In[ ]:


#scatter plot
x=np.random.rand(1000)
y=np.random.rand(1000)
plt.scatter(x,y)
plt.show()


# In[ ]:


#heat map
a_2 = np.random.rand(16,16)
plt.imshow(a_2,cmap='hot',interpolation='nearest')
plt.show()


# In[ ]:


#pie chart
plt.figure(figsize = (3,3))
x=[40,20,5]
labels = ['Bikes','Cars','Buses']
plt.pie(x,labels=labels)
plt.show()


# In[ ]:


#sea born
from numpy import mean
import seaborn as sns
iris = sns.load_dataset('iris')
sns.barplot(x='species',
           y='sepal_width',
           data = iris,
           estimator = mean,
           palette = 'spring')


# In[ ]:


#heat map
flights = sns.load_dataset('flights')
flights = flights.pivot("month","year","passengers")
sns.heatmap(flights,
           cmap="YlGnBu",
           linewidths=2,
           xticklabels=True,
           yticklabels=True)


# In[ ]:


#box plot
tips = sns.load_dataset('tips')
sns.boxplot(x="day",y="size",hue='sex',data=tips,palette='coolwarm')


# In[ ]:


tips.groupby('day').get_group('Sun')[['size','sex']]


# In[ ]:


tips.groupby('sex').get_group('Male')[['size']].describe()


# In[ ]:


tips.groupby('sex').get_group('Female')[['size']].describe()


# In[ ]:


tips = sns.load_dataset('tips')
sns.countplot(x='day',hue='sex',data=tips,palette='YlGnBu')


# In[ ]:




