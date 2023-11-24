import sqlite3

# Verbindung zu einer Datenbank erstellen (wird erstellt, falls nicht vorhanden)
conn = sqlite3.connect('example.db')

# Einen Cursor erstellen
c = conn.cursor()

# Eine Tabelle erstellen
c.execute('''CREATE TABLE IF NOT EXISTS stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Daten einfügen
c.execute("INSERT INTO stocks VALUES ('2023-10-01','BUY','AAPL',100,155.65)")

# Änderungen speichern (commit)
conn.commit()

# Daten abfragen
c.execute('SELECT * FROM stocks')

# Ergebnisse ausgeben
for row in c.fetchall():
    print(row)

# Verbindung schließen
conn.close()
