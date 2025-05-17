import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor

# Title of the App
st.title("🚗 Car Price Prediction App")

# Load dataset (without displaying it)
@st.cache_data
def load_data():
    df = pd.read_csv("car data.csv")

    # Preprocessing
    df['Age'] = 2025 - df['Year']  # Calculate car age
    df.drop(columns=['Car_Name', 'Year'], inplace=True)

    # Encoding categorical variables
    df['Fuel_Type'] = df['Fuel_Type'].map({'Petrol': 0, 'Diesel': 1, 'CNG': 2})
    df['Seller_Type'] = df['Seller_Type'].map({'Dealer': 0, 'Individual': 1})
    df['Transmission'] = df['Transmission'].map({'Manual': 0, 'Automatic': 1})

    return df

df = load_data()

# Splitting data
X = df.drop("Selling_Price", axis=1)
y = df["Selling_Price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
gbr = GradientBoostingRegressor()
gbr.fit(X_train, y_train)

# Sidebar for User Input
st.sidebar.header("Enter Car Details")

present_price = st.sidebar.number_input("Present Price (in lakhs)", min_value=0.0, max_value=50.0, value=5.0)
kms_driven = st.sidebar.number_input("Kilometers Driven", min_value=0, max_value=500000, value=30000)
fuel_type = st.sidebar.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller_type = st.sidebar.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.sidebar.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.sidebar.selectbox("Number of Previous Owners", [0, 1, 2, 3])
age = st.sidebar.number_input("Car Age (in years)", min_value=0, max_value=50, value=5)

# Convert categorical inputs to numerical
fuel_type_map = {"Petrol": 0, "Diesel": 1, "CNG": 2}
seller_type_map = {"Dealer": 0, "Individual": 1}
transmission_map = {"Manual": 0, "Automatic": 1}

# Convert user input to numerical values
user_data = pd.DataFrame([[
    present_price, kms_driven, fuel_type_map[fuel_type], seller_type_map[seller_type], transmission_map[transmission], owner, age
]], columns=['Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner', 'Age'])

# Prediction Button
if st.sidebar.button("Predict Price"):
    prediction = gbr.predict(user_data)
    st.sidebar.success(f"Estimated Selling Price: ₹{prediction[0]:.2f} Lakhs")
