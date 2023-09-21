import streamlit as st 
import plotly.express as px
import pandas as pd

df=pd.read_csv('Fish.csv')
fig=px.bar(df,x='Species',y='Weight')
st.plotly_chart(fig)
