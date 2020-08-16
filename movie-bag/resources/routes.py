from .movie import MoviesApi, PingApi

def initialize_routes(api):
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(PingApi, '/api/ping')
