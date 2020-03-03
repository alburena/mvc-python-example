import json
from flask import Response, request, jsonify, abort
from flask_restful import Resource
from models.user import User


class UserController(Resource):
    def get(self):
        users = User.query.all()

        return jsonify([user.toJSON() for user in users])

    def post(self):
        try:
            body = request.get_json(force=True)
        
            if not body:
                return Response(errors={"message":"'No input data provided"}, mimetype="application/json", status=400)

            user = User(**body)
            err = user.save()
            if err != None:
                return Response(json.dumps({"errors":err}), mimetype="application/json", status=400)

            return user.toJSON(), 200
        except TypeError as e:
            return Response(json.dumps({"errors":"Invalid json input"}), mimetype="application/json", status=400)
        except Exception as e:
            return jsonify(errors={"message":e}), 400
    
    
class UsersController(Resource):
    def get(self, id):
        user = User.query.filter(User.id == id).first()
        if user == None:
            abort(404, 'User not found')

        return jsonify(user.toJSON())
    
    def put(self, id):
        user = User.query.filter(User.id == id).first()
        if user == None:
            abort(404, 'User not found')

        body = request.get_json(force=True)
        user.update(body)

        user = User.query.filter(User.id == id).first()
        print(user)

        return user.to_json(), 200

