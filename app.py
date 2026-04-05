import streamlit as st
import requests

st.title("AI Smart Pricing System 🚀")

st.write("Enter product details:")

# Inputs
rating = st.slider("Rating", 1.0, 5.0, 4.0)
demand = st.slider("Demand", 0.0, 1.0, 0.5)

category = st.selectbox(
    "Category",
    ["electronics", "home", "books"]
)

# Button
if st.button("Predict Price"):

    data = {
        "rating": rating,
        "demand": demand,
        "category": category
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict-price",
        json=data
    )

    result = response.json()

    st.success(f"Predicted Price: ₹{result['predicted_price']:.2f}")