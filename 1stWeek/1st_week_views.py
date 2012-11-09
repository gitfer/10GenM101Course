import bottle

@bottle.route("/")
def home_page():
	mythings = ['apple', 'orange', "pear"]
	#return bottle.template('hello_world', username="Federico", stuff=mythings)
	return bottle.template('hello_world', { 'username': "Federico", 'stuff': mythings })

bottle.debug(True)
bottle.run(host="localhost", port=8080)
