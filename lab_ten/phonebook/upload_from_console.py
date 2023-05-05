import psycopg2
from config import data

add = ''' INSERT INTO phonebook VALUES (%s, %s, %s); '''

db = psycopg2.connect(**data)
curr = db.cursor()

# enter data from console :
id = input("Enter ID : ")
name = input("Enter the name : ")
number = input("Enter the phone number : ")

curr.execute(add, (id, name, number))
print("Contact Successfully Added!")

curr.close()

db.commit()
db.close()