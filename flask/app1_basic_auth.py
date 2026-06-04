
from flask import Flask,request,Response

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "123"

@app.route("/")
def home():
    auth = request.authorization
    if not auth or auth.username != USERNAME or auth.password != PASSWORD:
        return Response(
            "Authentication required",
            401,
            {"WWW-Authenticate": 'Basic realm="Login Required"'}
        )
    return "<h3>Welcome! You are authenticated.</h3>"

@app.route("/public")
def public():
    return "<h3>This page is public. No login needed.</h3>"

if __name__ == "__main__":
    app.run(debug=True)
