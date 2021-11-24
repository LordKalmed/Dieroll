from flask import Flask, request, redirect, Response, jsonify
import requests
import random

app = Flask(__name__)

class roll:
    def rolling():
        value=random.randint(1,6)
        return value  

@app.route("/service4", methods=["POST", "GET"])
def game():
    player=requests.post("http://service3:5000/player", data = "angus" )
    comp=requests.get("http://service2:5000/comp")
    return jsonify(player, comp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)