from flask import Response, request, jsonify, make_response

from flask_restful import Resource
from resources.errors import  InternalServerError, MovieNotExistsError


class MoviesApi(Resource):

    def post(self):
        try:
            # user_id = get_jwt_identity()
            return make_response(jsonify([{"success":"Ok"}]), 200)

        except Exception as e:
            raise InternalServerError

class PingApi(Resource):
    def get(self):

         return make_response(jsonify([{"success":"Ok"}]), 200)
