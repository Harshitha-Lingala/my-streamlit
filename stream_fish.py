import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('Fish.csv')

avg_weight_by_species=df.groupby('Species')['Weight'].mean().reset_index()

plt.bar(avg_weight_by_species['Species'],avg_weight_by_species['Weight'],color='green',edgecolor='red')
plt.title('Average Weight of Species')
plt.xlabel('Species')
plt.ylabel('Avg Weight')
st.pyplot(plt)
                                    
