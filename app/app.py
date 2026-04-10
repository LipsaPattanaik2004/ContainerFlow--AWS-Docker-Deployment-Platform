from flask import Flask
import socket
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="testdb",
        user="user",
        password="password"
    )
    return conn

@app.route("/")
def home():
    hostname = socket.gethostname()

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        time = cur.fetchone()
        cur.close()
        conn.close()
    except:
        time = ["DB not connected"]

    return f"Hello from {hostname} | DB Time: {time}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
