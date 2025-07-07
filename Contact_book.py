import mysql.connector # Library helps to connect to MySQl Server

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="db_password",
        database="contact_book"
    )

def add_contact():
    db = connect_db() # Allows Connection to MySQL Server
    cursor = db.cursor() # Tool to execute SQL queries & fetch results

    name = input("Enter Contact Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email (optional): ")

    sql = "INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)" 
    values = (name, phone, email)

    try:
        cursor.execute(sql, values) # Sends the SQL query to MySQL and executes it.
        db.commit() # Saves the changes 
        print(" Contact Added Successfully!")
    except Exception as e:
        print(" Error while adding contact:", e)
        db.rollback() # Cancel the changes

    cursor.close() # Closes the cursor Object
    db.close() # Closes the connection 

def view_all_contacts():
    db = connect_db()
    cursor = db.cursor()

    sql = "SELECT * FROM contacts"

    try:
        cursor.execute(sql)
        results = cursor.fetchall()

        print("\n--- Contact List ---")
        if results:
            for row in results:
                print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]} | Email: {row[3]}")
        else:
            print(" No contacts found.")
    except Exception as e:
        print(" Error fetching contacts:", e)

    cursor.close()
    db.close()

# Show all contacts immediately at start
view_all_contacts()

# Main Menu Loop
while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_all_contacts()
    elif choice == '3':
        print("Exiting... Bye!")
        break
    else:
        print("Invalid choice. Please enter 1-3.")
