import streamlit as st
import pandas as pd

df=pd.read_csv('Fish.csv')
st.bar_chart(x=df['Species'],height=df['Weight'],width=0.5)
