from flask import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.attributes import QueryableAttribute
from .db import db

class BaseModel(db.Model):
    __abstract__ = True

    def __init__(self, **kwargs):
        self.from_dict(**kwargs)
    
    def from_dict(self, **kwargs):
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)
    
    def toJSON(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}