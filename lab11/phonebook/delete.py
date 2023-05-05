import psycopg2
from config import data

db = psycopg2.connect(**data)

curr = db.cursor()

name = input("Enter the name : ")

remove = ''' DELETE FROM phonebook_2v WHERE name = %s ; '''

curr.execute(remove, (name,))
print("Contact Successfully Deleted!")
curr.close()

db.commit()
db.close()