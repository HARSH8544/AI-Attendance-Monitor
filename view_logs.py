import sqlite3

# Database connect karo
conn = sqlite3.connect('productivity.db')
c = conn.cursor()

print("--- 📅 WORK LOGS (Harsh ki Report) ---")
print(f"{'ID':<5} {'NAME':<15} {'DATE':<12} {'TIME':<10}")
print("-" * 45)

# Saara data nikalo
try:
    c.execute("SELECT * FROM logs ORDER BY id DESC") # DESC matlab naya pehle
    rows = c.fetchall()

    if not rows:
        print("📭 Abhi tak koi data save nahi hua hai.")
    else:
        for row in rows:
            # row = (id, name, date, time)
            print(f"{row[0]:<5} {row[1]:<15} {row[2]:<12} {row[3]:<10}")

except Exception as e:
    print(f"❌ Error: Database nahi khul raha. ({e})")

conn.close()