from flask import Flask, render_template, request
from kiteconnect import KiteConnect

api_key='w8tleztptoyn1udq'
api_secret='mdeh32ryp2cr516979nl7qdm2itd2w32'
kite = KiteConnect(api_key)


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
#@app.route('/authenticate', methods=['GET', 'POST'])
def get_request_token():
    access_token = ''

    req_token_url = kite.login_url()

    # get access token
    if request.method=='POST':
        request_token = request.form.get('request_token')
        print('hey')
        print(request_token)
        data = kite.generate_session(request_token, api_secret)
        access_token = data['access_token']
        kite.set_access_token(access_token)

    return render_template('authenticate.html', req_token_url=req_token_url, access_token=access_token)

if __name__ == '__main__':
    app.run()
        

        
        
