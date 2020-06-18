from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eb289e8e6629dd79004bf93963dc2933'

from app import routes