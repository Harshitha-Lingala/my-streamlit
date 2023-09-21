import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('Fish.csv')
plt.hist(df['Species'])
st.pyplot(plt)
