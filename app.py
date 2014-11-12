from flask import Flask, request, redirect, render_template, session, escape
import json, urllib2


key = "0d7091936983bcf3195dc08f3ed4f7d4"

key2 = "AIzaSyDL5TSpzLPA-Zozqt_ObWEvNuooIy7eHtg"

#API Secret...shouldn't need this
#secret = "320445cae703c6d50a5aca4988cd3bc7"

app = Flask(__name__)
#d = None
app.secret_key = "hola"

#global contact2

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method=="GET":
        return render_template("home.html")
    else:
        session.pop('url', None)
        url = "http://api.petfinder.com/pet.find?format=json&key=" + key
        print url
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
        
        try:
            sizes.append( request.form["size1"])
        except:
            pass
        try:
            sizes.append( request.form["size2"])
        except:
            pass
        try:
            sizes.append( request.form["size3"])
        except:
            pass
        try:
            sizes.append( request.form["size4"])
        except:
            pass

        for size in sizes:
            if size != "":
                url += "&size=" + size
        
                
        req = urllib2.urlopen(url)
        d = json.loads( req.read() )

        try:
            # pets in list form
            pets = d["petfinder"]["pets"]["pet"]
        except:
            return render_template("oops.html")
            

        session['url'] = url
        
    
        print session
        return render_template("pets.html", pets=pets)

@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template("about.html")

@app.route("/pets/<pet>", methods = ["GET","POST"])
def pet(pet=None):

    print escape(session['url'])
    req = urllib2.urlopen( escape(session['url']))
    d = json.loads( req.read() )
    pet_ = None

    pets = d["petfinder"]["pets"]["pet"]
    for p in pets:
        if p['name']['$t'] == pet:
            pet_ = p


    try:
        pic = pet_["media"]["photos"]["photo"] 
        is_image = True
    except:
        is_image = False

    contact = pet_["contact"]
    global contact2
    contact2 = {}

    for item in contact:
        if contact[item].keys() != []:
            contact2[item] = contact[item]


    return render_template("pet.html", pet=pet_, is_image = is_image, contact=contact2)

@app.route("/directions", methods = ["GET", "POST"])
def directions():
    
    global address
    if request.method=="GET":
        return render_template("directions.html")
    else:
        address = request.form['address']
        b = request.form['b']
        if b == "submit":
            return redirect(url_for("results"))

@app.route("/results", methods=["GET", "POST"])
def results():

    return render_template("results.html")
    '''
    urld = "http://maps.googleapis.com/maps/api/directions/json?key=" + key2

    urld += "&origin=" + address

    dest = contact2['address']['$t']+','+contact2['city']['$t']+','+contact2['state']['$t']+','+contact2['zip']['$t']
    print dest

    urld += "&destination=" + dest
    '''




 #   req = urllib2.urlopen(urld)
#    d = json.loads(req.read())

    return "hello world"

    




    



if __name__=="__main__":
    app.debug = True
    app.run()
