import sqlite3;

# == Query the db and return all records ==
def show_all():
    # connect to database
    conn = sqlite3.connect('customer.db')
    # create a cursor
    cursor = conn.cursor()

    # query the db
    cursor.execute("SELECT rowid, * FROM customers")
    
    items =cursor.fetchall()
    for item in items:
        print(item)

    # commit our command
    conn.commit()

    # close our connection
    conn.close()

# == Add a new record to the table ==
def add_one(first, last, email):
    # connect to database
    conn = sqlite3.connect('customer.db')
    # create a cursor
    cursor = conn.cursor()

    # INSERT
    cursor.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))

    # commit our command
    conn.commit()

    # close our connection
    conn.close()

# == Add many new records to the table ==
def add_many(list):
    # connect to database
    conn = sqlite3.connect('customer.db')
    # create a cursor
    cursor = conn.cursor()

    # INSERT
    cursor.executemany("INSERT INTO customers VALUES (?,?,?)", (list))

    # commit our command
    conn.commit()

    # close our connection
    conn.close()

# == Delete record from table ==
def delete_one(id):
    # connect to database
    conn = sqlite3.connect('customer.db')
    # create a cursor
    cursor = conn.cursor()

    # query the db
    cursor.execute("DELETE FROM customers WHERE rowid =(?)", id)

    # commit our command
    conn.commit()

    # close our connection
    conn.close()