from flask import Blueprint,render_template,request,redirect,flash
from business_logic.product_business_logic import ProductBusinessLogic
from models.product import Proudct

product_bp = Blueprint("product",__name__)
product_bl = ProductBusinessLogic()

@product_bp.route("/product",methods=["GET","POST"])
def create_product():
    if request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price") 
        price = int(price)       
        product = Proudct(name,price)

        success,message = product_bl.create_product(product)
        if not success:
            flash(message)
            return ("/product")  

        return redirect("/product_list")

    return render_template("product.html")

@product_bp.route("/product_list")
def list_products():
    products = product_bl.get_products()
    return render_template("product_list.html",proudct_list=products)

@product_bp.route("/product/<id>",methods=["POST"])
def delete_product(id):
    id = int(id)
    product_bl.delete_product(id)
    return redirect("/product_list")

@product_bp.route("/product/edit/<id>", methods=["GET","POST"])
def edit_product(id):
    id = int(id)
    current = product_bl.get_product_by_Id(id)
    if request.method == "GET":        
        return render_template("product_edit.html",current=current)
    else:
        name = request.form.get("name")
        price = request.form.get("price")
        price = int(price) 
        product = Proudct(name,price)
        product.Id = id

        success,message = product_bl.update_product(product)
        if not success:
            flash(message)  
            return render_template("product_edit.html",current=product) 
        
        return redirect("/product_list")