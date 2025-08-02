CREATE OR REPLACE FUNCTION search_customers(
p_customer_id INTEGER,
p_customer_name VARCHAR,
p_email VARCHAR,
p_phone_number VARCHAR)
RETURNS TABLE(id INTEGER, customer_name VARCHAR, email VARCHAR, phone_number VARCHAR, shipping_address VARCHAR) AS $$
BEGIN
  IF p_customer_id IS NOT NULL AND p_customer_id > 0 THEN
  RETURN QUERY
  SELECT customers.id, customers.customer_name, customers.email, customers.phone_number, customers.shipping_address
  FROM customers   
  WHERE customers.id = p_customer_id
  ORDER BY customers.id;
ELSEIF (p_customer_name IS NOT NULL AND TRIM(p_customer_name) <> '') AND (p_email IS NOT NULL AND TRIM(p_email) <> '') AND (p_phone_number IS NOT NULL AND TRIM(p_phone_number) <> '') THEN
  RETURN QUERY
  SELECT customers.id, customers.customer_name, customers.email, customers.phone_number, customers.shipping_address
  FROM customers   
  WHERE (customers.customer_name ILIKE '%' || p_customer_name || '%') AND customers.email = p_email AND customers.phone_number = p_phone_number
  ORDER BY customers.id; 
ELSEIF (p_customer_name IS NOT NULL AND TRIM(p_customer_name) <> '') AND (p_email IS NOT NULL AND TRIM(p_email) <> '') THEN
  RETURN QUERY
  SELECT customers.id, customers.customer_name, customers.email, customers.phone_number, customers.shipping_address
  FROM customers   
  WHERE (customers.customer_name ILIKE '%' || p_customer_name || '%') AND customers.email = p_email 
  ORDER BY customers.id;
ELSEIF (p_customer_name IS NOT NULL AND TRIM(p_customer_name) <> '') AND (p_phone_number IS NOT NULL AND TRIM(p_phone_number) <> '') THEN
  RETURN QUERY
  SELECT customers.id, customers.customer_name, customers.email, customers.phone_number, customers.shipping_address
  FROM customers   
  WHERE (customers.customer_name ILIKE '%' || p_customer_name || '%') AND customers.phone_number = p_phone_number
  ORDER BY customers.id;
ELSEIF (p_email IS NOT NULL AND TRIM(p_email) <> '') AND (p_phone_number IS NOT NULL AND TRIM(p_phone_number) <> '') THEN
  RETURN QUERY
  SELECT customers.id, customers.customer_name, customers.email, customers.phone_number, customers.shipping_address
  FROM customers   
  WHERE (customers.email = p_email) AND customers.phone_number = p_phone_number
  ORDER BY customers.id;
ELSEIF p_customer_name IS NOT NULL AND TRIM(p_customer_name) <> '' THEN
  RETURN QUERY
  SELECT customers.id, customers.customer_name, customers.email, customers.phone_number, customers.shipping_address
  FROM customers   
  WHERE customers.customer_name ILIKE '%' || p_customer_name || '%'
  ORDER BY customers.id; 
ELSEIF p_email IS NOT NULL AND TRIM(p_email) <> '' THEN
  RETURN QUERY
  SELECT customers.id, customers.customer_name, customers.email, customers.phone_number, customers.shipping_address
  FROM customers   
  WHERE customers.email = p_email
  ORDER BY customers.id;
ELSEIF p_phone_number IS NOT NULL AND TRIM(p_phone_number) <> '' THEN
  RETURN QUERY
  SELECT customers.id, customers.customer_name, customers.email, customers.phone_number, customers.shipping_address
  FROM customers   
  WHERE customers.p_phone_number = p_phone_number
  ORDER BY customers.id;
ELSE
   RETURN QUERY
   SELECT customers.id, customers.customer_name, customers.email, customers.phone_number, customers.shipping_address
   FROM customers
   ORDER BY customers.id;
 END IF;

END;
$$ LANGUAGE plpgsql;
