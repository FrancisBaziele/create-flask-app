//importing flask, make sure flask is installed
from flask import Flask
import wtforms

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"

from project import routes