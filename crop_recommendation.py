import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_model():
    """Loads the crop recommendation model and scaler."""
    clf_model = joblib.load('models/classification_model.pkl')
    scaler_clf = joblib.load('models/scaler_clf.pkl')
    return clf_model, scaler_clf

def recommend_crop(user_input, model, scaler, chunk_size=100):
    """Preprocesses user input and recommends a crop."""

    if len(user_input) > chunk_size:
        # Split user input into chunks
        chunks = [user_input[i:i + chunk_size] for i in range(0, len(user_input), chunk_size)]

        # Scale each chunk separately
        scaled_chunks = [scaler.transform(chunk) for chunk in chunks]

        # Concatenate the scaled chunks
        user_input_scaled = pd.concat(scaled_chunks)
    else:
        # Scale the entire user input if it's smaller than the chunk size
        user_input_scaled = scaler.transform(user_input)

    # Predict the recommended crop
    prediction = model.predict(user_input_scaled)
    return prediction