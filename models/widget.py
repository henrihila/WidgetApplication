from datetime import datetime
from db import db


class WidgetModel(db.Model):
    __tablename__ = 'widgets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    number_of_parts = db.Column(db.Integer)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    updated_date = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, name, number_of_parts):
        self.name = name
        self.number_of_parts = number_of_parts

    def json(self):
        return {
            'name': self.name,
            'number_of_parts': self.number_of_parts
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
