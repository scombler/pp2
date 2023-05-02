import psycopg2
from config import data

config = psycopg2.connect(**data)

curr = config.cursor()

name = input("Enter the name : ")

upd = """
        DELETE FROM PhoneBook WHERE name = %s;
"""

curr.execute(upd, (name,))
print("Contact Successfully Deleted")

curr.close()

config.commit()
config.close()