from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

# Create a MetaData object
metadata = MetaData()

# Initialize the SQLAlchemy instance
db = SQLAlchemy(metadata=metadata)

# Earthquake model definition
class Earthquake(db.Model, SerializerMixin):
    __tablename__ = 'earthquakes'

    # Define columns
    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float)
    location = db.Column(db.String)
    year = db.Column(db.Integer)

    # Define the __repr__ method for string representation
    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"
