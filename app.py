from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Function jo database se data layega
def get_logs():
    conn = sqlite3.connect('productivity.db')
    c = conn.cursor()
    # Data nikal ke lao (Latest pehle)
    c.execute("SELECT * FROM logs ORDER BY id DESC")
    data = c.fetchall()
    conn.close()
    return data

# Website ka Home Page
@app.route('/')
def index():
    logs = get_logs()
    # Data ko 'index.html' bhej do
    return render_template('index.html', logs=logs)

if __name__ == '__main__':
    app.run(debug=True)