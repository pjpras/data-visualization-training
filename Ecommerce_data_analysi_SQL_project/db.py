import mysql.connector as my

try:
    # Establishing connection
    con = my.connect(
        host='localhost',
        user='root',
        password='mariam'
    )
    
    # Creating a cursor object
    cr = con.cursor()

    # Creating the 'ecommerce' database
    cr.execute('CREATE DATABASE IF NOT EXISTS ecommerce')

    # Selecting the database
    cr.execute('USE ecommerce')

    # Creating the 'customer' table
    cr.execute('''
    CREATE TABLE IF NOT EXISTS `customer` (
        `customer_id` varchar(10) NOT NULL,
        `name` varchar(100) NOT NULL,
        `city` varchar(65) NOT NULL,
        `email` varchar(45) NOT NULL,
        `phone_no` varchar(15) NOT NULL,
        `address` varchar(100) NOT NULL,
        `pin_code` int NOT NULL,
        PRIMARY KEY (`customer_id`)
    );
    ''')

    # Creating the 'product' table
    cr.execute('''
    CREATE TABLE IF NOT EXISTS `product` (
        `product_id` varchar(10) NOT NULL,
        `product_name` varchar(100) NOT NULL,
        `category` varchar(65) NOT NULL,
        `sub_category` varchar(45) NOT NULL,
        `original_price` double NOT NULL,
        `selling_price` double NOT NULL,
        `stock` int NOT NULL,
        PRIMARY KEY (`product_id`)
    );
    ''')

    # Creating the 'order_details' table
    cr.execute('''
    CREATE TABLE IF NOT EXISTS `order_details` (
        `order_id` int NOT NULL AUTO_INCREMENT,
        `customer_id` varchar(10) NOT NULL,
        `product_id` varchar(10) NOT NULL,
        `quantity` double NOT NULL,
        `total_price` double NOT NULL,
        `payment_mode` varchar(60) NOT NULL,
        `order_date` datetime DEFAULT NULL,
        `order_status` varchar(20) NOT NULL,
        PRIMARY KEY (`order_id`),
        KEY `customer_id` (`customer_id`),
        KEY `product_id` (`product_id`),
        CONSTRAINT `order_details_ibfk_1` FOREIGN KEY (`customer_id`)
        REFERENCES `customer` (`customer_id`),
        CONSTRAINT `order_details_ibfk_2` FOREIGN KEY (`product_id`)
        REFERENCES `product` (`product_id`)
    );
    ''')

    # Committing the transaction
    con.commit()
    print('Database and tables created successfully.')

except my.Error as e:
    print(f"Error: {e}")

finally:
    # Closing the connection
    if con.is_connected():
        cr.close()
        con.close()
        print('MySQL connection is closed.')
