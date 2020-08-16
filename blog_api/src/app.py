#src/app.py

from flask import Flask

from .config import app_config

# import user_api blueprint
from .views.BlogpostView import blogpost_api as blogpost_blueprint


def create_app(env_name):
  """
  Create app
  """

  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])

  # initializing bcrypt and db
  # bcrypt.init_app(app)
  # db.init_app(app)

  app.register_blueprint(blogpost_blueprint, url_prefix='/api/v1/blogposts')

  @app.route('/', methods=['GET'])
  def index():
    """
    example endpoint
    """
    return 'Congratulations! api endpoint is working'

  return app

