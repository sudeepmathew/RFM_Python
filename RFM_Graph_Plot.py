
# coding: utf-8

# Assignment on RFM Data Set
# Analyzing Data with Graphs on RFM

# In[1]:

#Import all libraries
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')


# In[5]:

# Reading RFM data set
df = pd.read_csv("E:\Studies\RFM Analysis\RFMClass.csv")


# In[50]:

# to display first 10 rows from tha data fram
df.head(10)


# In[7]:

#to display last 10 rows from the data frame
df.tail(10)


# In[8]:

#to dispaly sample items from the data frame
df.sample(10)


# In[10]:

# to dispaly the types of data frame
df.dtypes


# In[11]:

# to describe the data in the data frame
df.describe()


# In[12]:

#Plot hist
df['recency'].plot.hist(by = 'class')

Customers with less than 50 recency

# Above Hisogram shows that 1750 customers have less than 50 recency which means 40 % of customers have more recency and we need to find out whether these customers have high frequnecy and monetary to determine the value of the customers

Customers with less than 100 recency

Around 300 customers have recency less than 100 and we need to find out frequency and monetary for upselling the product

Customers with recency greater than 200

Around 200 customers has recency greater than 200 we need to find out the customers and retain them.
# We need to find out the  classification for the recency using an histogram and dencity
# 
# Dencity is calculated by frequency divided by class width

# In[15]:

# Finding classification using dencity for recency
df['recency'].plot.density()


# After checking dencity it is look like to be a normal distribution

# In[17]:

#histogram and distribution plotting
sns.distplot(df['recency'])


# In above diagram we can classify the distribution is looks like normal distribution

# Analysing frequency in RFM data set
# We have to analyze the frequency of customer visits to understand the high value customer. 
# The customer with high frequency will be high value customer

# Frequency histogram in a clss

# In[19]:

df['frequency'].plot.hist(by = 'class')


# By seeing histogram we can understand that more than 4000 customers have a frequncy less than 1000 and very few customers have frequency of more than 1000 and they will be the most visited customer and by analzing recency and frequncy and monetary we can classify them as the high value customers.

# In[21]:

# binning the distibution into quintiles and coloured as green
df['frequency'].hist(bins=5, color = 'green')

To understand and classify we will plot frequency in dencity distribution
# In[22]:

df['frequency'].plot.density(color = 'red')


# By seeing the diagram we can undersatnd that frequency is a normal distribution

# We can identify ouliers by plotting a boxplot
# 

# In[25]:

df.boxplot('recency')


# In[26]:

# Box Plot for frequency
df.boxplot('frequency')


# In[27]:

df.boxplot(column = 'recency', by = 'frequency')


# Monetary Analyzis 

# In[28]:

#Monetary Histogram
df['monetary'].plot.hist(by = 'class')


# By Analyzing monetary histogram we can identify that there are around 4000 customers are spending less than 25000
# and very few customers are spending more than 25000.
# 
# We need to identify the customers who are spending more and classify them as the heigh value customers

# We can analyze the classification by ploting density 

# In[30]:

df['monetary'].plot.density(color = 'green')


# By Understanding the density distribution we can classify this as a normal distribution

# In[34]:

df.boxplot(column = 'recency', by = 'monetary')


# Above box plot tells about moneatry and recency and monetary is in X axix and recency in Y axis

# In[35]:

sns.stripplot(x="monetary", y="frequency", jitter = True, data=df)


# In[38]:

mapping = {'Yes' :1, 'No' :2}
df.replace({'Yes': 1, 'No': 0})


# In[39]:

sns.stripplot(x="label", y="monetary", jitter = True, data=df)


# In[40]:

df.boxplot(column = 'recency', by = 'label')


# In[41]:

df.groupby('label').size().plot.bar(alpha = 0.4)


# 

# In[42]:

df.groupby("label").recency.hist()


# In[44]:

df.groupby("label").frequency.hist()


# In[45]:

df.groupby("label").monetary.hist()


# In[52]:

sns.lmplot('recency', # Horizontal axis
           'monetary', # Vertical axis
           data=df, # Data source
          )
# Below diagram shows us that there are high monetary value customers are present where recency is less than 50.
#We have to identify these customers and who are most recent annd have high monetary value for upselling and cross selling


# In[51]:

sns.lmplot('frequency', # Horizontal axis
           'monetary', # Vertical axis
           data=df, # Data source
          )
# By seeing below diagram we can see that customers have less than 1000 frequency are more and few have monetary greater than 100000
#There few customers have more than 2000 frequency and greater than 50000.


# In[53]:

sns.lmplot('recency', # Horizontal axis
           'monetary', # Vertical axis
           data=df, # Data source
           fit_reg=False, # Don't fix a regression line
           hue="label", # Set color
          )


# In[49]:

sns.pairplot(df)

