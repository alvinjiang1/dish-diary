from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class FoodEntry(db.Model):
    """
    Represents a food diary entry in the database.

    Attributes:
        id (int): The unique identifier for the food entry.
        image_url (str): The URL of the image associated with the food entry.
        description (str): The description of the food entry.
    """
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255))
    description = db.Column(db.Text)