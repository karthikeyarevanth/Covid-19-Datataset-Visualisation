#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplot import make_subplots
from datetime import datetime


# In[4]:


covid_df = pd.read_csv("C:/Users/ravi kumar/Desktop/Karthik Documents/covid_19_india.csv")


# In[7]:


covid_df.head()


# In[8]:


covid_df.info()


# In[9]:


covid_df.describe()


# In[5]:


vaccine_df= pd.read_csv("C:/Users/ravi kumar/Desktop/Karthik Documents/covid_vaccine_statewise.csv")


# In[12]:


vaccine_df.head()


# In[6]:


covid_df.drop(["Sno", "Time", "ConfirmedIndianNational", "ConfirmedForeignNational"], inplace = True,axis = 1)


# In[14]:


covid_df.head()


# In[7]:


covid_df["Date"] = pd.to_datetime(covid_df["Date"], format = "%Y-%m-%d")


# In[16]:


covid_df.head()


# In[17]:


covid_df.drop(["Sno", "Time", "ConfirmedIndianNational", "ConfirmedForeignNational"], inplace = True, axis = 1 )


# In[8]:


covid_df["Active_Cases"] = covid_df["Confirmed"] - ( covid_df["Cured"] + covid_df["Deaths"] )
covid_df.tail()


# In[10]:


statewise = pd.pivot_table(covid_df, values=["Confirmed", "Deaths" ,"Cured"], index= "State/UnionTerritory", aggfunc= max)


# In[11]:


#####Recovery Rate

statewise["Recovery Rate"] = statewise["Cured"]*100/statewise["Confirmed"]


# In[12]:


#####Mortality Rate

statewise["Mortality Rate"] = statetwise["Deaths"]*100/statewise["Confirmed"]


# In[13]:


statewise = statewise.sort_values(by = "Confirmed", ascending = "False")


# In[14]:


statewise.style.background_gradient(cmap = "cubehelix")


# In[15]:


#####Top 10 States with Actives cases

Top_10_active_cases = covid_df.groupby(by = "State/UnionTerritory").max()[["Active_Cases", "Date"]].sort_values(by=["Active_Cases"], ascending = False).reset_index()


# In[30]:


covid_df.tail()


# In[17]:


fig = plt.figure(figsize=(16,9))


# In[18]:


plt.title("Top 10 States with most Active cases in India", size = 25)


# In[19]:


ax = sns.barplot(data = Top_10_active_cases.iloc[:10], y ="Active_Cases", x = "State/UnionTerritory", linewidth = 2, edgecolor = "White") 


# In[20]:


#####Top 10 States with Actives cases

Top_10_active_cases = covid_df.groupby(by = "State/UnionTerritory").max()[["Active_Cases", "Date"]].sort_values(by=["Active_Cases"], ascending = False).reset_index()
fig = plt.figure(figsize=(16,9))
plt.title("Top 10 States with most Active cases in India", size = 25)
ax = sns.barplot(data = Top_10_active_cases.iloc[:10], y ="Active_Cases", x = "State/UnionTerritory", linewidth = 2, edgecolor = "White") 

plt.xlabel("STATES")
plt.ylabel("TOTAL ACTIVE CASES")
plt.show()


# In[21]:


#Top States with Highest Deaths
   
top_10_deaths = covid_df.groupby(by = "State/UnionTerritory").max()[["Deaths", "Date"]].sort_values(by=["Deaths"], ascending = False ).reset_index() 
fig = plt.figure(figsize=(25,16))
plt.title("Top 10 states with most deaths", Size = 25)
ax = sns.barplot(data = top_10_deaths.iloc[:12], y = "Deaths", x= "State/UnionTerritory", linewidth=2, edgecolor = "Black") 
plt.xlabel("STATES")
plt.ylabel("TOTAL DEATH COUNTS")
plt.show()


# In[67]:


#GROWTH TREND
 

fig = plt.figure(figsize  = (12,6))
ax = sns.lineplot(data = covid_df[covid_df["State/UnionTerritory"].isin(["Maharashtra", "Karnataka", "Kerala","Tamil Nadu","Uttar Pradesh"]),x ="Date", y =  "Active_Cases", hue = "State/UnionTerritories" ])
ax.set_title("Top 5 Affected States in India", size = 16)


# In[23]:


vaccine_df.head()


# In[36]:


vaccine_df.rename(columns = {"Updated On" : "Vaccine_date"}, inplace = True)


# In[37]:


vaccine_df.head(10)


# In[40]:


vaccine_df.info()


# In[41]:


vaccine_df.isnull().sum()


# In[48]:


vaccination = vaccine_df.drop(columns = ["Sputnik V (Doses Administered)", "AEFI","18-44 Years (Doses Administered)", "45-60 Years (Doses Administered)" , "60+ Years(Individuals Vaccinated)" ], axis = 1)


# In[49]:


vaccination.head()


# In[54]:


#Female vs Male Vaccination

male = vaccination["Male(Individuals Vaccinated)"].sum()
female = vaccination["Female(Individuals Vaccinated)"].sum()
px.pie(names=["Male", "Female"], values=[male,female], title = "Male and Female Vaccination") 


# In[58]:


#Removw where state is India 
vaccine = vaccine_df[vaccine_df.State != "India"]
vaccine


# In[61]:


vaccine.rename(columns = {"Total Individuals Vaccinated" : "Total"}, inplace = True)
vaccine.head()


# In[62]:


#States with most vaccinated People

max_vac = vaccine.groupby("State")["Total"].sum().to_frame("Total")
max_vac = max_vac.sort_values("Total", ascending = False)[:5]
max_vac


# In[65]:


fig = plt.figure(figsize=(25,16))
plt.title("Top 5 states with most Vaccines", Size = 9)
x = sns.barplot(data = max_vac.iloc[:10], y = max_vac.Total, x= max_vac.index, linewidth=2, edgecolor = "Black") 
plt.xlabel("STATES")
plt.ylabel("VACCINATION")
plt.show()


# In[90]:


min_vac = vaccine.groupby("State")["Total"].sum().to_frame("Total")
min_vac = min_vac.sort_values("Total", ascending = True )[:5]
min_vac


# In[ ]:





# In[91]:


fig = plt.figure(figsize=(25,16))
plt.title("Top 5 states with most Vaccines", Size = 9)
x = sns.barplot(data = min_vac.iloc[:10], y = min_vac.Total, x= min_vac.index, linewidth=2, edgecolor = "Black") 
plt.xlabel("STATES")
plt.ylabel("VACCINATION")
plt.show()


# In[ ]:




