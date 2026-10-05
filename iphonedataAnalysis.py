import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


df = pd.read_csv("/Users/kavitasingh/Documents/Projects/GEN AI/numpy/apple_products.csv")
# check cols 
# print(df.head())
# test null value 
# print(df.isnull().sum())
# check description 
# print(df.describe())

highest_rated = df.sort_values(by=["Star Rating"],ascending=False)
highest_rated= highest_rated.head(10)
# print(highest_rated['Product Name'])
"""
iphone = highest_rated['Product Name'].value_counts()
label = iphone.index
count = highest_rated["Number Of Ratings"]
figure = px.bar(highest_rated,x= label,y= count,title="Number of ratings of highest rated iphone")

figure.show()

iphone = highest_rated['Product Name'].value_counts()
label = iphone.index
count = highest_rated["Number Of Reviews"]
figure = px.bar(highest_rated,x= label,y= count,title="Number of Reviews of highest rated iphone")

figure.show()


figure = px.scatter(data_frame=df,x="Number Of Ratings",y="Sale Price",size="Discount Percentage",trendline='ols',title="Relationship between sale price and number of ratings of iphone")

figure.show()
"""
figure = px.scatter(data_frame=df,x="Number Of Ratings",y="Discount Percentage",size="Sale Price",trendline='ols',title="Relationship between discount percentage and number of ratings of iphone")

figure.show()