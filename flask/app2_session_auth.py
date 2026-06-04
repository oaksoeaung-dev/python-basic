

from flask import Flask,session,redirect,url_for,request,render_template,flash

app = Flask(__name__)
app.secret_key = "123"

USERNAME = "admin"
PASSWORD = "123"

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == USERNAME and password == PASSWORD:
            session["username"] = username
            return redirect("/")
        flash("Invalid username or password")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username",None)
    return redirect("/login")

@app.route("/")
def home():
    if "username" not in session:
        return redirect("/login")
    return render_template("dashboard.html",username=session["username"],role="user")

@app.route("/public")
def public():
    return "<h3>This page is public. No login needed.</h3>"

if __name__ == "__main__":
    app.run(debug=True)
