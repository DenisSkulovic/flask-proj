from flask import Flask
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True
app.config

db = SQLAlchemy(app)


@app.errorhandler(404)
def page_not_found(e):
    return jsonify([
        {
            "message": "404 bitch ass nigga"
        }
    ]), 404


app.run()
