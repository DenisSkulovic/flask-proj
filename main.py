from flask import Flask
from flask import request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True
app.config

test = [
    {
        "id": 1,
        "bitch": True,
        "ass": True,
    },
    {
        "id": 2
    },
    {
        "id": 3
    }
]


@app.route('/', methods=["GET"])
def hello_world():
    return jsonify(test)


@app.errorhandler(404)
def page_not_found(e):
    return jsonify([
        {
            "message": "404 bitch ass nigga"
        }
    ]), 404


app.run()
