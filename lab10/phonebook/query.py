import psycopg2
from config import data

db = psycopg2.connect(**data)

curr = db.cursor()

mode = int(input())

# filter to display all name data in alphabetical order :
f1 = ''' SELECT name FROM phonebook ORDER BY name ASC ;'''
# curr.execute(f1)

# filter to display all data :
f2 = ''' SELECT * FROM Phonebook ; '''
# curr.execute(f2)

if mode == 1:
    curr.execute(f1)
    print("all names in phonebook table in alphabetical order : ")
    print(*curr.fetchall(), sep = "\n")

elif mode == 2:
    curr.execute(f2)
    print("phonebook table : ")
    print(*curr.fetchall(), sep = "\n")


curr.close()

db.commit()
db.close()