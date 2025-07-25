# app.py
import os
from flask import Flask, render_template, request,redirect, jsonify, flash, url_for, get_flashed_messages, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import label
from datetime import datetime
import sys
import os
import json
from sqlalchemy.sql import func

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

# Get the directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# Add the parent directory to sys.path
sys.path.append(parent_dir)

# Now you can import modules from the parent directory
# Assuming 'my_module.py' is in the parent directory
import models
import routes  

# App set up
app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY']  = "12345"

# Load environment variables from .env file
""" from dotenv import load_dotenv
load_dotenv()  """

# Construct the database URI
username = os.getenv("PG_USERNAME", "postgres")
password = os.getenv("PG_PASSWORD", "meena")
database_name = os.getenv("DATABASE_NAME", "postgres")
host = os.getenv("PG_HOST", "localhost")
port = os.getenv("PG_PORT", "5432")

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Dummy user data (for demonstration purposes - replace with a database in production)
username = "admin"
password = "admin123"
users = {'username': 'admin', 'password': 'admin123'}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_input = request.form['username']
        password_input = request.form['password']
        if users['username'] == username_input and users['password'] == password_input:
            session['logged_in'] = True
            session['username'] = username_input
            flash('Logged in successfully!', 'success')
            return redirect(url_for('search_page'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/search')
def search_page():
    if 'logged_in' in session and session['logged_in']:
        return render_template('search.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('login'))


#db = SQLAlchemy(app)
models.db.init_app(app) 

# Initialize database
with app.app_context():
    models.db.create_all() 

@app.route('/data_display', methods=['GET', 'POST'])
def data_display():
    if request.method == 'POST':
        data = None
        # Get data from the form
        button_clicked = request.form.get('button_name')  # 'name' is the name attribute of button
        # Process the button click and generate data
        if button_clicked == 'button_a':
            rows_count = models.db.session.query(routes.Customer).count()            
            if rows_count == 0: # No existing customers, so perform bulk insert                
                 customers_to_insert = [                     
                    models.Customer(customer_name='John Smith', email='john.smith@example.com', phone_number='1111111111', shipping_address='123 Main St, Anytown'),
                    models.Customer(customer_name='Jane Doe', email='jane.doe@example.com', phone_number='1111111112', shipping_address='456 Elm St, AnotherTown'),
                    models.Customer(customer_name='Michael Johnson', email='michael.johnson@example.com', phone_number='1111111113', shipping_address='789 Oak St, Somewhere'),
                    models.Customer(customer_name='Emily Wilson', email='emily.wilson@example.com', phone_number='1111111114', shipping_address='567 Pine St, Nowhere'),
                    models.Customer(customer_name='David Brown', email='david.brown@example.com', phone_number='1111111115', shipping_address='321 Maple St, Anywhere')
                ]
                 models.db.session.bulk_save_objects(customers_to_insert)
                 models.db.session.commit()

            data = routes.customers()            
        elif button_clicked == 'button_b':
            rows_count = models.db.session.query(routes.Product).count()            
            if rows_count == 0: # No existing products, so perform bulk insert                
                 products_to_insert = [                    
                    models.Product(product_name='T-Shirt',	description='Comfortable cotton T-shirt.',	unit_price=25,	stock_quantity=200),
                    routes.Product(product_name='Headphones',	description='Noise-canceling headphones for immersive audio',	unit_price=150,	stock_quantity=75),
                    routes.Product(product_name='Jeans',	description='Classic denim jeans', unit_price=50,	stock_quantity=150),
                    routes.Product(product_name='Mouse',	description='Ergonomic wireless mouse',	unit_price=30,	stock_quantity=100),
                    routes.Product(product_name='Stove',	description='Gas stove top',	unit_price=550,	stock_quantity=100)
                     ]
                 models.db.session.bulk_save_objects(products_to_insert)
                 models.db.session.commit()

            data = routes.products()            
        elif button_clicked == 'button_c':
            rows_count = models.db.session.query(routes.Order).count()            
            if rows_count == 0: # No existing orders, so perform bulk insert                
                 orders_to_insert = [                  
                    models.Order(customer_id=1,	region="TX", order_date="2025-07-23"),
                    models.Order(customer_id=2,	region="FL", order_date="2025-07-23"),
                    models.Order(customer_id=5,	region="NC", order_date="2025-07-23")
                     ]
                 models.db.session.bulk_save_objects(orders_to_insert)
                 models.db.session.commit()

            data = routes.orders()            
        elif button_clicked == 'button_d':
            rows_count = models.db.session.query(routes.OrdersDetails).count()            
            if rows_count == 0: # No existing orders details, so perform bulk insert                
                 orders_details_to_insert = [                                        
                    models.OrdersDetails(order_id=1, product_id=3, quantity=5,	order_price=250),
                    models.OrdersDetails(order_id=1, product_id=5, quantity=10,	order_price=5500),
                    models.OrdersDetails(order_id=1, product_id=1, quantity=15,	order_price=330),
                    models.OrdersDetails(order_id=2, product_id=2, quantity=5,	order_price=750),                    
                    models.OrdersDetails(order_id=2, product_id=1, quantity=7,	order_price=154),                   
                    models.OrdersDetails(order_id=3, product_id=3, quantity=2,	order_price=100),
                    models.OrdersDetails(order_id=3, product_id=4, quantity=7,	order_price=210),
                    models.OrdersDetails(order_id=3, product_id=5, quantity=10,	order_price=5500),                    
                    models.OrdersDetails(order_id=3, product_id=1, quantity=20,	order_price=440)                 
                ]
                 models.db.session.bulk_save_objects(orders_details_to_insert)
                 models.db.session.commit()         
    
            query = models.db.session.query(
    	    routes.OrdersDetails.id, routes.OrdersDetails.order_id, routes.Order.customer_id, 
            routes.OrdersDetails.product_id, routes.Product.product_name, routes.Product.unit_price,                  
            routes.OrdersDetails.quantity, routes.OrdersDetails.order_price, routes.Order.order_date                                                                                     
		    ).join(routes.Product, routes.OrdersDetails.product_id == routes.Product.id) \
 		    .join(routes.Order, routes.OrdersDetails.order_id == routes.Order.id) 

            conn = models.db.engine.raw_connection()
            cursor = conn.cursor()
            sql_query_string = str(query)

            cursor.execute(sql_query_string) 
            rows = cursor.fetchall()             

            orders_list = []  
            if rows:
            # Iterate through each row in the 'rows' list
                for row in rows:
                # Each 'row' is a tuple containing the values for that row
                # You can access elements by index
                    orders_dict = {
                    "id": row[0],
                    "order_id": row[1],
                    "customer_id": row[2],
                    "product_id": row[3],
                    "product_name": row[4],
                    "unit_price": row[5],
                    "quantity": row[6],
                    "order_price": row[7],
                    "order_date": row[8] 
                    }
                    orders_list.append(orders_dict)  
                    #print (orders_list)            
            return render_template('ordermanagement.html', orders_details=orders_list) 
        return data
    else:
        return render_template('ordermanagement.html')    
    
@app.route("/admin_page", methods=['GET', 'POST'])
def admin_page():      
    return redirect(url_for('data_display'))

@app.route('/add_new_order_form/<string:table_name>', methods=['GET', 'POST'])
def add_new_order_form(table_name:str):    
    if request.method == 'POST':
        data = None       
        if table_name == 'orders':           
            data = routes.Product.query.order_by(routes.Product.product_name, routes.Product.id).all()                                                                               
            return render_template('add_new_order.html', results=data)           
    else:
        return render_template('ordermanagement.html') 

@app.route('/update_order_form/<string:table_name>/<int:id>', methods=['GET', 'POST'])
def update_order_form(table_name:str, id:int):  
    if request.method == 'POST':
        data = None       
        if table_name == 'orders':
            order_id = id
                       
            query = '''SELECT orders_details.id, orders_details.order_id, orders.customer_id, orders.region,
                    orders_details.product_id, products.product_name, products.unit_price,                  
                    orders_details.quantity, orders_details.order_price, orders.order_date  
                    FROM orders_details 
                    JOIN products ON orders_details.product_id = products.id
                    JOIN orders ON orders_details.order_id = orders.id
                    WHERE orders.id = ''' + str(order_id)

            conn = models.db.engine.raw_connection()
            cursor = conn.cursor()            
            #print(query)

            cursor.execute(query) 
            rows = cursor.fetchall()  

            orders_list = []  
            if rows:
            # Iterate through each row in the 'rows' list
                for row in rows:
                # Each 'row' is a tuple containing the values for that row
                # You can access elements by index
                    orders_dict = {
                    "id": row[0],
                    "order_id": row[1],
                    "customer_id": row[2],
                    "region": row[3],
                    "product_id": row[4],
                    "product_name": row[5],
                    "unit_price": row[6],
                    "quantity": row[7],
                    "order_price": row[8],
                    "order_date": row[9] 
                    }
                    orders_list.append(orders_dict)  
                    #print (orders_list)   
            products_list = routes.Product.query.order_by(routes.Product.product_name, routes.Product.id).all()          
            return render_template('update_order_form.html', orders=orders_list, products=products_list)                       
    else:
        return render_template('ordermanagement.html')  

@app.route('/delete/<string:table_name>/<int:id>')
def delete(table_name:str, id:int):
    delete_row = None
    if table_name == 'customers':
        delete_row = routes.Customer.query.get_or_404(id) 
    elif table_name == 'products':
        delete_row = routes.Product.query.get_or_404(id)
    elif table_name == 'orders':
        delete_row = routes.Order.query.get_or_404(id)
    elif table_name == 'orders_details':
        delete_row = routes.OrdersDetails.query.get_or_404(id)
    else:
        return redirect("/")
    try:
        models.db.session.delete(delete_row)
        models.db.session.commit()
        flash("Success: Deleted the entry successfully.")         
        return redirect(url_for('admin_page'))   
    except Exception as e:
        return f"Error:{e}"
    
@app.route("/update/<string:table_name>/<int:id>", methods=['GET', 'POST'])
def update(table_name:str, id:int):     
    update_row = None
    table_data = []
    show_section_customers = True
    if table_name == 'customers':
          update_row = routes.Customer.query.get_or_404(id) 
    elif table_name == 'products':
       update_row = routes.Product.query.get_or_404(id)
    elif table_name == 'orders':
        update_row = routes.Order.query.get_or_404(id)
        order_id = id
    """ elif table_name == 'orders_details':
        update_row = routes.OrdersDetails.query.get_or_404(id)  """    

    if request.method == "POST":
        if table_name == 'customers':            
            row = update_row # routes.Customer.query.get(id)
            row.customer_name = request.form['customer_name']
            row.email = request.form['email']
            row.phone_number = request.form['phone_number']
            row.shipping_address = request.form['shipping_address']   
            try:
                models.db.session.commit()
                flash("Success: Updated customer table successfully.")
                return redirect(url_for('admin_page')) 
            except Exception as e:
                return f"ERROR:{e}"
        elif table_name == 'products':            
            row = update_row # routes.Product.query.get(id)
            row.product_name = request.form['product_name']
            row.description = request.form['description']
            row.unit_price = request.form['unit_price']
            row.stock_quantity = request.form['stock_quantity']   
            try:
                models.db.session.commit()
                flash("Success: Updated product table successfully.")
                return redirect(url_for('admin_page')) 
            except Exception as e:
                return f"ERROR:{e}" 
        elif table_name == 'orders':            
            row = update_row # routes.Order.query.get(id)
            customer_id = request.form['customer_id']
            # Check if the field is empty and assign None
            if customer_id == '':
                row.customer_id = None
            else:
                id = customer_id
                # Check if the value is valid 
                customer = routes.Customer.query.get(id)
                if customer:
                    try:
                        row.customer_id = int(customer_id) # Convert to integer
                    except ValueError:
                    # Handle invalid integer input (e.g., flash a message)
                        pass                    
                else:             
                    flash(f'Error: Customer with ID {id} does not exist.', 'error')
                    return redirect("/") 
                
            row.region = request.form['region'] 
            row.order_date = request.form['order_date'] 
            # retrieving dynamic column values from the product table 
            item_values = request.form.getlist('data_item_value[]')
            item_quantities = request.form.getlist('data_item_quantity[]')

            # Combine into a list of dictionaries for easier processing        
            for i in range(len(item_values)):
                table_data.append({
                    'value': item_values[i],
                    'quantity': item_quantities[i]
                })
            #print(table_data)           
            try:
                models.db.session.commit()
                flash("Success: Updated Order table successfully.")
                #return redirect(url_for('admin_page'))  
            except Exception as e:
                return f"ERROR:{e}" 
            
            table_name = 'orders_details'
            # delete and re add the entries into orders_details table  
            try:   
                query = "DELETE FROM orders_details WHERE order_id=" + str(order_id)          

                conn = models.db.engine.raw_connection()
                cursor = conn.cursor() 
                cursor.execute(query) 
                conn.commit()
            except Exception as e:
                print(f"Error: {e}")
                # Rollback changes if an error occurs
                conn.rollback()
            finally:
                # Close the cursor and connection
                if 'cursor' in locals() and cursor:
                    cursor.close()
                if 'conn' in locals() and conn:
                    conn.close()
                     
            # add new entry in order_details table
            for item in table_data:
                product_id_new = item['value']
                quantity_new = item['quantity']
                product = routes.Product.query.get(product_id_new)
                order_price_new = int(quantity_new) * product.unit_price
                new_orders_detail = models.OrdersDetails(order_id=order_id, product_id=product_id_new, quantity=quantity_new, order_price=order_price_new)

                try:
                    models.db.session.add(new_orders_detail)
                    models.db.session.commit()                        
                except Exception as e:
                    return f"ERROR:{e}" 
            flash("Success: Added new order and orders details entries successfully.")               
            return redirect(url_for('admin_page'))        
    else:
        return render_template("ordermanagement.html")    
    
@app.route("/create/<string:table_name>", methods=['POST'])
def create(table_name:str):
    #print(request.form)
    table_data = []
    if table_name == 'customers':         
        customer_name_new = request.form['customer_name']
        email_new = request.form['email']
        phone_number_new = request.form['phone_number']
        shipping_address_new = request.form['shipping_address']
        new_customer = models.Customer(customer_name=customer_name_new, email=email_new, phone_number=phone_number_new, shipping_address=shipping_address_new)
          
    elif table_name == 'products':
        product_name_new = request.form['product_name']
        description_new = request.form['description']
        unit_price_new = request.form['unit_price']
        stock_quantity_new = request.form['stock_quantity']
        new_product = models.Product(product_name=product_name_new, description=description_new, unit_price=unit_price_new, stock_quantity=stock_quantity_new)

    elif table_name == 'orders':       
        id = request.form['customer_id']
        # Check if the value is valid 
        customer = routes.Customer.query.get(id)
        if customer:
            customer_id_new = id
        else:             
            flash(f'Error: Customer with ID {id} does not exist.', 'error')
            return redirect("/")        

        region_new = request.form['region']
        #id = request.form['product_selection_option']

        # retrieving dynamic column values from the product table 
        item_values = request.form.getlist('data_item_value[]')
        item_quantities = request.form.getlist('data_item_quantity[]')

        # Combine into a list of dictionaries for easier processing        
        for i in range(len(item_values)):
            table_data.append({
                'value': item_values[i],
                'quantity': item_quantities[i]
            })
        #print(table_data)
        
        order_date_new = request.form['order_date']              
        new_order = models.Order(customer_id=customer_id_new, region=region_new, order_date=order_date_new)
   
    if request.method == "POST":
        if table_name == 'customers':        
            try:
                models.db.session.add(new_customer)
                models.db.session.commit()
                flash("Success: Added new customer entry successfully.")
                return redirect(url_for('admin_page'))
            except Exception as e:
                return f"ERROR:{e}"   
        elif table_name == 'products':        
            try:
                models.db.session.add(new_product)
                models.db.session.commit()
                flash("Success: Added new product entry successfully.")
                return redirect(url_for('admin_page'))
            except Exception as e:
                return f"ERROR:{e}" 
        elif table_name == 'orders':        
            try:
                models.db.session.add(new_order)
                models.db.session.commit()
                order_id_new = new_order.id

                # add new entry in order_details table
                for item in table_data:
                    product_id_new = item['value']
                    quantity_new = item['quantity']
                    product = routes.Product.query.get(product_id_new)
                    order_price_new = int(quantity_new) * product.unit_price
                    new_orders_detail = models.OrdersDetails(order_id=order_id_new, product_id=product_id_new, quantity=quantity_new, order_price=order_price_new)

                    try:
                        models.db.session.add(new_orders_detail)
                        models.db.session.commit()                        
                    except Exception as e:
                        return f"ERROR:{e}" 
                flash("Success: Added new order and orders details entries successfully.")               
                return redirect(url_for('admin_page'))
            except Exception as e:
                return f"ERROR:{e}"
    else:
        return render_template("ordermanagement.html") 
 
@app.route("/search", methods=['GET', 'POST'])
def search():
    id_input = request.form['id']
    if id_input is not None and id_input != "":
        id_input = int(id_input) 
    else:
        id_input = 0   

    customer_name_input = request.form['customer_name']    
    email_input = request.form['email']
    phone_number_input = request.form['phone_number']
    #shipping_address_input = request.form['shipping_address']
    try:
        rows_count = models.db.session.query(routes.Customer).count()            
        if rows_count == 0: # No existing customers, so perform bulk insert                
                customers_to_insert = [                     
                models.Customer(customer_name='John Smith', email='john.smith@example.com', phone_number='1111111111', shipping_address='123 Main St, Anytown'),
                models.Customer(customer_name='Jane Doe', email='jane.doe@example.com', phone_number='1111111112', shipping_address='456 Elm St, AnotherTown'),
                models.Customer(customer_name='Michael Johnson', email='michael.johnson@example.com', phone_number='1111111113', shipping_address='789 Oak St, Somewhere'),
                models.Customer(customer_name='Emily Wilson', email='emily.wilson@example.com', phone_number='1111111114', shipping_address='567 Pine St, Nowhere'),
                models.Customer(customer_name='David Brown', email='david.brown@example.com', phone_number='1111111115', shipping_address='321 Maple St, Anywhere')
            ]
                models.db.session.bulk_save_objects(customers_to_insert)
                models.db.session.commit()

        # Get a raw database connection from SQLAlchemy's engine
        conn = models.db.engine.raw_connection()
        cursor = conn.cursor()
        
        # call the function get_customers   
        #call_function_script_customers= "SELECT * FROM get_customers({id_input}, {customer_name_input}, {email_input}, {phone_number_input});"
        call_function_script_customers= "SELECT * FROM get_customers(%s, %s, %s, %s);"        
        
        cursor.execute(call_function_script_customers, ((id_input, customer_name_input, email_input, phone_number_input)))    
        rows = cursor.fetchall()  
        customers_list = []  
        if rows:
            # Iterate through each row in the 'rows' list
            for row in rows:
                # Each 'row' is a tuple containing the values for that row
                # You can access elements by index
                customer_dict = {
                "id": row[0],
                "customer_name": row[1],
                "email": row[2],
                "phone_number": row[3],
                "shipping_address": row[4]
                }
                customers_list.append(customer_dict)                 
            
            return render_template('search_results.html', results=customers_list)
        else:
            return jsonify({"message": "User not found"}), 404

    except Exception as e: 
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()   


# Runner and debugger
if __name__ == '__main__':
    app.run(debug=True)  
