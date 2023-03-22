import psycopg2
from urllib.parse import quote  
from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData


engine = create_engine('postgresql+psycopg2://postgres:password@localhost:5432/red_army')# % quote('Mysql.003'))

with engine.connect() as connection:
    metadata = MetaData(engine)
    sales_table = Table('sales', metadata, autoload=True, autoload_with=engine)

    delete_record = sales_table.delete().where(sales_table.c.order_num==1105910)
    connection.execute(delete_record)

    # Create
    insert_statement = sales_table.insert().values(order_num=1105910,
                                                   order_type='Retail',
                                                   cust_name='Almond Raymond',
                                                   prod_number='A11223F',
                                                   prod_name='Practical NLP',
                                                   quantity=5,
                                                   price=200,
                                                   discount=0,
                                                   order_total=1000)
    connection.execute(insert_statement)

    # Read 
    select_statement = sales_table.select().limit(10)
    results = connection.execute(select_statement)
    for r in results:
        print(r)

    # Update 
    update_satement = sales_table.update().where(sales_table.c.order_num==1105910).values(quantity=8, order_total=1600)
    connection.execute(update_satement)

    # Confirm Update: Read
    reselect_statement = sales_table.select().where(sales_table.c.order_num==1105910)
    updated_set = connection.execute(reselect_statement)
    for u in updated_set:
        print(u)

    # Delete
    delete_statement = sales_table.delete().where(sales_table.c.order_num==1105910)
    connection.execute(delete_statement)

    # Confirm Delete: Read
    not_found_field = connection.execute(reselect_statement)
    print(not_found_field.rowcount)
