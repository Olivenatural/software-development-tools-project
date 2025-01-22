# Data Loading Section
import pandas as pd
import plotly.express as px
import streamlit as st

data = pd.read_csv('WHR2024.csv')

# Data Cleaning Section
df.isnull().sum()

# Filling missing values with the mean for the selected columns
df['Explained by: Log GDP per capita'] = df['Explained by: Log GDP per capita'].fillna(df['Explained by: Log GDP per capita'].mean())
df['Explained by: Social support'] = df['Explained by: Social support'].fillna(df['Explained by: Social support'].mean())
df['Explained by: Healthy life expectancy'] = df['Explained by: Healthy life expectancy'].fillna(df['Explained by: Healthy life expectancy'].mean())
df['Explained by: Freedom to make life choices'] = df['Explained by: Freedom to make life choices'].fillna(df['Explained by: Freedom to make life choices'].mean())
df['Explained by: Generosity'] = df['Explained by: Generosity'].fillna(df['Explained by: Generosity'].mean())
df['Explained by: Perceptions of corruption'] = df['Explained by: Perceptions of corruption'].fillna(df['Explained by: Perceptions of corruption'].mean())
df['Dystopia + residual'] = df['Dystopia + residual'].fillna(df['Dystopia + residual'].mean())


# Visualization Section

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

# Add a slider to control the number of bins for the histogram
bins = st.slider("Select number of bins", min_value=5, max_value=50, value=20)

# Create the histogram with the selected number of bins
fig = px.histogram(df, 
                   x="Ladder score", 
                   title="Distribution of Happiness Scores", 
                   labels={"Ladder score": "Happiness Score (Ladder Score)"}, 
                   nbins=bins)

# Show the plot in Streamlit
st.plotly_chart(fig)
