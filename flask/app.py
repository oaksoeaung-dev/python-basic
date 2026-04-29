from flask import Flask,render_template,request,redirect
import business_logic.product_business_logic as product_bl

app = Flask(__name__)

#mapping
@app.route("/") #root 
def home():
    return redirect("/product_list")


@app.route("/product",methods=["GET","POST"])
def create_product():
    if request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price")
        product_bl.create_product(name,price)
        return redirect("/product_list")

    return render_template("product.html")

@app.route("/product_list")
def list_products():
    products = product_bl.get_products()
    return render_template("product_list.html",proudct_list=products)

@app.route("/product/<index>",methods=["POST"])
def delete_product(index):
    product_bl.delete_product(index)
    return redirect("/product_list")

@app.route("/product/edit/<index>", methods=["GET","POST"])
def edit_product(index):
    current = product_bl.get_product_by_index(index)
    if request.method == "GET":        
        return render_template("product_edit.html",current=current,index = index)
    else:
        name = request.form.get("name")
        price = request.form.get("price")
        product_bl.update_product(index,name,price)
        return redirect("/product_list")

if __name__ == "__main__":
    app.run(debug=True)