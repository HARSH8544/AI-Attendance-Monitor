import sqlite3
from datetime import datetime

# Database aur Table banana
def init_db():
    conn = sqlite3.connect('productivity.db')
    c = conn.cursor()
    # Table: ID, Naam, Tareekh, Time
    c.execute('''CREATE TABLE IF NOT EXISTS logs
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  name TEXT, 
                  date TEXT, 
                  time TEXT)''')
    conn.commit()
    conn.close()

# Entry save karna
def log_entry(name):
    conn = sqlite3.connect('productivity.db')
    c = conn.cursor()
    
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")

    # Check karo: Kya abhi haal hi mein entry ki hai? (Taaki spam na ho)
    c.execute("SELECT * FROM logs WHERE name=? ORDER BY id DESC LIMIT 1", (name,))
    last_entry = c.fetchone()

    should_save = True
    if last_entry:
        # Agar pichli entry ko 1 minute bhi nahi hua, to dobara save mat karo
        last_time_str = last_entry[3] # Time column
        last_time = datetime.strptime(last_time_str, "%H:%M:%S")
        time_diff = (now - now.replace(hour=last_time.hour, minute=last_time.minute, second=last_time.second)).seconds
        
        if time_diff < 60: # 60 second ka gap rakhenge
            should_save = False

    if should_save:
        c.execute("INSERT INTO logs (name, date, time) VALUES (?, ?, ?)", (name, date_str, time_str))
        conn.commit()
        print(f"💾 Saved: {name} at {time_str}")
    
    conn.close()

# Jab ye file banegi, database turant ban jayega
init_db()