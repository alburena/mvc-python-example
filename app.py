from dotenv import load_dotenv
from flask import Flask, make_response, jsonify
from flask_restful import Api
from controllers.routes import initialize_routes

def create_app():
    load_dotenv()

    """Construct the core application."""
    app = Flask(__name__)
    app.config.from_object('config.Config')

    api = Api(app)
    initialize_routes(api)

    return app