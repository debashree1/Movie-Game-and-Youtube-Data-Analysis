# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 11:16:08 2018

@author: Debashree_Debalaxmi
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_excel("C:\\Users\\acer\\Desktop\\movies_data.xlsx")
print(df)
print(df.shape)         #to know the dimension
print(df.head(4))       #displaying first 4rows
print(df[3:7])          #displaying rows from index 3 to 6
print(df.tail(5))       #displaying first 5rows
plt.plot(df[1])

df=pd.read_excel("C:\\Users\\acer\\Desktop\\movies_data.xlsx",na_values=["not a value"])   #displaying missing values as "not a value"
print(df)  
print(df.fillna(method='pad'))            #forward fill method



df=pd.read_excel("C:\\Users\\acer\\Desktop\\movies_data.xlsx",header=None,names=["id","movies name","release year","rating","downloads"])   #inserting new header
print(df['downloads'].isnull())         #checking if the values for 'downloads' are null 
grouped=df.groupby('release year')      #grouping by 'release year'
print(grouped.size())                   #to get the no of released films in each year of the group
print(grouped.get_group(1935))          #to display details of all the films released in the year 1935
print(grouped.get_group(1985)['movies name'])   #to display only the movies names released in the year 1985 

plt.plot(df["rating"])

print(df[0:5]['movies name'])       #to display first 5 movies name

print(df.loc[:,['movies name','rating']])   #to display only values of only 'movies name' and 'rating'
print(df.loc[:,['movies name','rating']][1:10])     #to display only values of only 'movies name' and 'rating' from id 1 to 10
print(df['movies name'])        
print(df['rating'].max())       # get the maximum value of the column 'rating'
print(df['rating'].min())       # get the minimum value of the column 'rating'

print(grouped.get_group(1994)['rating'])    #ratings in 1994
print(df.loc[df['rating'].idxmax()])     #to get the maximum rating row
print(df.loc[df['rating'].idxmax()]['release year'])    #finding the year of maximum rating
j = [i for i in df['rating'] if i >= 4.5]
print(j)
