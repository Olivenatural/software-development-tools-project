import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
data = pd.read_csv('WHR2024.csv')

# A header for Streamlit app
st.header("World Happiness Report Data Visualizations")

# A checkbox to toggle between the histogram and scatterplot
show_histogram = st.checkbox("Show Histogram")
show_scatter = st.checkbox("Show Scatter Plot")

# A dropdown to select a column for the x-axis
x_axis = st.selectbox("Select a column for X-axis", data.columns)

# Define behavior change for the checkbox: for example, filtering out countries with low GDP
exclude_low_gdp = st.checkbox("Exclude countries with low GDP per capita")

if exclude_low_gdp:
    data = data[data["Explained by: Log GDP per capita"] > 1.0] # Filter out countries with GDP < 1

# Show the histogram if the checkbox is checked
if show_histogram:
    fig = px.histogram(data, x=x_axis, title=f"Histogram of {x_axis}")
    st.plotly_chart(fig)

# Show the scatter plot if the checkbox  is checked
if show_scatter:
    fig_scatter = px.scatter(data, x=x_axis, y='Ladder score', title=f"Scatter Plot: {x_axis} vs Ladder Score")
    st.plotly_chart(fig_scatter)    

