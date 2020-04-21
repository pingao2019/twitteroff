from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

# Each class we make will be a table in the DB


class User(DB.Model):

    """ TWITTER USERS we analyze"""

    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)
    # newest_tweet_id = DB.Column(DB.BigInteger)
    # formatting

    def __repr__(self):
        return '<User {}>'.format(self.name)


class Tweet(DB.Model):

    """TWEETS we pull"""
    
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))
    # formatting

    def __repr__(self):
        return '<Tweet {}>'.format(self.text)