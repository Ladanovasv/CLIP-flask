import json
import os
from werkzeug.utils import secure_filename
from flask import request
from flask import Blueprint
from flask import render_template
from .configs import config, init_config
from .utils import allowed_file
from .model import predict

views_bp = Blueprint('CLIP', __name__)


@views_bp .route('/')
def home():
    return render_template('home.html')


@views_bp.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print("request data", request.data)
        print("request files", request.files)

        # check if the post request has the file part
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            dir_file = os.path.join('data/uploads/', filename)
            file.save(dir_file)
            # Send uploaded image for prediction
            predicted_image_class = predict(dir_file, classes)
            print("predicted_image_class", predicted_image_class)
            return json.dumps(predicted_image_class)
    return ""
