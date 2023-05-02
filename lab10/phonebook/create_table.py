import psycopg2
from config import data

# connecting to our database :
config = psycopg2.connect(**data)

curr = config.cursor()

sql = """
        CREATE TABLE PhoneBook(
            name VARCHAR PRIMARY KEY,
            number VARCHAR(11)
    );
"""

curr.execute(sql)

curr.close()
config.commit()
config.close()