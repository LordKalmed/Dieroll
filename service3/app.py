from flask import Flask, request, redirect, Response, jsonify
import requests
import random

app = Flask(__name__)

class roll:
    def rolling():
        value=random.randint(1,3)
        if value == 1:
            result = "1"
        elif value == 2:
            result = "2"
        elif value == 3:
            result = "3"
        return result  

@app.route("/number", methods=["GET"])
def number():
    attempt1=roll.rolling()
    #value=str(attempt1)
    value=str(attempt1)
    return Response(value)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)