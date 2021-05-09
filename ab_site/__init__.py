from flask import Flask

app = Flask(__name__)

from ab_site import routes
