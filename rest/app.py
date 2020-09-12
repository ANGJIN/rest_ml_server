import os
from flask import Flask, flash, request, redirect, url_for, session, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS
from PIL import Image
import numpy as np
from numpy import asarray
import tensorflow as tf

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

UPLOAD_FOLDER = './'
ALLOWED_EXTENSIONS = set(['png'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)


@app.route('/rest/image', methods=['POST'])
def image_upload():
    app.logger.debug("post!")
    target = os.path.join(UPLOAD_FOLDER, 'uploadedImage')
    if not os.path.isdir(target):
        os.mkdir(target)
    file = request.files['file']
    filename = secure_filename(file.filename)
    destination = "/".join([target, filename])
    file.save(destination)
    session['uploadFilePath'] = destination

    image = Image.open(
        './uploadedImage/{}'.format(file.filename)).convert('RGB')
    data = asarray(image, dtype=np.float32)
    return jsonify({'message': get_predict(data)})


def get_predict(data):
    # PREDICTION STARTS HERE -----------------------------------------------------------------------------------------

    # Load the model from the checkpoint file where the ModelCheckpoint callback saved it to.
    model = tf.keras.models.load_model("../models/checkpoint.hdf5")

    # Get an image from the test data to feed it into the network. Since the input of the network has to
    # be 4-dimensional, we add a first dimension by reshaping the image.
    first_image = data
    first_image_4d = np.reshape(first_image, (1, 32, 32, 3))

    # Run the prediction on the loaded model
    predicted_class_probabilities = model.predict(first_image_4d)

    # Get the index of the class with the highest probability and print it.
    predicted_class = np.argmax(predicted_class_probabilities)
    probability = predicted_class_probabilities[0][predicted_class]
    if predicted_class == 0:
        cls = "airplane"
    elif predicted_class == 1:
        cls = "automobile"
    elif predicted_class == 2:
        cls = "bird"
    elif predicted_class == 3:
        cls = "cat"
    elif predicted_class == 4:
        cls = "deer"
    elif predicted_class == 5:
        cls = "dog"
    elif predicted_class == 6:
        cls = "frog"
    elif predicted_class == 7:
        cls = "horse"
    elif predicted_class == 8:
        cls = "ship"
    else:
        cls = "truck"

    return str.format("Prediction : {0} Probability {1} %", cls, probability*100)


if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.logger.debug("run!")
    app.run(host='0.0.0.0')
