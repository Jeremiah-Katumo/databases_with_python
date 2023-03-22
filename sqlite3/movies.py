import sqlite3

connection = sqlite3.connect('movies1.db') # connect with a database
cursor = connection.cursor()              # grab a cursor to create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS movies1
    (Title TEXT, Director TEXT, Year INT)''') # create table


# Add data to the created database
# Avoid duplication of fields by writing the line as a comment
cursor.execute("INSERT INTO Movies1 VALUES ('Matatu driver', 'Matoo Sussex', 1976)")
# cursor.execute("SELECT * FROM Movies")

films = [('Emancipation', 'Wes Anderson', 2022),
        ('Entergalactic', 'Mac Winfield', 2022),
        ('Nobody', 'Allister Brown', 2021)]

# This code will look at each tuple and run the insertion for each tuple
cursor.executemany('INSERT INTO movies1 VALUES (?,?,?)', films)

records = cursor.execute("SELECT * FROM movies1")

# print(cursor.fetchone())
print(cursor.fetchall())

for record in records:
    print(record)


# Filtering in a database
release_year = (2022, )
cursor.execute('SELECT * FROM movies1 WHERE Year=?', release_year)

print(cursor.fetchall())

connection.commit() # commit the changes made
connection.close()
