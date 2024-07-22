#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


HR = pd.read_excel(r"C:\Users\harsh\OneDrive\Desktop\HR.xlsx")


# In[6]:


HR. shape


# In[9]:


HR.head(5)


# In[8]:


HR.tail()


# In[9]:


HR.columns


# In[14]:


HR = HR.drop(['Department'], axis = 1)
HR.head(5)


# In[15]:


HR.isnull()


# In[10]:


HR.drop_duplicates()
HR.dropna()


# In[12]:


corr_matrix=HR.corr()
plt.figure(figsize=(20,10))
sns.heatmap(corr_matrix,annot=True,cmap='coolwarm')
plt.title("correlation map for Numeric values")
plt.show()


# In[14]:


data=HR


# In[16]:


sns.countplot(data=HR, x="OverTime")
plt.title("OverTime")
plt.show()


# In[17]:


sns.countplot(data=HR, x="MaritalStatus")
plt.title("MaritalStatus")
plt.show()


# In[18]:


plt.figure(figsize=(9,5))
sns.countplot(data=HR,y='JobRole')
plt.title("Job Role")
plt.show()


# In[21]:


sns.countplot(data=HR, x="EducationField")
plt.title("Department")
plt.show()


# In[23]:


sns.countplot(data=HR, x="EducationField")
plt.title("EmployeeNumber")
plt.show()


# In[24]:


sns.countplot(data=HR,x="BusinessTravel")
plt.title("Business Travel")
plt.show()


# In[26]:


sns.countplot(data=HR,x="Department")
plt.show()


# In[28]:


sns.boxplot(data=HR,x="OverTime",y="Age")
plt.title("relationship between overtime and age")
plt.show()


# In[30]:


sns.histplot(data=HR,x="TotalWorkingYears",bins=10,kde=True)
plt.title("Total Working Years")
plt.show()


# In[32]:


sns.histplot(data=HR,x="Education",bins=10,kde=True)
plt.title("EducationLevel")
plt.show()


# In[33]:


sns.histplot(data=HR,x="NumCompaniesWorked",bins=10,kde=True)
plt.title("no of companies worked")
plt.show()


# In[34]:


sns.histplot(data=HR,x="DistanceFromHome",bins=10,kde=True)
plt.title("Distance from home")
plt.show()


# In[35]:


sns.histplot(data=HR,x="MonthlyIncome",bins=10,kde=True)
plt.title("Monthly income Distribution")
plt.show()


# In[36]:


plt.figure(figsize=(10,5))
sns.boxplot(data=HR,x="JobRole",y="MonthlyIncome")
plt.title("Salary by Job Role")
plt.xticks(rotation=90)
plt.show()


# In[37]:


plt.figure(figsize=(10,5))
sns.countplot(data=HR,x="JobRole",hue="Attrition")
plt.title("Attrition by Job Role")
plt.xticks(rotation=90)
plt.show()


# In[38]:


plt.figure(figsize=(10,5))
sns.boxplot(data=HR,x="Department",y="Age")
plt.title("Age Distribution By Department")

plt.show()


# In[39]:


sns.histplot(data=HR,x="YearsAtCompany",bins=10,kde=True)
plt.title("Years At Company Distribution")
plt.show()


# In[ ]:




