from flask import Flask, request, redirect, Response, jsonify
import requests
import random


app=Flask(__name__)

class roll:
    def rolling():
        value=random.randint(1,3)
        if value == 1:
            result = "red"
        elif value == 2:
            result = "blue"
        elif value == 3:
            result = "green"
        return result  

@app.route("/colour", methods=["GET"])
def colour():
    attempt1=roll.rolling()
    #value=str(attempt1)
    value=str(attempt1)
    return Response(value)

#@app.route("/comp", methods=["GET"])
#def comp():
#    attempt1=roll.rolling()
#    attempt3=roll.rolling()
#    attempt4=roll.rolling()
#    attempt5=roll.rolling()
#    value={1:attempt1, 2: attempt2, 3: attempt3, 4: attempt4, 5: attempt5}
#    return jsonify(value)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001, debug=True)







#get message name
#Create name.game object with players dice results in a list. e.g Angus.game[2,4,3,6,1]


#after request from service 4 for oject infor drop object