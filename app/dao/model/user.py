from marshmallow import Schema, fields

from app.database import db


class User(db.Model):
    """
    The User class inherits from the Model class of the flask_sqlalchemy library defines the model
    of the 'user' table of the database used.
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String(255))
    surname = db.Column(db.String)
    password = db.Column(db.String(255), nullable=False)
    favorit_genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")


class UserSchema(Schema):
    """
    The UserSchema class inherits from the Schema class of the marshmallow library and defines the schema
    of the 'user' table of the database used for serialization and deserialization of objects.
    """
    id = fields.Int(dump_only=True)
    email = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    password = fields.Str()
    favorit_genre_id = fields.Int()
