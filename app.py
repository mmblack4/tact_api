from flask import Flask
from flask_restful import  Api

from resources.user import User, UserList, UserBy
# from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(User, '/user/<string:username>')
api.add_resource(UserBy, '/user/<string:column>/<string:column_value>')
api.add_resource(UserList, '/users')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)