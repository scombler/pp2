from config import data
import psycopg2

# connecting to our database :
db = psycopg2.connect(**data)
curr = db.cursor()

sql = '''
        CREATE TABLE phonebook(
            id INT NOT NULL,
            name VARCHAR(100),
            number VARCHAR(100)       
    );
'''

curr.execute(sql)

curr.close()
db.commit()
db.close()