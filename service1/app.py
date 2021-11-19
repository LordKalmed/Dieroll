from flask import Flask, redirect, render_template, request

app=Flask(__name__)

@app.route("/")
def homepage():
    return render_template('home.html')
    

@app.route("player", methods=["POST"])
def player():
    name=request.form["name"]
    #post to service 2 name
    #post to service 3
    # # service 2 posts to service 4 
    return render_template("results.html")              #results will get values from service 2 and 3 for name.objects
    
#@app.route("comp/<name>")
#def comp():
    #post to service 3. 
    # # service 3 posts to service 4

#@app.route("/results/<name>")
#def results():
    #Get results from service 4
    #return render_template('results.html', record=record)


#@app.run(debug=True, port=5000)
    # specify the port it listens too here. 

app.run(host="0.0.0.0", debug=True, port=5000)