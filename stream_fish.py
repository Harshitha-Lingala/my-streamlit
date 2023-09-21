import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('Fish.csv')
avg_height_by_species=df.groupby('Species')['Height'].mean().reset_index()
plt.bar(avg_height_by_species['Species'],avg_height_by_species['Height'])
st.pyplot(plt)
                                