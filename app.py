import psycopg2
import os

def read_secret(secret_name):
    secret_path = f"/run/secrets/{secret_name}"
    if os.path.exists(secret_path):
        with open(secret_path, 'r') as secret_file:
            return secret_file.read().strip()
    return os.getenv(secret_name.upper())

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname=read_secret('postgres_db'),
            user=read_secret('postgres_user'),
            password=read_secret('postgres_password'),
            host="app_database") # tells the application to connect to the app_database service defined in docker-compose.yml via Docker's internal networking
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        exit(1)

def fetch_name():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM test ORDER BY id ASC LIMIT 1;")
    name = cursor.fetchone()
    cursor.close()
    conn.close()
    return name[0] if name else "No name found."

if __name__ == "__main__":
    name = fetch_name()
    print(f"Greeting from database: {name}")
