from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql+psycopg://postgres:password@localhost/red_army')
Base = declarative_base(engine)
Base.metadata.reflect(engine) # communicate  with database and reflect everything in it

class Sales(Base):
    __table__ = Base.metadata.tables['sales']

    def __repr__(self):
        return '''<Sale(order_num='{0}', order_type='{1}', cust_name='{2}', prod_name='{3}', quantity='{4}', 
        order_total='{5}')'''.format(self.order_num, self.order_type, self.cust_name, self.prod_name,
        self.quantity, self.order_total)

    def LoadSession():
        Session = sessionmaker(bind=engine)
        session = Session()

    if __name__ == "__main__":
        session = LoadSession()

        # Read
        smallest_sales = sales.query(Sales).order_by(Sales.order_total).limit(10)
        print(smallest_sales[0].cust_name)

        # Insert
        recent_sale = Sales(order_num=1105910, order_type='Retail', cust_name='Almond Raymond', 
                            prod_name='Practical NLP', quantity=15, order_total=3000)
        print(recent_sale)
        session.add(recent_sale)
        session.commit()

        # Update
        recent_sale.quantity = 15
        recent_sale.order_total = 3000
        session.commit()
        updated_sale = session.query(Sales).filter(Sales.order_num==1105910).first()
        print(updated_sale)

        # Delete 
        returned_sale = session.query(Sales).filter(Sales.order_num==1105010).first()
        session.delete(returned_sale)
        session.commit()

        session.commit()
