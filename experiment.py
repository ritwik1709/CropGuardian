from plant_disease_prediction import load_model, predict_disease
from glob import glob
from PIL import Image

model = load_model()
print("loaded model")
# Hash: ac68975229467b238b3ec3cc02fe8d1cf0f2a7eb7210db18cbaba2494b9c81cf

for filename in glob("C:\\Users\\Shouvik Dey\\Downloads\\Test_images\\Gra*"):
    image = Image.open(filename)
    prediction = predict_disease(image, model)
    print(prediction)