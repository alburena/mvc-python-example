from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def initialize_db(app):
    db.init_app(app)

    # Create tables for our models
    with app.app_context():
            db.create_all()
