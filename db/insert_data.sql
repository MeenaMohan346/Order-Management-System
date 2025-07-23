INSERT INTO customers (customer_name, email, phone_number, shipping_address)
	VALUES
	('John Smith', 'john.smith@example.com', '1111111111', '123 Main St, Anytown'),
	('Jane Doe', 'jane.doe@example.com', '1111111112', '456 Elm St, AnotherTown'),
	('Michael Johnson', 'michael.johnson@example.com', '1111111113', '789 Oak St, Somewhere'),
	('Emily Wilson', 'emily.wilson@example.com', '1111111114', '567 Pine St, Nowhere'),
	('David Brown', 'david.brown@example.com', '1111111115', '321 Maple St, Anywhere');

INSERT INTO products(product_name, description, unit_price, stock_quantity)
VALUES
('T-Shirt',	'Comfortable cotton T-shirt.',	25,	200),
('Headphones',	'Noise-canceling headphones for immersive audio',	150,	75),
('Jeans',	'Classic denim jeans'	,50,	150),
('Mouse',	'Ergonomic wireless mouse',	30,	100),
('Stove',	'Gas stove top',	550,	100);

INSERT INTO orders (customer_id,region,order_date)
	VALUES
(1,	"TX",	"2025-07-23"),
(2,	"FL",	"2025-07-23"),
(5,	"NC",	"2025-07-23");

INSERT INTO orders_details (order_id, product_id, quantity, order_price)
		VALUES
	(1,	3,	5,	250),
	(1,	6,	10,	5500),
	(1,	1,	15,	330),
	(2,	2,	5,	750),
	(2,	1,	7,	154),
	(3,	3,	2,	100),
	(3,	4,	7,	210),
	(3,	6,	10,	5500),
	(3,	1,	20,	440);
