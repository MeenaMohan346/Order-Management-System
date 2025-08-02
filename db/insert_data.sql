INSERT INTO customers (customer_name, email, phone_number, shipping_address)
	VALUES
	('John Smith', 'john.smith@example.com', '1111111111', '123 Main St, Anytown'),
	('Jane Doe', 'jane.doe@example.com', '1111111112', '456 Elm St, AnotherTown'),
	('Michael Johnson', 'michael.johnson@example.com', '1111111113', '789 Oak St, Somewhere'),
	('Emily Wilson', 'emily.wilson@example.com', '1111111114', '567 Pine St, Nowhere'),
	('David Brown', 'david.brown@example.com', '1111111115', '321 Maple St, Anywhere');

INSERT INTO products (product_name, description, image_url, unit_price, stock_quantity)
VALUES ('Chutney',	'Indian powders side dish for dosa.',	'/static/images/chutney_powders.png', 5,	200),
('Dals',	'Indian Dals for making curry', '/static/images/dals.png',  15,	75),
('Tea',	'Indian Tata Tea Powder', '/static/images/indian_tea.png', 19,	150),
('Masala',	'Indian Masala Powders (Spicy)',	'/static/images/masala_powders.png', 12,	100),
('Noodles',	'Millet Noodles (Sun-Dried)', '/static/images/millet_noodles.png', 	10,	50),
('Snacks',	'Indian Snacks', '/static/images/snacks.png', 	14,	10),
('Sweets',	'Indian Sweets', '/static/images/sweets.png', 	27,	150),
('Pancake',	'Millet Pancake Waffle Mix', '/static/images/pancake.png', 	11,	100);

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
