from flask import Flask, session, request, redirect, jsonify

# Our oauth
from nctu_oauth import Oauth

NCTU_APP_REDIRECT_URI = 'In this example is http://your.domain.name/auth'
NCTU_APP_CLIENT_ID = 'your client id'
NCTU_APP_CLIENT_SECRET = 'your client secret'

app = Flask(__name__)
app.secret_key = 'your super coll secrey key'

# make a oauth init
nctu = Oauth(
	redirect_uri=NCTU_APP_REDIRECT_URI, 
	client_id=NCTU_APP_CLIENT_ID, 
	client_secret=NCTU_APP_CLIENT_SECRET
)

@app.route("/")
def home():
	# check if login
	if session.get('logged_in'):
		# get user profile
		return jsonify(nctu.get_profile())
			
	return redirect('/login')

@app.route('/login')
def login():
	# redirect to nctu auth dialog
	return nctu.authorize()

@app.route('/auth')
def auth():
	# user code for getting token
	code = request.args.get('code')
	if code:
		#get user token
		if nctu.get_token(code):
			return redirect('/')
	
	return redirect('/login')


if __name__ == "__main__":
    app.run()