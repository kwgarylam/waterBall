import streamlit as st
import pandas as pd

# Sample data with two locations
data = pd.DataFrame({
    'city': ['San Francisco', 'Los Angeles'],
    'lat': [37.7749, 34.0522],
    'lon': [-122.4194, -118.2437]
})

# Title of the app
st.title('Map of Selected City')

# Selection box to choose a city
city = st.selectbox('Choose a city', data['city'])

# Filter data based on selection
selected_data = data[data['city'] == city]

# Display the selected city
st.write(f'Selected city: {city}')
st.dataframe(selected_data)

# Display the map with the selected location
st.map(selected_data)
