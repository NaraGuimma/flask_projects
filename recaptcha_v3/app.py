from urllib import response
from flask import Flask, render_template, redirect, url_for, request, abort
import requests


app = Flask(__name__)


SITE_KEY = 'SITE_KEY'
SECRET_KEY = 'SECRET_KEY'
VERIFY_URL = 'https://www.google.com/recaptcha/api/siteverify'


@app.route("/", methods=['GET'])
def home():
    return render_template('home.html', site_key=SITE_KEY)


@app.route("/sign-user-up", methods=['POST'])
def sign_up_user():
    print(request.form)
    secret_response = request.form['g-recaptcha-response']

    verify_response = requests.post(url=f'{VERIFY_URL}?secret={SECRET_KEY}&response={secret_response}').json()
    print(verify_response)

    if verify_response['success'] == False or verify_response['score'] < 0.5:
        abort(401)

    return redirect(url_for('home'))


if __name__=='__main__':
    app.run(debug=True)