
from flask import Flask
from endpoints.auth_bp import auth_bp

app = Flask(__name__)
app.register_blueprint(auth_bp)
app.secret_key = "123"

if __name__ == "__main__":
    app.run(debug=True)
