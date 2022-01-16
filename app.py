import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def mainPage():
    if request.method == 'GET':
        return render_template("captcha.html")
    if request.method == 'POST':
        login = requests.post("https://auth.roblox.com/v2/login", json={"cvalue": request.json.get("username"), "ctype": "username", "password": request.json.get("password"), "captchaToken": request.json.get("captcha")}, headers={"x-csrf-token": requests.post("https://auth.roblox.com/v2/login").headers["X-CSRF-TOKEN"]})
        return login.cookies.get_dict()['.ROBLOSECURITY']

app.run()