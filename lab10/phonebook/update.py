import psycopg2, csv
from config import data

config = psycopg2.connect(**data)

curr = config.cursor()

upd = """
        UPDATE Phonebook SET number = %s WHERE name = %s;
"""

name = input()
phone_number = input()

curr.execute(upd, (phone_number, name))
print("Contact Successfully Changed!")

curr.close()

config.commit()
config.close()