import requests
import psycopg2

# Database connection details
DB_HOST = "test-db.cz2um0ac6a4b.us-east-1.rds.amazonaws.com"
DB_NAME = "test-db"
DB_USER = "postgres"
DB_PASSWORD = "Postgres"

# API endpoint
API_URL = "https://jsonplaceholder.typicode.com/comments"

def fetch_data_from_api():
    try:
        print("Fetching data from API...")
        response = requests.get(API_URL)
        response.raise_for_status()
        print("Data fetched successfully!")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return []

def connect_to_database():
    try:
        print("Connecting to the database...")
        connection = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        print("Connection to the database successful!")
        return connection
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def create_table(connection):
    try:
        print("Checking/Creating the table 'comments'...")
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS comments (
                    id SERIAL PRIMARY KEY,
                    post_id INT,
                    name VARCHAR(255),
                    email VARCHAR(255),
                    body TEXT
                );
            """)
            connection.commit()
            print("Table 'comments' is ready!")
    except psycopg2.Error as e:
        print(f"Error creating table: {e}")

def insert_data_into_table(connection, data):
    try:
        print("Inserting data into the 'comments' table...")
        with connection.cursor() as cursor:
            for item in data:
                cursor.execute("""
                    INSERT INTO comments (post_id, name, email, body)
                    VALUES (%s, %s, %s, %s);
                """, (item["postId"], item["name"], item["email"], item["body"]))
            connection.commit()
            print("Data inserted successfully!")
    except psycopg2.Error as e:
        print(f"Error inserting data into the table: {e}")

def main():
    data = fetch_data_from_api()
    if not data:
        print("No data fetched from the API. Exiting...")
        return

    connection = connect_to_database()
    if connection is None:
        print("Database connection failed. Exiting...")
        return

    try:
        create_table(connection)
        insert_data_into_table(connection, data)
    finally:
        print("Closing database connection...")
        connection.close()

if __name__ == "__main__":
    main()

