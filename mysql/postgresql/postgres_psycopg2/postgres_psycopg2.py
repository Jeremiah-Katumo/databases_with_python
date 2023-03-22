import psycopg2
from sqlalchemy import create_engine


def insert_sales(conn, order_num, order_type, cust_name, prod_number, prod_name,
                 quantity, price, discount, order_total):
    order_total = quantity * price
    if discount != 0:
        order_total = order_total * discount

    sale_data = (order_num, order_type, cust_name, prod_number, prod_name, 
                 quantity, price, discount, order_total)

    cursor = conn.cursor()
    cursor.execute('''DELETE FROM sales WHERE order_num=1105910''' )

    cursor.execute('''INSERT INTO sales (order_num, order_type, cust_name, prod_number, prod_name,
    quantity, price, discount, order_total) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)''', sale_data)
    conn.commit()

    cursor.execute('''SELECT * FROM sales WHERE order_num=%s;''', (order_num,))

    rows = cursor.fetchall()
    for row in rows:
        print("CUST_NAME = ", row[0])
        print("ORDER_TOTAL = ", row[1], "\n")



if __name__ ==  '__main__':
    ####engine = create_engine('postgresql+psycopg2://postgres:password@localhost:5432/red_army') #% quote('Mysql.003'))

    conn = psycopg2.connect(database="red_army",
                            user="postgres",
                            password="Postgres.003",
                            host="localhost",
                            port="5432")
    
    order_num = int(input("What is the order number?\n"))
    order_type = input("What is the order type: Retail or Wholesale?\n")
    cust_name = input("What is the customer's name?\n")
    prod_number = input("What is the product number?\n")
    prod_name = input("What is the product name?\n")
    quantity = float(input("What was the quantity bought?\n"))
    price = float(input("What is the price of the product?\n"))
    discount = float(input("What is the discount of the product, if there is one?\n"))
    order_total = float(input("What is the order total?\n"))
    
    insert_sales(conn, order_num, order_type, cust_name, prod_number, prod_name,
                 quantity, price, discount, order_total)

    print("Data Successfully Inserted!")

    conn.close()

