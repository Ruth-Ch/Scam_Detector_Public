import streamlit as st
import joblib
import numpy as np

# Load trained components
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# App UI
st.title(" Scam Message Classifier")
st.write("Classify messages into ham, smishing, or spam.")

# User input
user_input = st.text_area("✉ Enter a message:")

# Optional binary features (used during training)
url = st.checkbox("Contains a URL?")
phone = st.checkbox("Mentions a phone number?")

# Predict button
if st.button("Detect"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        # Preprocess input
        vectorized_text = vectorizer.transform([user_input])
        extra_features = np.array([[int(url), int(phone)]])
        combined = np.hstack((vectorized_text.toarray(), extra_features))

        # Make prediction
        prediction = model.predict(combined)
        label = label_encoder.inverse_transform(prediction)[0]

        st.success(f" This message is classified as: **{label.upper()}**")
