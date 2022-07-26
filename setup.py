import sqlite3;

# == SQLITE DATATYPE(5) ==
# 1. NULL
# 2. INTEGER
# 3. REAL
# 4. TEXT
# 5. BLOB

# == connect to database ==
conn = sqlite3.connect('customer.db')

# == create a cursor ==
cursor = conn.cursor()

# == create a table ==
# cursor.execute("""CREATE TABLE customers (
#     first_name text,
#     last_name text,
#     email text
# )""")

# == INSERT one record INTO the table ==
# cursor.execute("INSERT INTO customers VALUES('idris', 'yakub', 'olayinkayakub@yahoo.com')")

# == INSERT many record INTO the table ==
# many_customers = [
#     ('idris', 'yakub', 'olayinka@yahoo.com'),
#     ('quam', 'yakub', 'quam@yahoo.com'),
#     ('fatiha', 'yakub', 'fatiha@yahoo.com')
#     ]
# cursor.executemany("INSERT INTO customers VALUES(?,?,?)", many_customers)

# == query the database ==
# cursor.execute("SELECT rowid, * FROM customers")

# == fetch from database ==
# print(cursor.fetchone())
# print(cursor.fetchmany(3))
# items = cursor.fetchall()

# == formating table ==
# for item in items:
    # print(item[0], " || " + item[1] + " || " + item[2] + " || " + item[3])

# == WHERE clause ==
# cursor.execute("SELECT * FROM customers WHERE first_name = 'quam'")
# items = cursor.fetchall()
# for item in items:
#     print(item)

# == WHERE LIKE clause ==
# cursor.execute("SELECT * FROM customers WHERE email LIKE 'ola%' ")
# or
# cursor.execute("SELECT * FROM customers WHERE email LIKE '%yahoo.com' ")
# or
# cursor.execute("SELECT * FROM customers WHERE email LIKE '%yakub%' ")
# items = cursor.fetchall()
# for item in items:
#     print(item)

# == UPDATE records ==
# cursor.execute("UPDATE customers SET email = 'folakeyakub@yahoo.com' WHERE first_name = 'fatiha'")

# == DELETE records ==
# cursor.execute("DELETE customers SET email = 'folakeyakub@yahoo.com' WHERE rowid = 1")

# query the database - ORDER BY
# cursor.execute("SELECT rowid, * FROM customers ORDER BY first_name DESC")

#query the database - AND/OR
# cursor.execute("SELECT rowid, * FROM customers WHERE first_name LIKE '%a%' AND rowid=2")

# LIMIT
# cursor.execute("SELECT rowid, * FROM customers LIMIT 3")

# DROP TABLE
# cursor.execute("DROP TABLE customers")


# commit our command
# conn.commit()

# close our connection
# conn.close()