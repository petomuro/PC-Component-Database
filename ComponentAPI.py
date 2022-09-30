import sqlite3


class ComponentAPI:
    # Constructor
    def __init__(self):
        self.conn = sqlite3.connect('store.db')
        self.cur = self.conn.cursor()
        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS components (id INTEGER PRIMARY KEY, name text, type text, price integer)')
        self.conn.commit()

    # Destructor
    def __del__(self):
        self.conn.close()

    # Insert data to DB
    def insert(self, name, type, price):
        self.cur.execute('INSERT INTO components VALUES (NULL, ?, ?, ?)', (name, type, price))
        self.conn.commit()

    # Remove data from DB
    def remove(self, id):
        self.cur.execute('DELETE FROM components WHERE id = ?', (id,))
        self.conn.commit()

    # Update data in DB
    def update(self, id, name, type, price):
        self.cur.execute('UPDATE components SET name = ?, type = ?, price = ? WHERE id = ?', (name, type, price, id))
        self.conn.commit()

    # Get all data from DB
    def fetch_all(self, params=None):
        if params is None:
            self.cur.execute(f'SELECT * FROM components {params}')
        else:
            self.cur.execute('SELECT * FROM components')

        return self.cur.fetchall()

    # Get all data from DB ordered by name descending
    def order_by_name_desc(self):
        self.fetch_all('ORDER BY name DESC')

        return self.cur.fetchall()

    # Get all data from DB ordered by name ascending
    def order_by_name_asc(self):
        self.fetch_all('ORDER BY name ASC')

        return self.cur.fetchall()

    # Get all data from DB ordered by price descending
    def order_by_highest_price(self):
        self.fetch_all('ORDER BY price DESC')

        return self.cur.fetchall()

    # Get all data from DB ordered by price ascending
    def order_by_lowest_price(self):
        self.fetch_all('ORDER BY price ASC')

        return self.cur.fetchall()

    # Get all graphic cards from DB
    def fetch_all_graphic_cards(self):
        self.fetch_all("WHERE name LIKE 'Gra%'")

        return self.cur.fetchall()

    # Get all processors cards from DB
    def fetch_all_processors(self):
        self.fetch_all("WHERE name LIKE 'Pro%'")

        return self.cur.fetchall()

    # Get all motherboards cards from DB
    def fetch_all_motherboards(self):
        self.fetch_all("WHERE name LIKE 'Moth%'")

        return self.cur.fetchall()
