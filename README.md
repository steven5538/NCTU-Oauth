#NCTU-Oauth

台灣國立交通大學推出了 [NCTU Oauth](https://id.nctu.edu.tw/)，現在，你可以透過本套件在 Flask 使用 NCTU Oauth。

依據[交通大學 OAuth 服務 - 開發者說明文件](https://id.nctu.edu.tw/docs/)進行相對應的開發，以下是一個使用本套件開發之範例。

```Python
#-*- encoding: UTF-8 -*-

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
```