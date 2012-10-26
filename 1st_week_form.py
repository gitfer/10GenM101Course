import bottle

@bottle.route("/")
def home_page():
	mythings = ['apple', 'orange', "pear"]
	#return bottle.template('hello_world', username="Federico", stuff=mythings)
	return bottle.template('form', { 'username': "Federico", 'stuff': mythings })

@bottle.post("/inserisci")
def favourite_fruit():
	fruit = bottle.request.forms.get("fruit")
	if(fruit == None or fruit == ""):
		fruit = "No fruit selected"
	bottle.response.set_cookie("fruit", fruit)
	bottle.redirect("/show_fruit")
#	return bottle.template("result_tpl", {'fruit': fruit})

@bottle.get("/show_fruit")
def show_fruit():
	fruit = bottle.request.get_cookie("fruit")
	return bottle.template("result_tpl", {'fruit': fruit})

bottle.debug(True)
bottle.run(host="localhost", port=8080)
