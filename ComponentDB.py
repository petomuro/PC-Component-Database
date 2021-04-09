import sqlite3
from Component import PCComponent

# Pre pracu s sqlite3 je potrebne vytvorit connection "conn = sqlite3.connect(ComponentDB)"
# a vlastne do store.db "ComponentDB = ComponentDatabase('store.db')" sa budu ukladat udaje
# "cur = conn.cursor()" vytvorenie objektu pre volanie metody "execute()" na vykonavanie SQL prikazov
# conn.commit() Uklada zmeny
# "fetchall()" nacitava vsetky riadky z databazy
# conn.close() zatvara connection

# def changename(self):
        # self.cur.execute("ALTER TABLE components RENAME TO Components")
        # self.conn.commit()

class ComponentDatabase:
    # Konstruktor
    def __init__(self, ComponentDB):
        self.conn = sqlite3.connect(ComponentDB)
        self.cur = self.conn.cursor()
        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS components (id INTEGER PRIMARY KEY, name text, type text, price integer)')
        self.conn.commit()

    # Vrati vsetky riadky z databazy
    def fetch(self):
        self.cur.execute('SELECT * FROM components')
        rows = self.cur.fetchall()
        return rows

    # Vklada udaje do databazy
    def insert(self, name, type, price):
        self.cur.execute('INSERT INTO components VALUES (NULL, ?, ?, ?)', (name, type, price))
        self.conn.commit()

    # Vymazava udaje z databazy
    def remove(self, id):
        self.cur.execute('DELETE FROM components WHERE id = ?', (id,))
        self.conn.commit()

    # Upravuje udaje v databaze
    def update(self, id, name, type, price):
        self.cur.execute('UPDATE components SET name = ?, type = ?, price = ? WHERE id = ?', (name, type, price, id))
        self.conn.commit()

    # Vrati vsetky riadky z databazy usporiadane podla mena vzostupne
    def orderbynamedesc(self):
        self.cur.execute('SELECT * FROM components ORDER BY name DESC')
        rows = self.cur.fetchall()
        return rows

    # Vrati vsetky riadky z databazy usporiadane podla mena zostupne
    def orderbynameasc(self):
        self.cur.execute('SELECT * FROM components ORDER BY name ASC')
        rows = self.cur.fetchall()
        return rows

    # Vrati vsetky riadky z databazy usporiadane podla ceny vzostupne
    def orderbypricehighest(self):
        self.cur.execute("SELECT * FROM components ORDER BY price+0 DESC")
        rows = self.cur.fetchall()
        return rows

    # Vrati vsetky riadky z databazy usporiadane podla ceny zostupne
    def orderbypricelowest(self):
        self.cur.execute("SELECT * FROM components ORDER BY price+0 ASC")
        rows = self.cur.fetchall()
        return rows

    # Vrati vsetky Graphic Cards
    def choosegraphic(self):
        self.cur.execute("SELECT * FROM components WHERE name LIKE 'Gra%'")
        rows = self.cur.fetchall()
        return rows

    # Vrati vsetky Processors
    def chooseprocessor(self):
        self.cur.execute("SELECT * FROM components WHERE name LIKE 'Pro%'")
        rows = self.cur.fetchall()
        return rows

    # Vrati vsetky Motherboards
    def choosemotherboard(self):
        self.cur.execute("SELECT * FROM components WHERE name LIKE 'Moth%'")
        rows = self.cur.fetchall()
        return rows

    # Destruktor
    def __del__(self):
        self.conn.close()

# Ulozenie databazy do store.db + vlozenie udaju
# ComponentDB = ComponentDatabase('store.db')
# ComponentDB.insert('Graficka Karta', 'NVIDIA Geforce GTX 1060', '350')
