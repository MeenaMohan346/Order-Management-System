
var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.6.3.min.js'; // Check https://jquery.com/ for the current version
document.getElementsByTagName('head')[0].appendChild(script);

var script = document.createElement('script');
script.src = src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"; 
document.getElementsByTagName('head')[0].appendChild(script);

 function openEditModal(table_name, id) {  
    if (table_name == "customers") {
        fetch(`/update/customers/${id}`, { method: 'POST',
            headers: { 'Content-Type': 'application/json' }},)
            .then(response => response.json())
            .then(data => {    

        document.getElementById('editId').value = id;
        document.getElementById('editCustomername').value = 'customer_name';  
        document.getElementById('ediEmail').value = 'email'; 
        document.getElementById('editPhonenumber').value = 'phone_number'; 
        document.getElementById('editShippingaddress').value = 'shipping_address';    
        document.getElementById('editModal'+ id).style.display = "none";
        });

    } else if (table_name == "products") {
        fetch(`/update/products/${id}`, { method: 'POST',
            headers: { 'Content-Type': 'application/json' }},)
            .then(response => response.json())
            .then(data => {    

        document.getElementById('editId').value = id;
        document.getElementById('editProductname').value = 'product_name';  
        document.getElementById('editDescription').value = 'description'; 
        document.getElementById('editUnitprice').value = 'unit_price'; 
        document.getElementById('editStockquantity').value = 'stock_quantity';     
        document.getElementById('editModal'+id).style.display = "none";
        });

    } else if (table_name == "orders") {
        fetch(`/update/orders/${id}`, { method: 'POST',
            headers: { 'Content-Type': 'application/json' }},)
            .then(response => response.json())
            .then(data => {    

        document.getElementById('editId').value = id;
        document.getElementById('editcustomerid').value = 'customer_id';  
        document.getElementById('editRegion').value = 'region'; 
        document.getElementById('editProductid').value = 'product_id'; 
        document.getElementById('editOrderdate').value = 'order_date'; 
        document.getElementById('editQuantity').value = 'quantity'; 
        document.getElementById('editAmount').value = 'amount';    
        document.getElementById('editModal'+id).style.display = "none";
        });

    } else if (table_name == "orders_details") {
        fetch(`/update/customers/${id}`, { method: 'POST',
            headers: { 'Content-Type': 'application/json' }},)
            .then(response => response.json())
            .then(data => {    

        document.getElementById('editId').value = id;
        document.getElementById('editOrderid').value = 'order_id';  
        document.getElementById('editProductid').value = 'product_id'; 
        document.getElementById('editQty').value = 'qty'; 
        document.getElementById('editOrderprice').value = 'order_price';   
        document.getElementById('editModal'+id).style.display = "none";
        });

    }        

     /* $("#editModal").modal('show'); */
      $("#editModal"+id).modal('show');
}

function closeEditModal() {
    document.getElementById('editModal'+id).style.display = "none";
}

 window.onclick = function(event) {
    if (event.target == document.getElementById('editModal'+id)) {
        document.getElementById('editModal'+id).style.display = "none";
    }
} 

document.getElementById(table_name, 'editForm').addEventListener('submit', function(event) {
    event.preventDefault();
    if (table_name == 'customers') {
        const id = document.getElementById('editId').value;
        const customer_name = document.getElementById('editCustomername').value;
        const email = document.getElementById('editEmail').value;
        const phone_number = document.getElementById('editPhonenumber').value;
        const shipping_address = document.getElementById('editShippingaddress').value;
        fetch(`/update/customers/${id}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id:id, customer_name:customer_name, email: email, phone_number:phone_number, shipping_address:shipping_address })
        })
        .then(response => {
            if (response.ok) {
                closeEditModal();
                // Reload the table or update the specific row
                location.reload();
            } else {
                // Handle error
            }
        });
    } else if (table_name == 'products') {
        const id = document.getElementById('editId').value;
        const product_name = document.getElementById('editProductname').value;
        const description = document.getElementById('editDescription').value;
        const unit_price = document.getElementById('editUnitprice').value;
        const stock_quantity = document.getElementById('editStockquantity').value;
        fetch(`/update/products/${id}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id:id, product_name:product_name, description: description, unit_price:unit_price, stock_quantity:stock_quantity })
        })
        .then(response => {
            if (response.ok) {
                closeEditModal();
                // Reload the table or update the specific row
                location.reload();
            } else {
                // Handle error
            }
        });
    } else if (table_name == 'orders') {
        const id = document.getElementById('editId').value;
        const customer_id = document.getElementById('editcustomerid').value;
        const region = document.getElementById('editRegion').value;
        const product_id = document.getElementById('editProductid').value;
        const order_date = document.getElementById('editOrderdate').value;
        const quantity = document.getElementById('editQuantity').value;
        const amount = document.getElementById('editAmount').value;
        fetch(`/update/orders/${id}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id:id, customer_id:customer_id, region: region, product_id:product_id, order_date:order_date, quantity:quantity, amount:amount })
        })
        .then(response => {
            if (response.ok) {
                closeEditModal();
                // Reload the table or update the specific row
                location.reload();
            } else {
                // Handle error
            }
        });
    } else if (table_name == 'orders_details') {
        const id = document.getElementById('editId').value;
        const order_id = document.getElementById('editOrderid').value;
        const product_id = document.getElementById('editProductid').value;
        const qty = document.getElementById('editQty').value;
        const order_price = document.getElementById('editOrderprice').value;
        fetch(`/update/orders_details/${id}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id:id, order_id:order_id, product_id: product_id, qty:qty, order_price:order_price })
        })
        .then(response => {
            if (response.ok) {
                closeEditModal();
                // Reload the table or update the specific row
                location.reload();
            } else {
                // Handle error
            }
        });
    }
    
});

