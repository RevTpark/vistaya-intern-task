from flask import Flask, request, session
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

# import Route Classes
from api import InputValidatorAPI, SlotBookingAPI, SlotCancelAPI, SquareCheck

# Initialize app and database
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///temporaryDatabase.db"
db = SQLAlchemy(app)

# Initialize RESTful API and paths
api = Api(app, prefix="/api")

api.add_resource(InputValidatorAPI, "/items")
api.add_resource(SlotBookingAPI, "/slot/booking")
api.add_resource(SlotCancelAPI, "/slot/cancel")
api.add_resource(SquareCheck, "/plot")
