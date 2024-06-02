from flask import Flask
from database import db

app = Flask(__name__)
app.config.from_prefixed_env()
db.init_app(app)
