#!/usr/bin/env python
# coding: utf-8

# # 5 stars artifacts

# ## Import necessary libraries

# In[8]:


import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import plotly.express as px
import plotly.io as pio


# ## Load Genshin Impact Artifacts dataset

# In[9]:


# Define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('../../../Genshin-admin/genshin-impact-artifacts-dc88c443e085.json', scope)

# Authorize the clientsheet 
client = gspread.authorize(creds)


# In[10]:


# Get the instance of the Spreadsheet
sheet = client.open('Genshin Impact artifacts dataset')

#Get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)


# In[11]:


# Get all the records of the data
records_data = sheet_instance.get_all_records()

# Convert the json to dataframe
genshin_df = pd.DataFrame.from_dict(records_data)

# View the top records
genshin_df.head()


# ## Dataset size

# In[12]:


five_stars_df = genshin_df.loc[genshin_df['rarity'] == 5]
five_stars_df.shape


# ## General data visualization

# ### Frequency of artifact types

# In[13]:


df = five_stars_df.groupby('artifact_type').size()
df = df.reset_index()
df.columns = ['Artifact type', 'Counts']


# In[15]:


fig = px.bar(df, x='Artifact type', y='Counts', color='Artifact type', 
             template = 'plotly_white', color_discrete_sequence = px.colors.qualitative.Prism)
fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
fig.show('sphinx_gallery')


# In[ ]:




