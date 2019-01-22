# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 20:23:22 2018

@author: Debashree_Debalaxmi
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("C:\\Users\\acer\\Desktop\\youtube.xlsx")
print(df)
#to find out top 5 categories with max no of videos uploaded
pp = df.groupby('category').size().sort_values(ascending=False)[:5]
print(pp)
plt.plot(df["category"])
plt.title("Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
