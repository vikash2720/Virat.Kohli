#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# In[3]:


data=pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Virat_Kohli.csv")


# In[4]:


print(data.head(5))


# In[5]:


print(data.isnull().sum())


# In[6]:


# Total Runs Between 18-Aug-08 - 22-Jan-17
data["Runs"].sum()


# In[7]:


# Average Runs Between 18-Aug-08 - 22-Jan-17
data["Runs"].mean()


# In[11]:


data.shape


# In[12]:


6164/132


# In[13]:


matches = data.index #no of matches(132)
figure = px.line(data, x=matches, y="Runs", 
                 title='Runs Scored by Virat Kohli Between 18-Aug-08 - 22-Jan-17')
figure.show()


# In[14]:


data.index


# In[18]:


(data["Runs"]>=100).sum() #no of centuries


# In[19]:


# Batting Positions
data["Pos"] = data["Pos"].map({3.0: "Batting At 3", 4.0: "Batting At 4", 2.0: "Batting At 2", 
                               1.0: "Batting At 1", 7.0:"Batting At 7", 5.0:"Batting At 5", 
                               6.0: "batting At 6"})

Pos = data["Pos"].value_counts()
label = Pos.index
counts = Pos.values
colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Number of Matches At Different Batting Positions')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# # In more than 68% of all the innings played by Virat Kohli, 
# #he batted in the third position. Now let’s have a look at the total runs scored by Virat Kohli in different positions:
# 

# In[20]:


label = data["Pos"]
counts = data["Runs"]
colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Runs By Virat Kohli At Different Batting Positions')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# # More than 72% of the total runs scored by Virat Kohli are while batting at 3rd position. So we can say batting at 3rd position is perfect for Virat Kohli.

# # Now let’s have a look at the number of centuries scored by Virat Kohli while batting in the first innings and second innings:

# In[21]:


centuries = data.query("Runs >= 100")
figure = px.bar(centuries, x=centuries["Inns"], y = centuries["Runs"], 
                color = centuries["Runs"],
                title="Centuries By Virat Kohli in First Innings Vs. Second Innings")
figure.show()


# # So most of the centuries are scored while batting in the second innings. By this, we can say that Virat Kohli likes chasing scores. Now let’s have a look at the kind of dismissals Virat Kohli faced most of the time:

# In[22]:


# Dismissals of Virat Kohli
dismissal = data["Dismissal"].value_counts()
label = dismissal.index
counts = dismissal.values
colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Dismissals of Virat Kohli')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# # So most of the time, Virat Kohli gets out by getting caught by the fielder or the keeper. Now let’s have a look at against which team Virat Kohli scored most of his runs:

# In[23]:


figure = px.bar(data, x=data["Opposition"], y = data["Runs"], color = data["Runs"],
            title="Most Runs Against Teams")
figure.show()


# # According to the above figure, Virat Kohli likes batting against Sri Lanka, Australia, New Zealand, West Indies, and England. But he scored most of his runs while batting against Sri Lanka. Now let’s have a look at against which team Virat Kohli scored most of his centuries:

# In[24]:


figure = px.bar(centuries, x=centuries["Opposition"], y = centuries["Runs"], 
                color = centuries["Runs"],
                title="Most Centuries Against Teams")
figure.show()


# # Most Centuries Against Teams
# So, most of the centuries scored by Virat Kohli were against Australia. Now let’s analyze Virat Kohli’s strike rate. To analyze Virat Kohli’s strike rate, I will create a new dataset of all the matches played by Virat Kohli where his strike rate was more than 120:

# In[25]:


strike_rate = data.query("SR >= 120")
print(strike_rate)


# # Now let’s see whether Virat Kohli plays with high strike rates in the first innings or second innings:

# In[26]:


figure = px.bar(strike_rate, x = strike_rate["Inns"], 
                y = strike_rate["SR"], 
                color = strike_rate["SR"],
            title="Virat Kohli's High Strike Rates in First Innings Vs. Second Innings")
figure.show()


# # So according to the above figure, Virat Kohli likes playing more aggressively in the first innings compared to the second innings. Now let’s see the relationship between runs scored by Virat Kohli and fours played by him in each innings:

# In[28]:


figure = px.scatter(data_frame = data, x="Runs",
                    y="6s", size="SR", trendline="ols", 
                    title= "Relationship Between Runs Scored and Sixes")
figure.show()


# # There is no strong linear relationship here. It means Virat Kohli likes playing fours more than sixes. So this is how you can analyze the performance of Virat Kohli or any other cricketer in the world.

# # So this is how you can perform Virat Kohli performance analysis using the Python programming language. Analyzing a player’s performance is one of the use cases of Data Science in sports analytics. I hope you liked this article on Virat Kohli performance analysis using Python. Feel free to ask valuable questions in the comments section below.
