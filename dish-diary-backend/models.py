from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class FoodEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255))
    description = db.Column(db.Text)