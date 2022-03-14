import time
from click import password_option
from flask import Flask, render_template, redirect, request, url_for


app = Flask(__name__) #Instantiates Flask as "app"

@app.route('/')
def homePage():
    return render_template('menuPage.html')


@app.route('/login', methods=["POST", "GET"])#Two methods: POST and GET, POST for secure data, GET for loading pages
def loginPage():
    if request.method == "POST":    #If request method is POST, user has entered details.
        username = request.form["username"] #Take the data from the request form and store it as "username" and "password"
        password = request.form["password"]
        textmsg = username + "  " + password
        return textmsg
 
    else:
        return render_template('loginPage.html')


@app.route("/wrongDetails")
def wrongDetailsPage():
    return render_template('signUpError.html')


@app.route('/signup', methods=["POST", "GET"])
def signUpPage():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        passwordConfirm = request.form["confirmPassword"]
        if username.length > 0:
            if password == passwordConfirm:
                msg = "siuuu"
            else:
                return render_template('signUpError.html')

        else:
            return render_template('signUpError.html')
    else:
        return render_template('signUpPage.html')

#Error is that signUp page is not allowing users to create an account

        
if __name__ == "__main__":
    app.run()