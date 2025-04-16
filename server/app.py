from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from models import db
from routes import register_routes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
db.init_app(app)
Migrate(app, db)
register_routes(app)

@app.route('/')
def home():
    return {"message": "Late Show API running 🚀"}
