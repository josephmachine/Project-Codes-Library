from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

# class Book(db.Model):
#     __tablename__ = 'Books'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(500))
#     author = db.Column(db.String(500))
#     isbn = db.Column(db.String(50), unique=True)
#     availability = db.Column(db.String(10))
#     checkedOut = db.relationship('CheckedOut')

class Material(db.Model):
    __tablename__ = 'Materials'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    author = db.Column(db.String(500))
    type = db.Column(db.String(100))
    availability = db.Column(db.String(10))
    replacementCost = db.Column(db.Integer)
    checkedOut = db.relationship('CheckedOut')

class User(db.Model, UserMixin):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    password = db.Column(db.String(150))
    numBooks = db.Column(db.Integer)
    numMagazines = db.Column(db.Integer)
    numCDs = db.Column(db.Integer)
    numVHS = db.Column(db.Integer)
    numDVD = db.Column(db.Integer)
    checkedOut = db.relationship('CheckedOut')

class CheckedOut(db.Model, UserMixin):
    __tablename__ = 'CheckedOut'
    materialId = db.Column(db.Integer, db.ForeignKey('Materials.id'), primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('Users.id'))
    checkOutDate = db.Column(db.DateTime(timezone=True))


    