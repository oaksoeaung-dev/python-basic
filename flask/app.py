from flask import Flask,redirect
from endpoints.product import product_bp
from endpoints.category import category_bp

app = Flask(__name__)
app.register_blueprint(product_bp)
app.register_blueprint(category_bp)
app.secret_key="123"

#mapping
@app.route("/") #root 
def home():
    return redirect("/product_list")

if __name__ == "__main__":
    app.run(debug=True)

#boostraper