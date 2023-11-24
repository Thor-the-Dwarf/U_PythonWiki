import sqlite3

# Verbindung zu einer Datenbank erstellen (wird erstellt, falls nicht vorhanden)
conn = sqlite3.connect('demo.db')

# Einen Cursor erstellen
c = conn.cursor()

# Eine Tabelle erstellen
c.execute('''CREATE TABLE IF NOT EXISTS stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Daten einfügen
# c.execute("INSERT INTO stocks VALUES ('2023-10-01','BUY','AAPL',100 ,155.65)")
c.execute('INSERT into personen (name, lebensalter) VALUES("maria", 25)')


# Änderungen speichern (commit)
conn.commit()

# Daten extrahieren
c.execute('SELECT * FROM stocks') #jetzt ist das Querry im Cursor
for row in c.fetchall():
    print(row)

# Verbindung schließen
conn.close()

