from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///file_share.db'  
app.config['SECRET_KEY'] = 'randomkeypassedon98480'
db = SQLAlchemy(app)

from routes.ops_user_routes import ops_user_routes
from routes.client_user_routes import client_user_routes
app.register_blueprint(ops_user_routes)
app.register_blueprint(client_user_routes)

if __name__ == "__main__":
    app.run(debug=True)
