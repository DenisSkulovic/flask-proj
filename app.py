from flask import Flask
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.environ.get("SECRET_KEY")
db = SQLAlchemy(app)


@app.errorhandler(404)
def page_not_found(e):
    return jsonify([
        {
            "message": "404 bitch ass nigga"
        }
    ]), 404


if __name__ == "__main__":
    db.create_all()
    app.run()
