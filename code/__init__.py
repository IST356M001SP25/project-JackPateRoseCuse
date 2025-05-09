import pandas as pd
import streamlit as st
import seaborn as sns 

# URL of the dataset
hitting_url = "https://www.baseball-reference.com/leagues/majors/2025.shtml"
fielding_url = "https://www.baseball-reference.com/leagues/majors/2025-standard-fielding.shtml"
pitching_url = "https://www.baseball-reference.com/leagues/majors/2025-standard-pitching.shtml"


# Read all tables from the webpage
hitting_table = pd.read_html(hitting_url) 
hitting_table = hitting_table[0][0:31]  # The first table is the one we want
# print(hitting_table)  # Display the first few rows of the first table 

fielding_table = pd.read_html(fielding_url)
fielding_table = fielding_table[0][0:31]  # The first table is the one we want
# print(fielding_table)  # Display the first few rows of the first table

pitching_table = pd.read_html(pitching_url)
pitching_table = pitching_table[0][0:31]  # The first table is the one we want
# print(pitching_table)  # Display the first few rows of the first table

merged_df = pd.merge(hitting_table, fielding_table, on='Tm', how='inner')
merged_df = pd.merge(merged_df, pitching_table, on='Tm', how='inner')
# print(merged_df)  # Display the first few rows of the merged DataFrame

merged_df.to_csv('team_stats_2025.csv', index=False)
# Create a CSV file in the current directory

st.title("MLB Team Statistics 2025")
