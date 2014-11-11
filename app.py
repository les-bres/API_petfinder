from flask import Flask, request, redirect, render_template, session, escape
import json, urllib2


key = "0d7091936983bcf3195dc08f3ed4f7d4"

#API Secret...shouldn't need this
#secret = "320445cae703c6d50a5aca4988cd3bc7"

app = Flask(__name__)
d = None

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method=="GET":
        return render_template("home.html")
    else:
        url = "http://api.petfinder.com/pet.find?format=json&key=" + key
        url += "&location=" + request.form["zip"]

        type = request.form["type"]
        if (type != ""):
            url += "&animal=" + type

        ages = []
        
        try:
            ages.append( request.form["age1"])
        except:
            pass
        try:
            ages.append( request.form["age2"])
        except:
            pass
        try:
            ages.append( request.form["age3"])
        except:
            pass
        try:
            ages.append( request.form["age4"])
        except:
            pass

        for age in ages:
            if age != "":
                url += "&age=" + age
        
        
        sizes = []
        sizes.append( request.form["size1"])
        sizes.append( request.form["size2"])
        sizes.append( request.form["size3"])
        sizes.append( request.form["size4"])

        for size in sizes:
            if size != "":
                url += "&size=" + size
                
        print url
        req = urllib2.urlopen(url)
        d = json.loads( req.read() )

        # pets in list form
        pets = d["petfinder"]["pets"]["pet"]

        #session['pets'] = pets
        #session['yo'] = "hi"
    
        #print session
        return render_template("pets.html", pets=pets)

@app.route("/pets/<pet>", methods = ["GET","POST"])
def pet(pet=None):
    
    pets = d["petfinder"]["pets"]["pet"]
    pet_ = None
    for p in pets:
        if p['name']['$t'] == pet:
            pet_ = p
            print "horray"

            
    return render_template("pet.html", pet=pet_)

if __name__=="__main__":
    app.debug = True
    app.run()
