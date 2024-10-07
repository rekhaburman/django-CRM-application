import mysql.connector

# Database connection parameters
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Rekha@#123'
}

try:
  
    dataBase = mysql.connector.connect(**db_config)
   
    cursorObject = dataBase.cursor()
    
    
    cursorObject.execute("SHOW DATABASES LIKE 'supertest';")
    database_exists = cursorObject.fetchone()
    
    
    if not database_exists:
        cursorObject.execute("CREATE DATABASE supertest;")
        print("Database 'supertest' created successfully!")
    else:
        print("Database 'supertest' already exists.")
    
    
    dataBase.commit()
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
   
    cursorObject.close()
    dataBase.close()


print("All operations completed successfully!")
