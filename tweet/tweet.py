from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

# Each class we make will be a table in the DB
#import basilica
#conn = basilica.Connection('5ec9ed3f-ab63-052c-4126-f8706da6c18b')
#embedding = conn.embed_sentence('hey this is a cool tweet', model='twitter')

class User(db.Model):

    """ TWITTER USERS we analyze"""

    id = db.Column(db.BigInteger, primary_key=True)
    screen_name = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String)
    location = db.Column(db.String)
    followers_count = db.Column(db.Integer)
    latest_tweet_id = db.Column(db.BigInteger)
    


class Tweet(DB.Model):

    """TWEETS we pull"""

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey("user.id"))
    full_text = db.Column(db.String(500))
    embedding = db.Column(db.PickleType)

    user = db.relationship("User", backref=db.backref("tweets", lazy=True))

    def __repr__(self):
        return '<Tweet {}>'.format(self.text)



