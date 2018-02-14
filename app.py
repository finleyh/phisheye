from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
	return "/domain<br/> /domain/add/:name:<br/>/domain/remove/:name:<br/><br/>/results<br/>/results/:domain:<br/>/results/:domain:/:number_of_results:"

@app.route('/domain/add/<url>',methods=['GET'])
def create_domain(url):
	#create a new domain submission 
	return "create the domain {}".format(url)

@app.route('/domain/remove/<url>',methods=['GET'])
def delete_domain(url):
	#delete a domain by string name
	return "delete the domain {}".format(url)

@app.route('/domain', methods=['GET'])
def list_domains():
	return "list submitted domains"

@app.route('/results', methods=['GET'])
def list_results():
	#return the most recent round of results
	return "list results"

@app.route('/results/<domain>', methods=['GET'])
@app.route('/results/<domain>/<int:limit>', methods=['GET'])
def domain_results():
	#if limit is set, set the limit for the sql query to that value
	if limit:
		return "results for domain, with specified limit"	
	#limit should default to 5 in the sql query
	else:
		return "results, for domain, defaults to last  5"

		

if __name__=='__main__':
	app.run()
