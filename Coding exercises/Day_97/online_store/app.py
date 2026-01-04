# Import needed modules
import stripe
from flask import Flask, render_template, redirect, url_for, session, request
from flask_login import LoginManager, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

# Import needed functions and classes from other scripts within the app
from models import db, User, Product
from forms import RegistrationForm, LoginForm
from config import Config

#############
# App setup #
#############
load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

stripe.api_key = app.config["STRIPE_SECRET_KEY"]

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

########
# Home #
########


@app.route("/")
def index():
    products = Product.query.all()
    return render_template("index.html", products=products)

################
# Authenticate #
################


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if User.query.filter_by(email=email).first():
            return "User already exists"
        user = User(email=email, password_hash=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for("index"))
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            return redirect(url_for("index"))
        return "Invalid credentials"
    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

########
# Cart #
########


@app.route("/add-to-cart/<int:product_id>")
def add_to_cart(product_id):
    cart = session.get("cart", {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    session["cart"] = cart
    return redirect(url_for("cart"))


@app.route("/update-cart", methods=["POST"])
def update_cart():
    cart = session.get("cart", {})

    product_id = request.form.get("product_id")
    quantity = request.form.get("quantity")

    if product_id and quantity:
        quantity = int(quantity)

        if quantity <= 0:
            cart.pop(product_id, None)
        else:
            cart[product_id] = quantity

    session["cart"] = cart
    return redirect(url_for("cart"))


@app.route("/cart")
def cart():
    cart = session.get("cart", {})
    items = []
    total_cents = 0
    for product_id, qty in cart.items():
        product = Product.query.get(int(product_id))
        if product:
            subtotal = product.price_cents * qty
            total_cents += subtotal
            items.append({"product": product, "quantity": qty, "subtotal": subtotal})
    return render_template("cart.html", items=items, total_cents=total_cents)

############
# Checkout #
############


@app.route("/checkout")
@login_required
def checkout():
    cart = session.get("cart", {})
    if not cart:
        return redirect(url_for("cart"))

    line_items = []
    for product_id, qty in cart.items():
        product = Product.query.get(int(product_id))
        if product:
            line_items.append({
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": product.name},
                    "unit_amount": product.price_cents,
                },
                "quantity": qty,
            })

    session_stripe = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        mode="payment",
        success_url=url_for("success", _external=True),
        cancel_url=url_for("cart", _external=True),
    )

    return redirect(session_stripe.url)


@app.route("/success")
def success():
    session.pop("cart", None)
    return render_template("success.html")

###########
# Run app #
###########


if __name__ == "__main__":
    app.run(debug=True)
