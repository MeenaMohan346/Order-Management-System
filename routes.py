from flask import Flask, render_template, request, redirect, jsonify
from models import Customer, Product, Order, OrdersDetails

# app = Flask(__name__)
app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/customers')
def customers():
    all_customers = Customer.query.order_by(Customer.id).all()                     
    return render_template('ordermanagement.html', customers=all_customers)

@app.route('/products')
def products():
    all_products = Product.query.order_by(Product.id).all()      
    return render_template('ordermanagement.html', products=all_products)

@app.route('/orders')
def orders():
    all_orders = Order.query.order_by(Order.id).all()     
    return render_template('ordermanagement.html', orders=all_orders)

@app.route('/orders_details')
def orders_details():
    all_orders_details = OrdersDetails.query.order_by(OrdersDetails.id).all()       
    return render_template('ordermanagement.html', orders_details=all_orders_details)