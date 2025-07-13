import streamlit as st
import requests
import matplotlib.pyplot as plt

st.title("🌦️ Current Weather Dashboard")
city_name = st.text_input("Enter city name", "")

if city_name:
    API_KEY = "9fff63a0978a39e3507d4ab1d2cb333e"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        temp = data['main']['temp']
        humidity = data['main']['humidity']
        weather_desc = data['weather'][0]['description'].title()

        st.subheader(f"📍 City: {city_name}")
        st.write(f"🌡️ **Temperature:** {temp}°C")
        st.write(f"💧 **Humidity:** {humidity}%")
        st.write(f"🌥️ **Condition:** {weather_desc}")

        labels = ['Temperature (°C)', 'Humidity (%)']
        values = [temp, humidity]
        colors = ['orange', 'skyblue']

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(labels, values, color=colors)
        ax.set_title(f"Current Weather in {city_name}")
        ax.set_ylim(0, 100)

        for i, v in enumerate(values):
            ax.text(i, v + 2, str(v), ha='center', fontweight='bold')
        st.pyplot(fig)
        
    else:
        st.error("❌ Failed to fetch data. Please check the city name.")
