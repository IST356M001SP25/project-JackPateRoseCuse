import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

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
team_stats_df = pd.merge(merged_df, pitching_table, on='Tm', how='inner')
# print(merged_df)  # Display the first few rows of the merged DataFrame

team_stats_df.to_csv('team_stats_2025.csv', index=False)
# Create a CSV file in the current directory

st.title("MLB Team Statistics 2025")

# Load the dataset to the repository, so that you can use it with other codes if you wanted to later
team_stats_df = pd.read_csv('team_stats_2025.csv')

# Streamlit app
st.title("MLB Team Statistics 2025")

# Dropdowns for selecting columns to compare
columns = team_stats_df.columns.tolist()
x_axis = st.selectbox("Select X-axis column:", columns)
y_axis = st.selectbox("Select Y-axis column:", columns)

# Creating a scatterplot that allows the user to select the x-axis and y-axis columns, along with finding their correlation
if x_axis and y_axis:
    st.write(f"Scatterplot: {x_axis} vs {y_axis}")
    plt.figure(figsize=(10, 6))
    scatter_plot = sns.scatterplot(
        data=team_stats_df,
        x=x_axis,
        y=y_axis,
        hue='Tm',  # Color by team
        palette='Set1',  # Use a color palette
    )
    plt.legend(title='Team', bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot(plt)

print(columns) # print all the columns in the dataset



# Display the correlation between the selected column and win%
st.title("Correlation to Win%")
columns_2 = columns # Creating a new ID for the columns list to avoid confusion with the previous one

# Dropdown for selecting the x-axis column 
x_axis2 = st.selectbox("Select X-axis column:", columns_2, index=1)  # Default to the second column

#Creating the scatterplot that allows the user to select the x-axis column, along with finding their correlation to win%
if x_axis2:
    st.write(f"Correlation: {x_axis2} vs W%") # Title of the graph
    plt.figure(figsize=(10, 6)) # Size of the graph
    correlation_plot = sns.scatterplot(
        data=team_stats_df, # DataFrame containing the team statistics
        x=x_axis2, # X axis column selected by the user
        y='W-L%',  # Correlate with Win%
        hue='Tm',  # Color by team
        palette='Set1',  # Use a color palette
    )
    plt.legend(title='Team', bbox_to_anchor=(1.05, 1), loc='upper left') # Display the legend in the upper left corner
    st.pyplot(plt) # Plot the graph 
