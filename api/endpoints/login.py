from flask_restful import Resource

from database import db

class Login(Resource):
    def get(self):
        print(db.cursor)
        return {"Hello": "world"}

    