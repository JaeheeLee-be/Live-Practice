from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Review(db.Model):

    __tablename__ = "reviews"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Review {self.id}: {self.title}>"  