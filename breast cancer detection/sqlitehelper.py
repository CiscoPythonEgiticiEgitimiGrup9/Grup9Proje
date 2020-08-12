import sqlite3

class SqliteHelper:
    
    def __init__(self, name=None):
        self.conn = None
        self.cursor = None
        
        if name:
            self.open(name)
    
    def open(self, name):
        try:
            self.conn = sqlite3.connect(name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print("Failed connection to database.")   

    def create_table_test(self):
        c = self.cursor
        c.execute("""
                  CREATE TABLE test(
                  ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  Date Text,
                  Tc TEXT,
                  Name Text,
                  Result Text
                  )
                  """)

    def insert(self, query,data):
        c = self.cursor
        c.execute(query, data)
        self.conn.commit()
    
    def update(self, query,data):
        c = self.cursor
        c.execute(query,data)
        self.conn.commit()

    def select(self, query):
        c = self.cursor
        c.execute(query)
        return c.fetchall()
    
    def delete(self,query):
        c = self.cursor
        c.execute(query)
        self.conn.commit()

#test = SqliteHelper("database.db")
#test.create_table_category()
#test.create_table_paper()
#test.create_table_paper_question()
#test.create_table_question()
#test.create_table_sub_category()

# test.insert("INSERT INTO users (name,year,admin) VALUES ('atılım',1983,0)")
# test.update("UPDATE users SET name='ali' where name='emrah'")
# print(test.select("SELECT * FROM users"))





