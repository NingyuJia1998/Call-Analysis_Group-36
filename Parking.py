#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)


# In[14]:


#import data
data=pd.read_csv('C://哥大//课程文件//tools for analytics//group project//data//311_Service_Requests_2020.csv',encoding='utf-8')
data.head(2)


# In[6]:


#choose one zip code
data_10025=data.loc[data['Incident Zip']==10025.0]
data_10025


# In[7]:


# save as csv file for further use
data_10025.to_csv('C://哥大//课程文件//tools for analytics//group project//data//data_10025.csv', encoding='utf-8-sig',index=False)


# In[10]:


# the Illegal Parking rate in 10025
data_10025_parking=data_10025.loc[data_10025['Complaint Type']=='Illegal Parking']
rate_10025=data_10025_parking.shape[0]/data_10025.shape[0]
rate_10025


# In[11]:


# the whole rate
data_parking=data.loc[data['Complaint Type']=='Illegal Parking']
rate=data_parking.shape[0]/data.shape[0]
rate


# In[13]:


higher_parking_proportion= rate_10025>rate
higher_parking_proportion


# In[ ]:




