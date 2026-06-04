from flask import Blueprint,render_template,request,redirect,session,flash
from functools import wraps
from business_logic.user_business_logic import UserBusinessLogic

auth_bp = Blueprint("auth",__name__)
user_bl = UserBusinessLogic()
def login_required(f):
    @wraps(f) ## flask
    def check(*args,**kwargs):
        if "username" not in session:
            return redirect("/login")
        return f(*args,**kwargs) 
    return check

def admin_required(f):
    @wraps(f)
    def check(*args,**kwargs):
        if "username" not in session:
            return redirect("/login")
        if session.get("role") != "admin":
            flash("Admin access required.")
            return redirect("/")
        return f(*args,**kwargs)
    return check

@auth_bp.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        success,result = user_bl.authenticate_user(username,password)
        if success:
            session["username"] = result.username
            session["role"] = result.role
            return redirect("/")
        flash(result)
    return render_template("login.html")

@auth_bp.route("/register",methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        success,message = user_bl.register_user(username,password)
        if success:
            flash("Registration successful! Please login.")
            return redirect("/login")
        flash(message)
    return render_template("register.html")

@auth_bp.route("/logout")
def logout():
    session.pop("username",None)
    session.pop("role",None)
    return redirect("/login")

@auth_bp.route("/")
@login_required
def home():
    return render_template("dashboard.html",username=session["username"],role=session["role"])

@auth_bp.route("/admin")
@admin_required
def admin():
    return render_template("dashboard.html",username=session["username"],role=session["role"])
