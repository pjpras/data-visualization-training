import mysql.connector as my
from faker import Faker
import random
import uuid
from datetime import datetime

# Initialize Faker instance
faker = Faker()

# Connect to the MySQL database
con = my.connect(
    host='localhost',
    user='root',
    password='mariam',
    database='ecommerce'
)

cr = con.cursor()

# Insert 1000 random customers
for _ in range(1000):
    customer_id = str(uuid.uuid4())[:10]  # Generate a unique 10-character customer_id
    name = faker.name()
    city = faker.city()
    email = faker.email()
    phone_no = faker.phone_number()[:14]  # Limit phone number to 15 characters
    address = faker.address().replace("\n", " ")
    pin_code = faker.zipcode()
    
    cr.execute('''
        INSERT INTO customer (customer_id, name, city, email, phone_no, address, pin_code)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    ''', (customer_id, name, city, email, phone_no, address, pin_code))

# Insert 1000 random products
for _ in range(1000):
    product_id = str(uuid.uuid4())[:10]  # Generate a unique 10-character product_id
    product_name = faker.word().capitalize()
    category = random.choice(['Electronics', 'Clothing', 'Home', 'Beauty', 'Sports'])
    sub_category = random.choice(['Mobile', 'Laptop', 'Shirt', 'Sofa', 'Makeup', 'Football'])
    original_price = round(random.uniform(10.0, 500.0), 2)
    selling_price = round(original_price * random.uniform(0.8, 1.2), 2)
    stock = random.randint(10, 500)
    
    cr.execute('''
        INSERT INTO product (product_id, product_name, category, sub_category, original_price, selling_price, stock)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    ''', (product_id, product_name, category, sub_category, original_price, selling_price, stock))

# Insert 1000 random orders
for _ in range(1000):
    order_id = None  # Let MySQL auto-increment the order_id
    cr.execute('SELECT customer_id FROM customer ORDER BY RAND() LIMIT 1')
    customer_id = cr.fetchone()[0]
    
    cr.execute('SELECT product_id FROM product ORDER BY RAND() LIMIT 1')
    product_id = cr.fetchone()[0]
    
    quantity = round(random.uniform(1, 10), 2)
    total_price = round(quantity * random.uniform(10.0, 500.0), 2)
    payment_mode = random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer', 'Cash on Delivery'])
    order_date = faker.date_time_this_year(before_now=True, after_now=False).strftime('%Y-%m-%d %H:%M:%S')
    order_status = random.choice(['Pending', 'Shipped', 'Delivered', 'Cancelled'])
    
    cr.execute('''
        INSERT INTO order_details (customer_id, product_id, quantity, total_price, payment_mode, order_date, order_status)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    ''', (customer_id, product_id, quantity, total_price, payment_mode, order_date, order_status))

# Commit the transaction
con.commit()

# Close the cursor and connection
cr.close()
con.close()

print("Inserted 1000 random rows into customer, product, and order_details tables.")
