# web_app/routes/home_routes.py

from flask import Blueprint
home_routes = Blueprint('home_routes', __name__)

@home_routes.route('/')
def hello():
    print('VISITED THE HELLO PAGE')
    return "Hello world!"
       
@home_routes.route('/about')
def about():
    print('Visted the about page')
    return"About Me!"

@home_routes.route('/iris')
def iris():    from sklearn.datasets import load_iris
 from sklearn.linear_model import LogisticRegression
 X, y = load_iris(return_X_y=True)
 clf = LogisticRegression(random_state=0, solver='lbfgs',
                          multi_class='multinomial').fit(X, y)

 return str(clf.predict(X[:2, :]))
