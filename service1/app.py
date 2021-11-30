from flask import Flask, redirect, render_template, request, jsonify
import requests
import json

app=Flask(__name__)

@app.route("/")
def homepage():
    rec=requests.get("http://service4:5003/score")
    record=rec.text
    return render_template('home.html', records=record)
    

#results will get values from service 2 and 3 for name.objects
    
#@app.route("/results", methods=["POST", "GET"])
#def comp():
    #post to service 3. 
    # # service 3 posts to service 4

#@app.route("/results/<name>")
#def results():
    #Get results from service 4
    #return render_template('results.html', record=record)


#@app.run(debug=True, port=5000)
    # specify the port it listens too here. 

app.run(host="0.0.0.0",debug=True, port=5000)