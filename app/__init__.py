from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from stackifyapm.contrib.flask import StackifyAPM

app = Flask(__name__)
app.config['APPLICATION_NAME'] = 'flask-app'
app.config['ENVIRONMENT'] = 'Production'
StackifyAPM(app)
app.config.from_object('config')
db = SQLAlchemy(app)


from app import views, models