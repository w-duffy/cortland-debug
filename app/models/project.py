from datetime import datetime
from .db import db, environment, SCHEMA, add_prefix_for_prod

class Project(db.Model):
    __tablename__ = 'projects'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    goal = db.Column(db.Numeric(10, 2), nullable=False)
    location = db.Column(db.Text, nullable=False)
    media_url = db.Column(db.Text, nullable=False)
    deadline = db.Column(db.DateTime, default=datetime.now())


    def to_dict(self):
        return {
            "id": self.id,
            "amount": float(self.amount),
            "user_id": self.user_id,
            "title": self.title,
            "description": self.description,
            "body": self.body,
            "goal": float(self.goal),
            "location": self.location,
            "media_url": self.media_url,
        }
