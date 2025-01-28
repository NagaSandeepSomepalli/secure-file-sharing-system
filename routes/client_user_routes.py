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
from flask import jsonify
from utils import generate_secure_url

@client_user_routes.route('/download/<int:file_id>', methods=['GET'])
def download_file(file_id):
    secure_url = generate_secure_url(file_id)
    return jsonify({"download-link": f"http://localhost:5000/download-file/{secure_url}"})
