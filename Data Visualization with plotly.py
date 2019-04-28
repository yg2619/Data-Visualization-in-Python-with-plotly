#!/usr/bin/env python
# coding: utf-8

# # Project: DC vs Marvel: The Rise of Superheroes

# # Import Dataset

# In[2]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


dc_filename = '/Users/yirouge/Python/comic-characters/dc-wikia-data.csv'
marvel_filename = '/Users/yirouge/Python/comic-characters/marvel-wikia-data.csv'


# In[4]:


dc = pd.read_csv(dc_filename)
marvel = pd.read_csv(marvel_filename)


# # Data Visualization - Character Origin Year & Appearances
# ## DC vs Marvel: Character Origin Year Distribution
# The following codes need to use the module plotly and its Python package needs to be installed inside your terminal first using `conda install -c plotly plotly `.

# In[5]:


import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)


# In[6]:


year_count_dc = dc.YEAR.value_counts()
year_count_marvel = marvel.Year.value_counts()
trace1 = go.Bar(
    x = year_count_dc.index,
    y = year_count_dc.values,
    name = 'DC Characters',
    marker = dict(
        color = 'rgb(49,130,189)',
    )
)
trace2 = go.Bar(
    x = year_count_marvel.index,
    y = year_count_marvel.values,
    name = 'Marvel Characters',
    marker = dict(
        color = 'rgb(204,204,204)',
    )
)

data = [trace1,trace2]
layout = go.Layout(
    xaxis=dict(title = 'Origin Year'),
    yaxis=dict(title = 'Counts'),
    title='Character Origin Year Distribution',
    barmode='group',
)

fig = go.Figure(data=data,layout=layout)
iplot(fig,filename='grouped-bar', image='jpeg')


# Based on the bar chart above, it can be seen that both DC and Marvel have had three peaks in creating new characters during the same time period. In addition, if we look into the political background of these time periods, we can see that important political events around the world have greatly influenced the emergence of superheroes in the comic books of both DC and Marvel.
# 
# `1940s: World War II & Great Depression`
# 
# Both the World War II and the Great Depression has stimulated people's urge for victory and justice. Superhero stories emerged accordingly as they are the adventures of powerful individuals to use their abilities to impose personal morality on the world through violence.
# DC and Marvel started their business during this phase and created popular characters such as Batman and Captain America.
# 
# 
# `1990s: Cold War`
# 
# The intensity around the world during the Cold War has also inspired the emergence of numerous powerful and heroic characters including one of the most famous superheroes in the history -- Superman.
# 
# 
# `2005-2010: New Era - Superhero Movies`
# 
# With the success of DC's Batman movies in the 2000s and Marvel's numerous movies since Iron Man in 2008, people's passions towards superheroes started rising again. Therefore, the number of newly created characters in both DC and Marvel peaked for the third time.

# ## DC vs Marvel: Characters with Most Appearances

# In[7]:


dc_sort = dc.nlargest(5,'APPEARANCES')
marvel_sort = marvel.nlargest(5,'APPEARANCES')
dc_sort.name = dc_sort.name.str.replace('\(.*\)','')
marvel_sort.name = marvel_sort.name.str.replace('\(.*\)','')
trace1 = go.Bar(
    x = dc_sort.APPEARANCES,
    y = dc_sort.name,
    name = 'DC Characters',
    marker = dict(
        color = 'rgb(49,130,189)',
    ),
    orientation = 'h',
)
trace2 = go.Bar(
    x = marvel_sort.APPEARANCES,
    y = marvel_sort.name,
    name = 'Marvel Characters',
    marker = dict(
        color = 'rgb(250,128,114)',
    ),
    orientation = 'h',
)

data = [trace1,trace2]
layout = go.Layout(
    xaxis=dict(title = 'Appearances'),
    yaxis=dict(autorange = 'reversed',
              tickangle = -40),
    title='Character with Most Appearances',
    barmode='group',
)

fig = go.Figure(data=data,layout=layout)
iplot(fig,filename='horizontal-bar', image='jpeg')


# **DC Characters**
# 
# The top 5 characters with the most appearances in DC are Batman, Superman, Green Latern, James Gordon, and Richard Grayson. One thing that's particularly interesting is that both James Gordon and Richard Grayson have their origin stories started in Batman's stroyline and they perform as a supporting character for Batman a lot of times.
# 
# **Marvel Characters**
# 
# Marvel's top 5 characters with the most appearances, however, are all superheroes with their own independent storylines and have had huge success after they got filmized, including Spiderman, Captain America, Wolverine, Iron Man, and Thor.

# ## Character Appearances with respect to Origin Year

# In[8]:


trace0 = go.Bar(
    x= dc.YEAR,
    y= dc.APPEARANCES,
    name='DC Characters',
    text= dc.name,
    marker=dict(
        color='rgb(49,130,189)'
    )
)
trace1 = go.Bar(
    x= marvel.Year,
    y= marvel.APPEARANCES,
    name='Marvel Characters',
    text= marvel.name,
    marker=dict(
        color='rgb(204,204,204)',
    )
)

data = [trace0, trace1]
layout = go.Layout(
    xaxis=dict(tickangle=-45,
              title='Year'),
    yaxis=dict(title='Appearances'),
    title='Appearances with respect to Origin year Bar Plot',
    barmode='group',
)

fig = go.Figure(data=data, layout=layout)
iplot(fig, filename='angled-text-bar', image='jpeg')


# It can be concluded from the bar chart above that DC's many popular characters were created during 1940s (World War II) and 1990s (Cold War) as we have implied before. However, Marvel's most popular characters were created during 1960-1970, which can be regarded as **The Rise of Marvel**.
# 
# On the one hand, it was in 1961 that the brand was officially renamed as Marvel Comics with the launch of the popular superhero group -- *The Fantastic Four*.
# On the other hand, Stan Lee revolutionized Marvel by changing its target audiences from children to older readers. As a result, many popular characters were created since 1960 including **Spiderman**, **Iron Man**, and **Wolverine**.

# In[ ]:




