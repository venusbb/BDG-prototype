from flask import Flask
from govuk_frontend_jinja.flask_ext import init_govuk_frontend


app = Flask(__name__)

from app import routes
