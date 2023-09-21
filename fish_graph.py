import streamlit as st
import pandas as pd

df=pd.read_csv('Fish.csv')
st.bar_chart(height=df['Species'],x=df['Weight'],width=0.5)
