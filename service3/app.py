from flask import Flask, request, redirect, Response, jsonify
import requests
import random

app = Flask(__name__)

class roll:
    def rolling():
        value=random.randint(1,6)
        return value  

@app.route("/player", methods=["POST"])
def player():
    name= request.data.decode('utf-8')
    attempt1=roll.rolling()
    attempt2=roll.rolling()
    attempt3=roll.rolling()
    attempt4=roll.rolling()
    attempt5=roll.rolling()
    value={0: name, 1:attempt1, 2: attempt2, 3: attempt3, 4: attempt4, 5: attempt5}
    return jsonify(value)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)