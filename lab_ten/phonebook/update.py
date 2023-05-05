import psycopg2
from config import data

db = psycopg2.connect(**data)

curr = db.cursor()

upd1 = ''' UPDATE phonebook SET number = %s WHERE name = %s ;'''
upd2 = ''' UPDATE phonebook SET name = %s WHERE number = %s ; '''

mode = int(input())

if mode == 1:  # changing the number by the name :
    name = input("Enter the name : ")
    number = input("Enter the number : ")
    curr.execute(upd1, (number, name))
    print("Contact Number Successfully Changed!")
    
elif mode == 2:  # changing the the name by number :
    name = input("Enter the name : ")
    number = input("Enter the number : ")
    curr.execute(upd2, (name, number))
    print("Contact Name Successfully Changed!")

curr.close()

db.commit()
db.close()