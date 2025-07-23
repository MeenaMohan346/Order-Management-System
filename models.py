from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column, Date, Integer
from flask import Flask, render_template, request,redirect, jsonify, flash, url_for, get_flashed_messages

db = SQLAlchemy()

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_name = db.Column(db.String(50), nullable=False)    
    email = db.Column(db.String(50), unique=True)
    phone_number = db.Column(db.String(10))
    shipping_address = db.Column(db.String(100))  

    @staticmethod
    def search_customers(keyword):
        """
        Searches for products based on a keyword in name or description.
        """
        if not keyword:
            return Product.query.all()  # Return all products if no keyword

        search_pattern = f"%{keyword}%"
        return Product.query.filter(
            (Product.name.ilike(search_pattern)) | 
            (Product.description.ilike(search_pattern))
        ).all()
    
class Product(db.Model):
    __tablename__ = 'products'    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)    
    product_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100))   
    unit_price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer)

class Order(db.Model):
    __tablename__ = 'orders'    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id', ondelete='SET NULL'), nullable=True) # Set to NULL when parent is deleted.)
    region = db.Column(db.String(20), nullable=False)    
    order_date = db.Column(db.Date, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)      
    
class OrdersDetails(db.Model):
    __tablename__ = 'orders_details'    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id', ondelete='SET NULL'), nullable=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id', ondelete='SET NULL'), nullable=True)
    quantity = db.Column(db.Integer, nullable=False)
    order_price = db.Column(db.Float, nullable=False)  