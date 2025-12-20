import pandas as pd
import streamlit as st

st.header("Displaying dataframes")

data = pd.DataFrame({ 
    'Names': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Ages': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
})

st.dataframe(data)