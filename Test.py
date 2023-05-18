import streamlit as st
import pandas as pd
from datetime import datetime
import pip
pip.main(["install", "openpyxl"])

#set wide mode
st.set_page_config(layout="wide")

#Page title
st.title("Latton TT Series") 

#Create a df using an excel spreadsheet
df = pd.read_excel("Results Archive 11-5-23.xlsx")
df = df[['Position','Start Number','Name','Club','Split Time','Time']]

st.dataframe(df)
