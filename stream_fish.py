import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('Fish.csv')
avg_weight_by_species=df.groupby('Species')['Weight'].mean().reset_index().sort_values(by='Weight',ascending=True)
avg_height_by_species=df.groupby('Species')['Height'].mean().reset_index().sort_values(by='Height',ascending=True)


st.write(avg_weight_by_species)

st.write(avg_height_by_species)

plt.subplot(1,2,1)
plt.bar(avg_height_by_species['Species'],avg_height_by_species['Height'])
plt.title('Average Height of Species')
plt.xlabel('Species')
plt.ylabel('Avg Height')
plt.xticks(rotation=45)

plt.subplot(1,2,2)
plt.bar(avg_weight_by_species['Species'],avg_weight_by_species['Weight'])
plt.title('Average Weight of Species')
plt.xlabel('Species')
plt.ylabel('Avg Weight')
plt.xticks(rotation=45)

plt.tight_layout()

st.pyplot(plt)
                                
