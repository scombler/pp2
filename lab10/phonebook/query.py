import psycopg2
from config import data

config = psycopg2.connect(**data)

curr = config.cursor()

n = int(input())

sql = """
        SELECT * FROM PhoneBook;
"""

if n == 1:
    curr.execute(sql)
    print("all names")
    print(*curr.fetchall(), sep = '\n')


curr.close()

config.commit()
config.close()