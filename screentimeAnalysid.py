import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("/Users/kavitasingh/Documents/Projects/GEN AI/numpy/Screentime-App-Details-Dataset.csv")
# print(df.head())/
# print(df.isnull().sum())
# figure= px.bar(data_frame=df,x="Date",y="Usage",color="App",title="Usage Graph")
# figure= px.bar(data_frame=df,x="Date",y="Notifications",color="App",title="Notification Graph")
# figure= px.bar(data_frame=df,x="Date",y="Times opened",color="App",title="Times opened Graph")
figure = px.scatter(data_frame=df,x="Notifications",y="Usage",size="Notifications",
                    trendline="ols",
                    title="relationship between notification and amount of usage")
figure.show()