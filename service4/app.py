from typing import Text
from flask import Flask, request, redirect, Response, jsonify
import requests
import random

app = Flask(__name__)

class roll:
    def rolling():
        value=random.randint(1,6)
        return value  

@app.route("/score", methods=["POST", "GET"])
def game():
    #get the name from main page
    number=requests.get("http://service3:5002/number")
    num=number.text
    colour=requests.get("http://service2:5001/colour")
    col=colour.text
    luck= " "
    if num == "1":
        luck = "You will win"
    elif num == "2":
        luck = "You will come second"
    elif num == "3":
        luck = "You will loose"
    enviro=" "
    if col == "red":
        enviro = "in your next relatioship"
    if col == "blue":
        enviro = "in your next job"
    if col == "green":
        enviro = "in your next home"
    message= luck+" "+enviro
    return Response(message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)