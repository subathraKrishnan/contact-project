import sqlite3

def default_contact():
    db = sqlite3.connect("contacts.sqlite")
    db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email_address TEXT)")
    db.execute("INSERT INTO contacts (name, phone, email_address) VALUES ('Laura', 6578923 , 'laura@gmail.com')")
    db.execute("INSERT INTO contacts (name, phone, email_address) VALUES ('Grace', 6593745 , 'grace@hotmail.com')")
    db.execute("INSERT INTO contacts (name, phone, email_address) VALUES ('Sam' , 6569547 , 'sam@yahoo.com')")
    db.execute("INSERT INTO contacts (name, phone, email_address) VALUES ('Daniel' , 6526310 , 'daniel@gmail.com')")
    db.commit()

def print_contact():
    db = sqlite3.connect("contacts.sqlite")
    for row in db.execute("SELECT * FROM contacts "):
        print(row)
    db.close()

def add_contact(x,y,z):
    db = sqlite3.connect("contacts.sqlite")
    insert_query = "INSERT INTO contacts(name, phone, email_address) VALUES (?, ?, ?)"
    select_cursor = db.cursor()
    select_cursor.execute(insert_query,(x,y,z))
    print(f"{select_cursor.rowcount} rows added")
    db.commit()
    select_cursor.close()
    db.close()

def delete_contact(x):
    db = sqlite3.connect("contacts.sqlite")
    select_sql = "DELETE FROM contacts WHERE name = ?"
    select_cursor = db.cursor()
    select_cursor.execute(select_sql,(x,))
    print(x, "deleted from contact list")
    db.commit()
    select_cursor.close()
    db.close()
   
def update_contact(x,y,z):
    db = sqlite3.connect("contacts.sqlite")
    update_sql = f"UPDATE contacts SET phone = ?, email_address = ? WHERE contacts.name = ?"
    update_cursor = db.cursor()
    update_cursor.execute(update_sql,(y,z,x))
    print(f"{update_cursor.rowcount} rows updated") 
    db.commit()
    update_cursor.close()
    db.close()

def search_contact(x):
    db = sqlite3.connect("contacts.sqlite")
    select_cursor = db.cursor()
    select_cursor.execute('SELECT * FROM contacts')
    data=select_cursor.fetchall()
    y = 'not found'
    for row in data:
        if row[0] == x:
            y = 'found'
            print(row[0], row[1], row[2])
            break
    if y == 'not found':  
        print("contact not found")
    select_cursor.close()
    db.close()


action = input("Please choose an option: (1-ADD, 2-DELETE, 3-UPDATE, 4-SEARCH, 5-VIEW ALL) ")
match action:
    case "0":
        print(default_contact())
    case "1":
        name = input("Enter the name: ")
        phone = input("Enter the phone: ")
        email_address = input("Enter the email_address: ")
        print(add_contact(name, phone, email_address))
    case "2":
        name = input("Please enter the name of the contact to be deleted: ")
        print(delete_contact(name))
    case "3":
        name = input("Please enter the name of the contact to be updated: ")
        new_phone = input("Please enter new phone number: ")
        new_email_address = input("Please enter new_email_address: ")
        print(update_contact(name, new_phone, new_email_address))
    case "4":
        name = input("Please enter the name of the contact to search: ")
        print(search_contact(name))
    case "5":
        print(print_contact())
    case _:
        print("Option not valid")

