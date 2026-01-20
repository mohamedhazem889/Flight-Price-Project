import streamlit as st
import pandas as pd
import joblib
from streamlit_lottie import st_lottie
import json
import time

# Define the city short name mapping For Source
source_city_shortname_mapping = {
    "Delhi": "DEL",
    "Mumbai": "BOM",
    "Bangalore": "BLR",
    "Kolkata": "CCU",
    "Chennai": "MAA"
}

# Define the city short name mapping For Destination
dest_city_shortname_mapping = {
    "Delhi": "DEL",
    "New Delhi": "DEL",
    "Bangalore": "BLR",
    "Kolkata": "CCU",
    "Hyderabad": "HYD",
    "Cochin": "COK"
}

# Load your trained model and inputs
Model = joblib.load("Flight_Price_Model.pkl")
Inputs = joblib.load("inputs.pkl")

# Load Lottie animations
def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

welcome_animation = load_lottie_file("Start.json")
flight_animation = load_lottie_file("Predict.json")

# Function to map city name to its short name (Source)
def map_source_city_to_shortname(city_name):
    return source_city_shortname_mapping.get(city_name, "Unknown")

# Function to map city name to its short name (Destination)
def map_dest_city_to_shortname(city_name):
    return dest_city_shortname_mapping.get(city_name, "Unknown")

# Prediction function
def Prediction(Airline, Date_of_Journey, Source, Destination, dep_hour, dep_minute, Arrival_hour, Arrival_minute, Total_Stops, Duration_Minutes):
    df = pd.DataFrame(columns=Inputs)
    df.at[0, "Airline"] = Airline
    df.at[0, "Date_of_Journey"] = Date_of_Journey
    df.at[0, "Source"] = map_source_city_to_shortname(Source)  # Convert to short name
    df.at[0, "Destination"] = map_dest_city_to_shortname(Destination)  # Convert to short name
    df.at[0, "dep_hour"] = dep_hour
    df.at[0, "dep_minute"] = dep_minute
    df.at[0, "Arrival_hour"] = Arrival_hour
    df.at[0, "Arrival_minute"] = Arrival_minute
    df.at[0, "Total_Stops"] = Total_Stops
    df.at[0, "Duration_Minutes"] = Duration_Minutes
    result = Model.predict(df)
    return result[0]

# Main Streamlit app with advanced UI features
def Main():
    # Custom CSS for enhanced styling
    st.markdown(
    """
    <style>
    body, .stApp {
        background: rgb(5, 50, 90) !important;
        color: rgb(5, 50, 90) !important;
        font-family: 'Arial', sans-serif;
        height: 100vh;
        margin: 0;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* Title color */
    .title {
        font-size: 3.5em;
        color: #faf0e6 !important;  /* Off-white color */
        text-align: center;
        font-weight: bold;
        margin-bottom: 0.5em;
        text-shadow: 4px 4px 10px rgba(0, 0, 0, 0.8);
    }

    /* Subheader color */
    .custom-subheader {
        font-size: 1.8em;
        color: #faf0e6 !important;  /* Off-white color */
        text-align: left;
        margin-bottom: 2em;
        font-weight: 400;
    }
    .subtitle {
        font-size: 1.8em;
        color: #faf0e6;
        text-align: center;
        margin-bottom: 2em;
        font-weight: 400;
        }
    .stButton > button {
        background: rgb(5, 50, 90) !important;
        color: rgb(5, 50, 90) !important;
        font-size: 1.4em !important;
        padding: 12px 25px !important;
        border-radius: 20px !important;
        border: none;
        }
    .stButton > button:hover {
        transform: scale(1.1);
        background:  rgb(5, 50, 90);
        }
    .predict-result {
        font-size: 2em;
        background: rgb(5, 50, 90);
        text-align: center;
        font-weight: bold;
        margin-top: 20px;
        border: 2px solid rgb(8, 40, 58);
        border-radius: 12px;
        padding: 12px;
        box-shadow: 0 0 20px #faf0e6;
        color: #faf0e6; /* Changed text color to white */
        }
    .card {
        backdrop-filter: blur(10px);
        background: #faf0e6;
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.3);
        border: 1px solid rgb(5, 50, 90);
        }

    .stForm label, .stSlider label, .stSelectbox label {
    color: #faf0e6 !important; /* Set the title color */
        }

    .stSpinner > div > div {
        color: #faf0e6 !important; 
        font-size: 1.2em; 
    }



    </style>
    """,
    unsafe_allow_html=True
)

    # Sidebar
    st.sidebar.title("Navigation")
    st.sidebar.markdown("### Use the options below:")
    st.sidebar.markdown("1. Select cities.\n2. Enter journey details.\n3. Click Predict.")

    # Welcome animation
    st_lottie(welcome_animation, height=300, key="start_animation")

    # Welcome header
    st.markdown('<h1 class="title">Welcome to Flight Price Predictor ✈️</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Discover the best predictions for flight prices in just a few clicks!</p>', unsafe_allow_html=True)

        # Input form 
    st.markdown('<div class="card">', unsafe_allow_html=True)
    with st.form("flight_form"):
        
        st.markdown('<h3 class="custom-subheader">📋 Fill in your flight details:</h3>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            Source = st.selectbox("Select Source City", list(source_city_shortname_mapping.keys()))
        with col2:
            destination_options = [city for city in dest_city_shortname_mapping.keys() if city != Source]
            Destination = st.selectbox("Select Destination City", destination_options)

        Airline = st.selectbox("✈️ Select Airline", [
            "IndiGo", "Air India", "Jet Airways", "SpiceJet", "Vistara",
            "Multiple carriers", "Air Asia", "GoAir", 
            "Multiple carriers Premium economy", 
            "Jet Airways Business", 
            "Vistara Premium economy", "Trujet"
        ])
        Date_of_Journey = st.date_input("📅 Date of Journey")
        dep_hour = st.slider("🕒 Departure Hour", min_value=0, max_value=23, step=1)
        dep_minute = st.slider("🕒 Departure Minute", min_value=0, max_value=59, step=5)
        Arrival_hour = st.slider("🕒 Arrival Hour", min_value=0, max_value=23, step=1)
        Arrival_minute = st.slider("🕒 Arrival Minute", min_value=0, max_value=59, step=5)
        Total_Stops = st.slider("🛑 Total Stops", min_value=0, max_value=4, step=1)

        # Calculate Duration in minutes
        Duration_Minutes = ((Arrival_hour * 60) + Arrival_minute) - ((dep_hour * 60) + dep_minute)
    
    # Adjust duration if arrival time is before departure (midnight crossing)
        if Duration_Minutes < 0:
            Duration_Minutes += 1440  # Add 24 hours in minutes (1440 minutes)

       # Convert duration to hours and minutes
        hours = Duration_Minutes // 60
        minutes = Duration_Minutes % 60
        duration_display = f"{hours} hours {minutes} minutes"

        submit_button = st.form_submit_button(label="💵 Predict")

        if submit_button:
           with st.spinner("Predicting flight price..."):
            time.sleep(2)  # Simulate processing delay
            st_lottie(flight_animation, height=200, key="predict_animation")
            result = Prediction(Airline, Date_of_Journey, Source, Destination, dep_hour, dep_minute, Arrival_hour, Arrival_minute, Total_Stops, Duration_Minutes)
            formatted_result = f"{result:.2f}"

            # Display predicted price and flight details
            st.markdown(f"<p class='predict-result'>Predicted Flight Price: {formatted_result} ₹</p>", unsafe_allow_html=True)
            st.markdown('<h3 class="custom-subheader">🛫 Flight Details:</h3>', unsafe_allow_html=True)
            st.markdown(f"""
            <div class="card">
                <p><strong>Airline:</strong> {Airline}</p>
                <p><strong>Date of Journey:</strong> {Date_of_Journey}</p>
                <p><strong>Source:</strong> {Source} </p>
                <p><strong>Destination:</strong> {Destination} </p>
                <p><strong>Departure Time:</strong> {dep_hour:02}:{dep_minute:02}</p>
                <p><strong>Arrival Time:</strong> {Arrival_hour:02}:{Arrival_minute:02}</p>
                <p><strong>Total Stops:</strong> {Total_Stops}</p>
                <p><strong>Duration:</strong> {duration_display}</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)

Main()
