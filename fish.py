import streamlit as st
import pandas as pd
import plotly.express as px

df=pd.read_csv('Fish.csv')
fig = px.bar(df,x="Species",y="Weight")
st.plotly_chart(fig)
