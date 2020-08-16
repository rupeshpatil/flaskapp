#/src/views/BlogpostView.py
from flask import request, g, Blueprint, json, Response

blogpost_api = Blueprint('blogpost_api', __name__)


@blogpost_api.route('/', methods=['POST'])
def create():
  """
  Create Blogpost Function
  """
  # req_data = request.get_json()


  return custom_response([{'message':"OK"}], 200)

@blogpost_api.route('/', methods=['GET'])
def get_all():
  """
  Get All Blogposts
  """
  data = [{"title":"abc sdsd","description":"ssfdsdfsd fsfsf sf sdfsdf"}]
  return custom_response(data, 200)


def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )

