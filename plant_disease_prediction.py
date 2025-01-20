from PIL import Image
import tensorflow as tf
import matplotlib.pyplot as plt

class_labels = [
 'Apple___Apple_scab',
 'Apple___Black_rot',
 'Apple___Cedar_apple_rust',
 'Apple___healthy',
 'Blueberry___healthy',
 'Cherry_(including_sour)___Powdery_mildew',
 'Cherry_(including_sour)___healthy',
 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
 'Corn_(maize)___Common_rust_',
 'Corn_(maize)___Northern_Leaf_Blight',
 'Corn_(maize)___healthy',
 'Grape___Black_rot',
 'Grape___Esca_(Black_Measles)',
 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
 'Grape___healthy',
 'Orange___Haunglongbing_(Citrus_greening)',
 'Peach___Bacterial_spot',
 'Peach___healthy',
 'Pepper,_bell___Bacterial_spot',
 'Pepper,_bell___healthy',
 'Potato___Early_blight',
 'Potato___Late_blight',
 'Potato___healthy',
 'Raspberry___healthy',
 'Soybean___healthy',
 'Squash___Powdery_mildew',
 'Strawberry___Leaf_scorch',
 'Strawberry___healthy',
 'Tomato___Bacterial_spot',
 'Tomato___Early_blight',
 'Tomato___Late_blight',
 'Tomato___Leaf_Mold',
 'Tomato___Septoria_leaf_spot',
 'Tomato___Spider_mites Two-spotted_spider_mite',
 'Tomato___Target_Spot',
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
 'Tomato___Tomato_mosaic_virus',
 'Tomato___healthy',
]
def load_model():
    """Loads the plant disease prediction model."""
    model = tf.keras.models.load_model('plant_disease_efficientNetV2_modified1.h5')
    return model

def predict_disease(image_directory, model):
    """Preprocesses the image and predicts the disease."""

    # Preprocess the image using the same data augmentation as training
    # image = tf.convert_to_tensor(image)

    image_data = tf.keras.preprocessing.image_dataset_from_directory(
        image_directory,
        batch_size=1,
        image_size=(224,224),
        labels=None,
        shuffle=False,
    )

    image = next(iter(image_data))

    # Make prediction using the model
    prediction = model.predict(image)
    predicted_index = tf.argmax(prediction[0])  # Get the index of the most likely class

    # Access the class name using the predicted index
    predicted_class = class_labels[predicted_index]  # Convert index to class name
    # return predicted_class
    # return prediction
    return predicted_class