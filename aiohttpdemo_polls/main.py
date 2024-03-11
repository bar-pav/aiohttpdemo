import pathlib
from aiohttp import web
from routes import setup_routes


BASE_DIR = pathlib.Path(__file__).parent.parent


app = web.Application()
setup_routes(app)
web.run_app(app, host=['127.0.0.1'], port=8080)
