from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from sec.secure import authenticate, identity
from sec.user import UserRegister
from src.item import Item, ItemList
from init_db import Table

from settings.config import (
    app_key,
    main_user,
    main_pass
)

tableinfo = [
    ['users', 'items'], 
    ['name text, price real', 'id INTEGER PRIMARY KEY, username TEXT, password TEXT'],
    [main_user, main_pass]
]

users = Table(str(tableinfo[0][0]))
items = Table(str(tableinfo[0][1]))

users

app = Flask(__name__)
app.secret_key = app_key
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
