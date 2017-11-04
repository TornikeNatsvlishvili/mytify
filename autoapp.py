from app.app import create_app
from app.settings import DevConfig, ProdConfig

from flask.helpers import get_debug_flag

CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)
