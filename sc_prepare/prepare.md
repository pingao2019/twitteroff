# Questions of Understanding

1. Define the following and give an example of an appropriate task for each:


    Front-end: the "look-and-feel" of an application, as well as any logic that is executed by client-side (browser) JavaScript (which has grown surprisingly powerful)
    Back-end: the routing and "business logic", where responses (what the client sees) are built and APIs and databases are accessed
    Database: the "source of truth", where data is persisted and updated


2. What is a decorator?A decorator is a function that wraps and replaces another function. Since the original function is replaced, you need to remember to copy the original function's information to the new function. Use functools. wraps() to handle this for you.

3. What is a route?route("/") def home(): return "Hello World!" @app. route("/") is a Python decorator that Flask provides to assign URLs in our app to functions easily. It's easy to understand what is happening at first glance: the decorator is telling our @app that whenever a user visits our app domain (myapp.com) at the given

4. Why do we want to separate our code into separate files when writing an application? Why not just one big file?---The "why" would be the desire to reduce the size of a massive models.py file

5. What is an API? Give an example of an API that is not Twitter's.
Application programming interface, which helps a programmer to create software. A set of protocols defining how hardware and software can interact in a machine or across a networkBR3:Application programming interface, which is an intermediary allowing two applications to communicate. Amazon

6. What does it mean to pickle a model? Why might this be useful?What is a pickle/the process of pickling in python?
BR1: You can pickle a Python object for later use by adding the object in a jar, with a brine solution and some flavoring of choice!
BR2: The process of pickling refers to the serialization (storing the object to memory, a database, or a file) and deserialization of a Python Object. It's a way to convert a list, dictionary, or other object into a character stream.
BR3:Serialization of python objects to be saved to disk and reused in a future program. 
BR4: A pickle is a python object that’s been converted into a byte stream. Python objects are usually pickled in order to store them in databases, such as the BASILICA embeddings we used in Tuesday’s module.


​

# Basics of Flask
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

​

## Coding

Write a Flask application that displays "Hello World!" to the local host (usually `127.0.0.1:5000` or `localhost:5000`)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

​

## Questions of Understanding

1. Flask is described as a "microframework" for developing web applications. What is a "microframework"? Flask, a "microframework" for developing web applications. All this really means is that it's small and modular, and mostly just provides for URL routing and responses - for other things (templates, database, forms) you pick and choose your own other packages (and we'll give you some specific choices for this week).

This is in contrast with Django, the most popular "industry-grade" Python web application framework. Django is opinionated, and comes with built-in modules for pretty much everything.

There are more projects built with Django than Flask, but Flask is solidly second place in the Python web application ecosystem, and is a better minimal choice for a data scientist who just wants to get some results.

2. What is another web development framework in Python? Django is a full packaged framework that is less modular then flask, where flask is good for plugging parts into an existing web serving framework. django is better if there is no framework being used to get a solid foundation to build from. 
BR4: Django is a web app system designed to let you use it right out of the box with little hassle and provides a lot of built-in capability to create a web app from the ground up using only Django itself. Flask, on the other hand is very barebones but allows a greater degree of modularity and is more suited to lightweight web apps.


3. In this line of code: `APP = Flask(__name__)` What does `__name__` do?

4. What line of your code tells when and where "Hello World!" should be displayed?

5. What do we need to type into the terminal to run our flask application?

​FLASK_APP=hello.py flask run

# API's
FLASK_APP=web_app flask run
​

## Coding

API's are a common part of programming, whether setting up your own or using someone else's. Today we will be looking at the API for the board gaming hobby site BoardGameGeek (BGG). The API instructions can be found [here](https://boardgamegeek.com/wiki/page/BGG_XML_API&redirectedfrom=XML_API#). There are many wrappers online for the BGG API that you may use but the sample code below will use `requests` and the web scraping library `BeautifulSoup`.

​

```python

import requests

import bs4

​

game_id = 13

url = 'https://www.boardgamegeek.com/xmlapi/boardgame/' + str(game_id)

result = requests.get(url)

soup = bs4.BeautifulSoup(result.text, features='lxml')

print(soup.find('name').text)

```

​

The code above uses the API to search for a game by its ID number (more than 16,000 entries on BGG). Once the API returns the results, BeautifulSoup is used to parse the XML and make it easily searchable.

​

Explore the BGG API and see if you are able to find the following information about a game:

- Name

- Max and Min Players

- Play Time

- Game Description

- Some of the game mechanics

​

# Flask and Databases

​

## Code

Write a Flask web application using `SQLAlchemy` with the following:

- A home route that displays at least one entry from a database of stored BGG game information

- A dynamic route `/add/<game_id>` that adds game information into your database based on the ID in the route.

- A route that resets the database

- The database should have the following following columns as a minimum: id (integer), name (string), and max_players (integer)

​

## Questions of Understanding

1. What line of code establishes what database should be used for your application?

2. How do we define our table, what columns are going to be in it, and what those column datatypes are?

3. How do we make a query to our database?

​

# HTML Templates

​

## Code

Create a small HTML template to display all the games in your database. Update your home route to use this template.

​

## Questions of Understanding

1. What is an HTML template?

2. What module do we need to import from `flask` to use our HTML template?

​

# Heroku

​

## Code

It is not necessary, but you can try putting your app on Heroku

​

## Questions of Understanding

1. What is a platform-as-a-service?

2. Why do we need to use a service like Heroku? Why not just host the application on our local machine?

