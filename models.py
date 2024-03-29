""" SQLAlchemy models and utlity  funcitons for twittoff"""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    """Twitter Users corresponding to Tweets"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String, nullable=False)

    def __repre__(self):
        return "<User: {}>".format(self.name)

class Tweet(DB.Model):
    """tweet related to a user"""
    id = DB.Column(DB.BigInteger,primary_key=True)
    text = DB.Column(DB.Unicode(300))
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user =DB.relationship("User", backref=DB.backref("tweets", lazy=True))

def __repre__(self):
    return "<Tweet: {}>".format(self.text)