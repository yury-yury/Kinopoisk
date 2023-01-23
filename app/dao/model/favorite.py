from marshmallow import Schema, fields

from app.database import db


class Favorite(db.Model):
    """
    The Favorite class inherits from the Model class of the flask_sqlalchemy library defines the model
    of the 'favorite' table of the database used.
    """
    __tablename__ = 'favorite'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    user = db.relationship("User")
    movie = db. relationship("Movie")


class FavoriteSchema(Schema):
    """
    The FavoriteSchema class inherits from the Schema class of the marshmallow library and defines the schema
    of the 'favorite' table of the database used for serialization and deserialization of objects.
    """
    id = fields.Int(dump_only=True)
    user_id = fields.Int()
    movie_id = fields.Int()