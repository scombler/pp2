import psycopg2
from config import data

config = psycopg2.connect(**data)

curr = config.cursor()

number = int(input())

filter = """
        SELECT * FROM PhoneBook;
"""

curr.execute(filter)

result = curr.fetchall()

print(result)

curr.close()

config.commit()
config.close()