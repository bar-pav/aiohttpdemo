import pathlib

import aiohttp_jinja2
import jinja2
from aiohttp import web

from routes import setup_routes
from settings import config
from db import pg_context


BASE_DIR = pathlib.Path(__file__).parent.parent


app = web.Application()
setup_routes(app)
app['config'] = config
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(BASE_DIR / 'aiohttpdemo_polls' / 'templates')))
app.cleanup_ctx.append(pg_context)
web.run_app(app, host=['127.0.0.1'], port=8080)
