import streamlit as st
from datetime import datetime
from datetime import time
import requests

'''
# Taxi NY
'''

ride_date= st.date_input("Select the date of the ride", datetime.today())
#create a liste of time
times = [time(hour, minute) for hour in range(0, 24) for minute in range(0, 60)]



#create a selectbox taking the time
ride_time = st.selectbox(
    "Select the time of the ride",
    times,
    format_func=lambda t: t.strftime("%H:%M")
)
date_time = datetime.combine(ride_date, ride_time)

st.write("The selected date and time is :", date_time.strftime("%Y-%m-%d %H:%M"))

# Pickup location inputs
pickup_longitude = st.number_input("Enter the pickup longitude")
pickup_latitude = st.number_input("Enter the pickup latitude")

# Dropoff location inputs
dropoff_longitude = st.number_input("Enter the dropoff longitude")
dropoff_latitude = st.number_input("Enter the dropoff latitude")

# Passenger count input
passenger_count = st.number_input("Enter the passenger count", min_value=1, max_value=10, step=1)


# #dictionnary to use for the prediction

params ={"pickup_datetime":date_time.strftime("%Y-%m-%d %H:%M"),
    "pickup_longitude": float(pickup_longitude),
    "pickup_latitude":float(pickup_latitude),
    "dropoff_longitude": float(dropoff_longitude),
    "dropoff_latitude":float(dropoff_latitude) ,
    "passenger_count": int(passenger_count)}

#prediction

if st.button("Predict Fare"):
        # API URL (replace with your own if needed)
        url = 'https://taxifare.lewagon.ai/predict'
        response = requests.get(url, params=params)
        if response.status_code == 200:
            prediction = response.json().get("fare", "Error: Could not retrieve prediction")

            st.success(f"The predicted fare is ${prediction:.2f}")
        else:
            st.error("Error: Unable to get a response from the API")
else:
    st.warning("Please provide both pickup and dropoff locations.")
