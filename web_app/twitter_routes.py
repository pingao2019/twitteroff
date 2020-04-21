# web_app/routes/twitter_routes.py



from flask import Blueprint, render_template, jsonify

from web_app.models import db, User, Tweet, parse_records


twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>")
