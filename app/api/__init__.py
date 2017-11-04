from flask import Blueprint
from .views.user import UserLogin
from .views.search import Search
from .views.play import Play

api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

api_bp.add_url_rule('/users', view_func=UserLogin.as_view('users'))
api_bp.add_url_rule('/search', view_func=Search.as_view('search'))
api_bp.add_url_rule('/play', view_func=Play.as_view('play'))


