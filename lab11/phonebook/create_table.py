import psycopg2
from config import data

db = psycopg2.connect(**data)
curr = db.cursor()

sql = '''
    CREATE TABLE phonebook_2v (
        id SERIAL PRIMARY KEY,
        name VARCHAR,
        number VARCHAR
    );
'''


curr.execute(sql)

curr.close()

db.commit()
db.close()