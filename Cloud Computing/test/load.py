import io
from PIL import Image
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow import keras
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


model = keras.models.load_model("./model.h5")

# load the image
path = 'test/assets/buckettest.jpg'

with open(path, 'rb') as file:
    image_bytes = file.read()
    pillow_img = Image.open(io.BytesIO(image_bytes)).convert('L')

size = 150

img = load_img(path, target_size=(size, size))
img = img_to_array(img)
img = img.astype(np.float32) / 255.0

data = []
data.append(img)
data = tf.expand_dims(img, axis=0)

predictions = model(data)

pred = np.argmax(predictions, axis=1)
print(pred)
