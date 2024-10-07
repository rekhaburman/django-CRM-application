import mysql.connector

# Database connection parameters
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Rekha@#123'
}

try:
    # Establish a connection to the MySQL server
    dataBase = mysql.connector.connect(**db_config)
    
    # Prepare a cursor object
    cursorObject = dataBase.cursor()
    
    # Check if the database exists
    cursorObject.execute("SHOW DATABASES LIKE 'supertest';")
    database_exists = cursorObject.fetchone()
    
    # Create the database if it does not exist
    if not database_exists:
        cursorObject.execute("CREATE DATABASE supertest;")
        print("Database 'supertest' created successfully!")
    else:
        print("Database 'supertest' already exists.")
    
    # Commit the transaction (optional for creating a database)
    dataBase.commit()
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Close the cursor and connection
    cursorObject.close()
    dataBase.close()

print("All operations completed successfully!")
