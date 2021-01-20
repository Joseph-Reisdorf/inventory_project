import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    # command to start a database in db_file
    # python -c "from __name__ import *; create_connection('db_folder/inventory.db')"

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_table(db_file):
    # run with file path to db file to set up the inventory table in db_file
    # python -c "from __name__ import *; create_table('./db_folder/inventory.db')"

    c = sqlite3.connect(db_file)

    cursor = c.cursor()
    cursor.execute("""CREATE TABLE inventory (
        
        name text,
        type text,
        brand text,
        amount integer

        )""")

    c.commit()
    c.close()



#def add_item(database, name, product_type, brand, amount):
#    c = sqlite3.connect(database)
#    cursor = c.cursor()
#
#    c.execute("INSERT INTO inventory VALUES (?, ?, ?, ?)", (name, product_type, brand, amount))
#    c.commit()
#    c.close()

# def remove_item():

#def add_inventory():

#def remove_inventory():
    

    
if __name__ == '__main__':

    # Item name, product type, brand, amount
    # Mocha, frappe powder, coffee house, 4

    path = 'db_folder/inventory.db'
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    print("\nYou are now connected to your inventory database.")

   

    # keyboard loop to operate on inventory
    keyboard = ""
    while (keyboard != "STOP"):
        cursor.execute(input() + " into inventory values (?, ?, ?, ?)", (input(), input(), input(), input()))

        keyboard = input("Operation completed. Type \"STOP\" to end or enter to continue") 


    # print table
    cursor.execute("SELECT * FROM inventory")
    print(cursor.fetchall())

    # close file
    conn.commit()
    conn.close()
    print("Database disconnected.")

    
