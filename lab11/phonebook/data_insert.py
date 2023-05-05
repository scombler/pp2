import psycopg2
from config import data

db = psycopg2.connect(**data)
curr = db.cursor()

sql = ''' INSERT INTO phonebook_2v (name, number) VALUES (%s, %s); '''


name = input("enter the name : ")
number = input("enter the number : ")

curr.execute(sql, (name, number))

curr.close()

db.commit()
db.close()