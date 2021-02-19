import pandas as pd 
import plotly.express as px

df=pd.read_csv("corona data.csv")
print(df[:5])

chart=px.scatter(df,x="date",y="cases",title="Record of Covid cases", color="country", size_max=60)
chart.show()
