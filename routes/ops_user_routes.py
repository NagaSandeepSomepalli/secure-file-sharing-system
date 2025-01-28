from flask import Blueprint, request, jsonify
from models import User, db
from werkzeug.security import generate_password_hash

client_user_routes = Blueprint('client_user_routes', __name__)

@client_user_routes.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'])
    new_user = User(username=data['username'], email=data['email'], password=hashed_password, user_type="client")
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"})

from flask import Blueprint, request, jsonify
import os

ops_user_routes = Blueprint('ops_user_routes', __name__)

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'pptx', 'docx', 'xlsx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@ops_user_routes.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"})
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return jsonify({"message": "File uploaded successfully"})
    else:
        return jsonify({"message": "Invalid file type"})
