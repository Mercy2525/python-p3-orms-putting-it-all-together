import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:
    def __init__(self,name,breed):
        self.id=None
        self.name=name
        self.breed=breed

    @classmethod
    def create_table(cls):
        sql="""CREATE TABLE IF NOT EXISTS dogs(
            id INTEGER PRIMARY KEY,
            name TEXT,
            breed TEXT
        )"""
        CURSOR.execute(sql)
    
    @classmethod
    def drop_table(cls):
        sql="""DROP TABLE IF EXISTS dogs"""
        CURSOR.execute(sql)

    def save(self):
        sql="""INSERT INTO dogs (name,breed) VALUES (?,?)"""
        CURSOR.execute(sql,(self.name,self.breed))

    @classmethod
    def create(cls,name,breed):
        dog=cls(name,breed)
        dog.save()
        return dog
    
    @classmethod
    def new_from_db(cls,row):
        id,name,breed=row
        dog=cls(name,breed)
        dog.id=id
        return dog

    @classmethod
    def get_all(cls):
        sql="""SELECT * FROM dogs"""
        rows=CURSOR.execute(sql).fetchall()
        return [cls.new_from_db(row) for row in rows]
    
    @classmethod
    def find_by_name(cls,name):
        sql="""SELECT * FROM dogs WHERE name=? LIMIT 1"""
        song=CURSOR.execute(sql,(name)).fetchone()
        return cls.new_from_db(song)
    
    @classmethod
    def find_by_id(cls,id):
        sql="""SELECT * FROM dogs WHERE id=? LIMIT 1"""
        song=CURSOR.execute(sql,(id)).fetchone()
        return cls.new_from_db(song)
