from app import db, Product

# Create the database and the database table
db.create_all()

# Function to add sample products
def add_sample_products():
    # Clear existing products (optional)
    db.session.query(Product).delete()
    
    # Create sample products
    products = [
        Product(name="Product 1", description="Description of product 1", price=19.99, image_url="static/images/product1.jpg"),
        Product(name="Product 2", description="Description of product 2", price=29.99, image_url="static/images/product2.jpg"),
        Product(name="Product 3", description="Description of product 3", price=39.99, image_url="static/images/product3.jpg"),
    ]
    
    # Add products to the session
    db.session.add_all(products)
    
    # Commit the session
    db.session.commit()
    print("Sample products added!")

if __name__ == '__main__':
    add_sample_products()
