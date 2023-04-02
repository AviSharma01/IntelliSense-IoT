import psycopg2
from psycopg2.extras import RealDictCursor

# Define database connection details
dbname = "intellisense_iot"
user = "your-username"
password = "your-password"
host = "localhost"
port = "your-port"

# Define connection function
def connect():
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    return conn

# Define function to add a new temperature record to the database
def add_temperature(timestamp, temperature, humidity, category):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO temperature (timestamp, temperature, humidity, category) VALUES (%s, %s, %s, %s);", (timestamp, temperature, humidity, category))
    conn.commit()
    cur.close()
    conn.close()

# Define function to get all temperature records from the database
def get_all_temperatures():
    conn = connect()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM temperature;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

# Define function to add a new user to the database
def add_user(username, password, email, is_admin=False):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, password, email, is_admin) VALUES (%s, %s, %s, %s);", (username, password, email, is_admin))
    conn.commit()
    cur.close()
    conn.close()

# Define function to get a user by their username
def get_user_by_username(username):
    conn = connect()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM users WHERE username=%s;", (username,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

# Define function to get a user by their email
def get_user_by_email(email):
    conn = connect()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM users WHERE email=%s;", (email,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row
