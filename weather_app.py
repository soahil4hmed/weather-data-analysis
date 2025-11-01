# WEATHER DATA ANALYSIS AND VISUALIZATION USING PYTHON
# FRONTEND APP USING STREAMLIT
# Name: Sohail Ahmed | Roll No: 51724862117 | Course: MCA

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page Title
st.title("🌦️ Weather Data Analysis and Visualization")
st.write("### Mini Project by Sohail Ahmed (MCA)")
st.write("This simple app analyzes and visualizes weather data such as temperature, humidity, wind speed, and rainfall using Python.")

# Create Sample Weather Data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Temperature (°C)': [20, 22, 25, 30, 33, 35, 34, 33, 30, 28, 25, 22],
    'Humidity (%)': [60, 58, 55, 50, 45, 40, 42, 45, 50, 55, 58, 60],
    'Wind Speed (km/h)': [12, 14, 13, 11, 9, 8, 10, 12, 13, 14, 13, 12],
    'Rainfall (mm)': [50, 40, 30, 20, 10, 5, 80, 120, 100, 70, 60, 55]
}

df = pd.DataFrame(data)

# Display Data
st.subheader("📋 Weather Dataset")
st.dataframe(df)

# Line Chart - Temperature and Rainfall
st.subheader("🌡️ Temperature and Rainfall Over Months")
fig1, ax1 = plt.subplots()
ax1.plot(df['Month'], df['Temperature (°C)'], marker='o', color='red', label='Temperature (°C)')
ax1.plot(df['Month'], df['Rainfall (mm)'], marker='o', color='blue', label='Rainfall (mm)')
ax1.set_xlabel("Month")
ax1.set_ylabel("Values")
ax1.legend()
st.pyplot(fig1)

# Bar Chart - Humidity and Wind Speed
st.subheader("💨 Humidity and Wind Speed per Month")
fig2, ax2 = plt.subplots()
sns.barplot(x='Month', y='Humidity (%)', data=df, color='skyblue', label='Humidity', ax=ax2)
sns.barplot(x='Month', y='Wind Speed (km/h)', data=df, color='orange', label='Wind Speed', ax=ax2)
ax2.legend()
st.pyplot(fig2)

# Heatmap - Correlation
st.subheader("🔥 Correlation Between Weather Factors")
fig3, ax3 = plt.subplots()
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax3)
st.pyplot(fig3)

# Summary
st.subheader("📈 Summary Insights")
st.write(f"**Highest Temperature:** {df['Temperature (°C)'].max()} °C in {df.loc[df['Temperature (°C)'].idxmax(), 'Month']}")
st.write(f"**Highest Rainfall:** {df['Rainfall (mm)'].max()} mm in {df.loc[df['Rainfall (mm)'].idxmax(), 'Month']}")
st.write(f"**Average Humidity:** {df['Humidity (%)'].mean():.1f}%")
st.write(f"**Lowest Wind Speed:** {df['Wind Speed (km/h)'].min()} km/h")

st.success("✅ Analysis complete! You can use this app to present your Mini Project interactively.")
