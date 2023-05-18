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

#Iterate over the DataFrame, where the 'Name' column is date define 'date' variable and append this variable into a new 'Date' column
for index, row in df.iterrows():
    if type(row['Name']) == pd._libs.tslibs.timestamps.Timestamp:
        date = row['Name']
        df.at[index,'type'] = 'date'
    df.at[index,'Date'] = date

#Add new column with the day of the race
#df['Day'] = df['Date'].dt.day_name()

#Remove dates from rows
#df = df[df.type] != 'date'


st.dataframe(df)
