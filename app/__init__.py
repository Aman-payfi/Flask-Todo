from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from app.config import Config  # Corrected import

app = Flask(__name__)
app.config.from_object(Config)  # Use the imported Config class
db = SQLAlchemy(app)
jwt = JWTManager(app)

from app import routes


# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_jwt_extended import JWTManager
# from app.config import Config 

# app = Flask(__name__)
# app.config.from_object('config')
# db = SQLAlchemy(app)
# jwt = JWTManager(app)

# from app import routes