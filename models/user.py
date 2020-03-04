import datetime
from .db import db
from .baseModel import BaseModel
from flask_wtf import FlaskForm

class User(BaseModel):
    """Data model for user accounts."""

    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    firstname = db.Column(db.String(64),index=False,unique=True,nullable=False)
    email = db.Column(db.String(80),index=True,unique=True,nullable=False)
    created_at = db.Column(db.DateTime,index=False,unique=False, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime,index=False,unique=False, nullable=False, server_default=db.func.now(), server_onupdate=db.func.now())
    bio = db.Column(db.Text,index=False,unique=False,nullable=True)
    role = db.Column(db.String(20),index=False,unique=False,nullable=False)

    def save(self):
        try:
            self.role = 'public'
            db.session.add(self)
            db.session.commit()
        except Exception as error:
            return str(error.orig)

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)

        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()