import json
from database import db
from flask import redirect, url_for, request
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def __init__(self, name, email, password, role=["user"]):
        self.name = name
        self.email = email
        self.password = password
        self.role = generate_password_hash(password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def find_by_name(name):
        return User.query.filter_by(name=name).first()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)
