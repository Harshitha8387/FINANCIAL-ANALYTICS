#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd


# In[6]:


df=pd.read_csv(r"C:\Users\harsh\Downloads\FAD.csv")
df


# In[2]:


df.head()


# In[3]:


import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as mp
import warnings
warnings.filterwarnings('ignore')


# In[4]:


df.tail()


# In[12]:


df.head(20)


# In[9]:


df.info()


# In[10]:


df


# In[11]:


df.columns


# In[13]:


df.info()


# In[14]:


df.isnull().sum()


# In[8]:


df.duplicated().sum()


# In[11]:


df['Mar Cap - Crore'].dtype


# In[12]:


df['Name'].dtype


# In[13]:


df['Sales Qtr - Crore'].dtype


# In[15]:


df[11:28]


# In[ ]:




