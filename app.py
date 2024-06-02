from flask import Flask
from views import BLUEPRINTS
from database import db

app = Flask(__name__)
app.config.from_prefixed_env()
db.init_app(app)

for bp in BLUEPRINTS:
    app.register_blueprint(bp)
