from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os


app = Flask(__name__)


# Load CNN model
model = load_model(r"C:\Users\HASNA FATHIMA\OneDrive\Desktop\Deepfake_Flask_Project\deepfake_detector .keras")


# Your model validation accuracy
MODEL_ACCURACY = 73.10


@app.route("/")
def home():
    return render_template(
        "index.html",
        accuracy=MODEL_ACCURACY
    )


@app.route("/predict", methods=["POST"])
def predict():

    image = request.files["image"]


    # Save uploaded image
    img_path = "static/uploaded_image.jpg"

    image.save(img_path)


    # Preprocess image
    img = load_img(
        img_path,
        target_size=(224,224)
    )


    img = img_to_array(img)

    img = img / 255.0


    img = np.expand_dims(img, axis=0)



    # Prediction
    prediction = model.predict(img)


    probability = prediction[0][0]


    if probability > 0.5:

        result = "Real Image"

        confidence = probability * 100

    else:

        result = "Fake Image"

        confidence = (1 - probability) * 100



    return render_template(
        "index.html",
        prediction=result,
        confidence=round(confidence,2),
        image_path=img_path,
        accuracy=MODEL_ACCURACY
    )



if __name__ == "__main__":
    app.run(debug=True)