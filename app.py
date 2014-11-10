from flask import Flask, request, redirect, render_template, session
import json, urllib2


key = "0d7091936983bcf3195dc08f3ed4f7d4"

#API Secret...shouldn't need this
#secret = "320445cae703c6d50a5aca4988cd3bc7"

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method=="GET":
        return render_template("home.html")
    else:
        url = "http://api.petfinder.com/pet.find?format=json&key=" + key
        url += "&location=" + request.form["zip"]
        print url
        req = urllib2.urlopen(url)
        d = json.loads( req.read() )
        print d
        return "hi"

if __name__=="__main__":
    app.debug = True
    app.run()
