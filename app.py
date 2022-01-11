from flask import Flask
from flask_restful import Api

from resources.widget import Widget, WidgetList

from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Widget, '/widget/<string:name>')
api.add_resource(WidgetList, '/widgets')

if(__name__ == '__main__'):
    app.run(port=5000, debug=True)
