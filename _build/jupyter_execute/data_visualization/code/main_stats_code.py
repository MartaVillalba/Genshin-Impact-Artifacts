#!/usr/bin/env python
# coding: utf-8

# # Plots source code

# ## Data load

# ### Import necessary libraries

# In[1]:


import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from IPython.display import HTML


# ### Load Genshin Impact Artifacts dataset

# In[2]:


# Define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('../../../Genshin-admin/genshin-impact-artifacts-dc88c443e085.json', scope)

# Authorize the clientsheet 
client = gspread.authorize(creds)


# In[3]:


# Get the instance of the Spreadsheet
sheet = client.open('Genshin Impact artifacts dataset')

#Get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)


# In[4]:


# Get all the records of the data
records_data = sheet_instance.get_all_records()

# Convert the json to dataframe
genshin_df = pd.DataFrame.from_dict(records_data)

# View the top records
genshin_df.head()


# ### Separe into 4 stars and 5 stars artifacts

# In[5]:


five_stars_df = genshin_df.loc[genshin_df['rarity'] == 5]


# In[6]:


four_stars_df = genshin_df.loc[genshin_df['rarity'] == 4]


# ### Dataset size

# In[7]:


five_stars_df.shape


# In[8]:


four_stars_df.shape


# ## Frecuency of main stats

# ### 5 stars artifacts

# In[9]:


df_5 = five_stars_df.groupby(['artifact_type', 'main_stat']).size()/five_stars_df.shape[0]*100
df_5 = df_5.reset_index()
df_5.columns = ['Artifact type', 'Main stat', 'Relative frecuency (%)']


# In[10]:


fig = px.bar(df_5, x='Main stat', y='Relative frecuency (%)', color='Artifact type', 
             template = 'plotly_white', color_discrete_sequence = px.colors.qualitative.Prism)
fig.update_traces(hoverlabel_font_color = 'white')
fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
fig.write_html('../figures/main_stats_5.html')
HTML('../figures/main_stats_5.html')


# ### 4 stars artifacts

# In[11]:


df_4 = four_stars_df.groupby(['artifact_type', 'main_stat']).size()/four_stars_df.shape[0]*100
df_4 = df_4.reset_index()
df_4.columns = ['Artifact type', 'Main stat', 'Relative frecuency (%)']


# In[12]:


fig = px.bar(df_4, x='Main stat', y='Relative frecuency (%)', color='Artifact type', 
             template = 'plotly_white', color_discrete_sequence = px.colors.qualitative.Prism)
fig.update_traces(hoverlabel_font_color = 'white')
fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
fig.write_html('../figures/main_stats_4.html')
HTML('../figures/main_stats_4.html')


# ### 4 stars vs. 5 stars artifacts

# #### Circlet of Logos

# In[13]:


df_circlet_5 = five_stars_df.groupby(['artifact_type', 'main_stat']).size()
df_circlet_5 = df_circlet_5.reset_index()
df_circlet_5.columns = ['Artifact type', 'Main stat', 'Relative frecuency (%)']
df_circlet_5 = df_circlet_5[df_circlet_5['Artifact type'] == 'Circlet of Logos']
df_circlet_5['Relative frecuency (%)'] = df_circlet_5['Relative frecuency (%)']/df_circlet_5['Relative frecuency (%)'].sum()*100


# In[14]:


df_circlet_4 = four_stars_df.groupby(['artifact_type', 'main_stat']).size()
df_circlet_4 = df_circlet_4.reset_index()
df_circlet_4.columns = ['Artifact type', 'Main stat', 'Relative frecuency (%)']
df_circlet_4 = df_circlet_4[df_circlet_4['Artifact type'] == 'Circlet of Logos']
df_circlet_4['Relative frecuency (%)'] = df_circlet_4['Relative frecuency (%)']/df_circlet_4['Relative frecuency (%)'].sum()*100


# In[15]:


fig = make_subplots(rows = 1, cols = 2, specs = [[{'type':'domain'}, {'type':'domain'}]])
fig.add_trace(go.Pie(labels = df_circlet_5['Main stat'], values = df_circlet_5['Relative frecuency (%)'], 
                     name="5 stars", sort = False), 1, 1)
fig.add_trace(go.Pie(labels = df_circlet_4['Main stat'], values = df_circlet_4['Relative frecuency (%)'], 
                     name="4 stars", sort = False), 1, 2)
fig.update_traces(hole=.4, hoverinfo="label+percent+name", hoverlabel_font_color = 'white')

fig.update_layout(title_text="Relative frecuency (%) of main stats in Circlet of Logos",
                  colorway = px.colors.qualitative.Prism,
                  margin=dict(t=50, b=0, l=0, r=0),
                  annotations=[dict(text='5 stars', x=0.18, y=0.5, font_size=15, showarrow=False),
                              dict(text='4 stars', x=0.815, y=0.5, font_size=15, showarrow=False)])
fig.write_html('../figures/main_stats_circlet_pie.html')
HTML('../figures/main_stats_circlet_pie.html')


# #### Goblet of Eonothem

# In[16]:


df_goblet_5 = five_stars_df.groupby(['artifact_type', 'main_stat']).size()
df_goblet_5 = df_goblet_5.reset_index()
df_goblet_5.columns = ['Artifact type', 'Main stat', 'Relative frecuency (%)']
df_goblet_5 = df_goblet_5[df_goblet_5['Artifact type'] == 'Goblet of Eonothem']
df_goblet_5['Relative frecuency (%)'] = df_goblet_5['Relative frecuency (%)']/df_goblet_5['Relative frecuency (%)'].sum()*100


# In[17]:


df_goblet_4 = four_stars_df.groupby(['artifact_type', 'main_stat']).size()
df_goblet_4 = df_goblet_4.reset_index()
df_goblet_4.columns = ['Artifact type', 'Main stat', 'Relative frecuency (%)']
df_goblet_4 = df_goblet_4[df_goblet_4['Artifact type'] == 'Goblet of Eonothem']
df_goblet_4['Relative frecuency (%)'] = df_goblet_4['Relative frecuency (%)']/df_goblet_4['Relative frecuency (%)'].sum()*100


# In[18]:


fig = make_subplots(rows = 1, cols = 2, specs = [[{'type':'domain'}, {'type':'domain'}]])
fig.add_trace(go.Pie(labels = df_goblet_5['Main stat'], values = df_goblet_5['Relative frecuency (%)'], 
                     name="5 stars", sort = False), 1, 1)
fig.add_trace(go.Pie(labels = df_goblet_4['Main stat'], values = df_goblet_4['Relative frecuency (%)'], 
                     name="4 stars", sort = False), 1, 2)
fig.update_traces(hole=.4, hoverinfo="label+percent+name", hoverlabel_font_color = 'white')

fig.update_layout(title_text="Relative frecuency (%) of main stats in Goblet of Eonothem",
                  colorway = px.colors.qualitative.Prism,
                  margin=dict(t=50, b=0, l=0, r=0),
                  annotations=[dict(text='5 stars', x=0.18, y=0.5, font_size=15, showarrow=False),
                              dict(text='4 stars', x=0.815, y=0.5, font_size=15, showarrow=False)])
fig.write_html('../figures/main_stats_goblet_pie.html')
HTML('../figures/main_stats_goblet_pie.html')


# #### Sands of Eon

# In[19]:


df_sands_5 = five_stars_df.groupby(['artifact_type', 'main_stat']).size()
df_sands_5 = df_sands_5.reset_index()
df_sands_5.columns = ['Artifact type', 'Main stat', 'Relative frecuency (%)']
df_sands_5 = df_sands_5[df_sands_5['Artifact type'] == 'Sands of Eon']
df_sands_5['Relative frecuency (%)'] = df_sands_5['Relative frecuency (%)']/df_sands_5['Relative frecuency (%)'].sum()*100


# In[20]:


df_sands_4 = four_stars_df.groupby(['artifact_type', 'main_stat']).size()
df_sands_4 = df_sands_4.reset_index()
df_sands_4.columns = ['Artifact type', 'Main stat', 'Relative frecuency (%)']
df_sands_4 = df_sands_4[df_sands_4['Artifact type'] == 'Sands of Eon']
df_sands_4['Relative frecuency (%)'] = df_sands_4['Relative frecuency (%)']/df_sands_4['Relative frecuency (%)'].sum()*100


# In[21]:


fig = make_subplots(rows = 1, cols = 2, specs = [[{'type':'domain'}, {'type':'domain'}]])
fig.add_trace(go.Pie(labels = df_sands_5['Main stat'], values = df_sands_5['Relative frecuency (%)'], 
                     name="5 stars", sort = False), 1, 1)
fig.add_trace(go.Pie(labels = df_sands_4['Main stat'], values = df_sands_4['Relative frecuency (%)'], 
                     name="4 stars", sort = False), 1, 2)
fig.update_traces(hole=.4, hoverinfo="label+percent+name", hoverlabel_font_color = 'white')

fig.update_layout(title_text="Relative frecuency (%) of main stats in Sands of Eon",
                  colorway = px.colors.qualitative.Prism,
                  margin=dict(t=50, b=0, l=0, r=0),
                  annotations=[dict(text='5 stars', x=0.18, y=0.5, font_size=15, showarrow=False),
                              dict(text='4 stars', x=0.815, y=0.5, font_size=15, showarrow=False)])
fig.write_html('../figures/main_stats_sands_pie.html')
HTML('../figures/main_stats_sands_pie.html')


# In[ ]:




