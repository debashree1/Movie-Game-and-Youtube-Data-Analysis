# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 10:40:38 2018

@author: Debashree_Debalaxmi
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("C:\\Users\\acer\\Downloads\\Pokemon.csv")
print(df)                  
print(df.shape)     #to get the dimensions 
print(df.head(2))   #to get the top 2 rows
print(df[4:9])      #to get the rows from index 4 to 8
print(df[36:45])    #to get the rows from index 36 to 44
print(df[101:109])  #to get the rows from index 101 to 108
print(df.columns)   #to get the column names
print(df.Name)      #to get the values of the column "Name"
print(df.HP)        #to get the values of the column "HP"
print(df.head(5))   #to get the top 5 rows
print(df.tail(5))   #to get the last 5 rows
print(df.tail(1))   #to get the last rows
plt.plot(df["Type 1"])
plt.title("Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()


