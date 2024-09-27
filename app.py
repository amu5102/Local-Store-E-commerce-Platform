from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Models
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)


@app.before_first_request
def create_tables():
    db.create_all()
    add_sample_products()

def add_sample_products():
    products = [
        Product(name="Product 1", description="Description of product 1", price=19.99, image_url="static/images/product1.jpg"),
        Product(name="Product 2", description="Description of product 2", price=29.99, image_url="static/images/product2.jpg"),
        Product(name="Product 3", description="Description of product 3", price=39.99, image_url="static/images/product3.jpg"),
    ]
    db.session.add_all(products)
    db.session.commit()

# Routes
@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(product_id)
    session.modified = True
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    if 'cart' not in session:
        return render_template('cart.html', products=[], total=0)

    cart_items = Product.query.filter(Product.id.in_(session['cart'])).all()
    total = sum(item.price for item in cart_items)
    return render_template('cart.html', products=cart_items, total=total)

if __name__ == '__main__':
    app.run(debug=True)
