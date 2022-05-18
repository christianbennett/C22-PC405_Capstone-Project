from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow import keras
import tensorflow as tf
import io
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Import model
model = keras.models.load_model("model.h5")

# Convert image to array


def transform_image(img):

    imgs = []
    img = img.resize((150, 150))
    img = img_to_array(img)
    img = img.astype(np.float32) / 255
    imgs.append(img)
    imgs = tf.image.resize(img, [150, 150])
    imgs = np.expand_dims(imgs, axis=0)

    return imgs

# Prediction function


def predict(x):

    predictions = model(x)
    pred = np.argmax(predictions, axis=1)
    return pred


# Initialize Flask server with error handling
app = Flask(__name__)

# Label names
label = ['Aluminium', 'Carton', 'Glass', 'Organic Waste',
         'Other Plastics', 'Paper and Cardboard', 'Plastic', 'Textiles', 'Wood']


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({"error": "no file"})

        try:
            image_bytes = file.read()
            pillow_img = Image.open(io.BytesIO(image_bytes))
            prediction = predict(transform_image(pillow_img))
            data = {"prediction": int(prediction), "label": label[int(prediction)]
                    }
            return jsonify(data)
        except Exception as e:
            return jsonify({"error": str(e)})

    return "OK"


if __name__ == "__main__":
    app.run(debug=True)
