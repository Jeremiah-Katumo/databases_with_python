import psycopg2

conn = psycopg2.connect(dbname="red_army",
                 user="postgres",
                 password="Postgres.003",
                 host="localhost",
                 port="5432")

cursor = conn.cursor()

cursor.execute('''CREATE TABLE Sales 
(ORDER_NUM INT PRIMARY KEY,
ORDER_TYPE TEXT,
CUST_NAME TEXT,
PROD_NUMBER TEXT,
PROD_NAME TEXT,
QUANTITY INT,
PRICE REAL,
DISCOUNT REAL,
ORDER_TOTAL REAL);''')

conn.commit()
conn.close()
