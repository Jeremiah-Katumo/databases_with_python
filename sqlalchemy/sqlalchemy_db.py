import sqlalchemy as db

engine = db.create_engine('sqlite:///movies1.db') # connect with the database

connection = engine.connect()   # create a connection object

metadata = db.MetaData()        # Retrieve the metadata. It holds all info about our table

# Load the movies table into sqlalchemy
movies = db.Table('movies1', metadata, autoload=True, autoload_with=engine)

query = db.select([movies])     # set queries for execution with the connection object

result_proxy = connection.execute(query)  # proxies the cursor object from Python Database API
# You can use the result_proxy to retrieve the data
result_set = result_proxy.fetchall()      # retrieve the data

print(result_set[0])
print(result_set[:2])

query = db.select([movies]).where(movies.columns.Director == "Mac Winfield")

result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()

print(result_set[0])

#  Insert into table
query = movies.insert().values(Title='Psycho', Director='Alfred Hitchcock', Year=1960)

connection.execute(query)

query = db.select([movies])

result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()

print(result_set)
