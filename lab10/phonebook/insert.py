import psycopg2, csv
from config import data

config = psycopg2.connect(**data)

curr = config.cursor()

add = """
        INSERT INTO Phonebook VALUES(%s, %s) returning *;
"""

with open("info.csv", "r") as f:
    reader = csv.reader(f, delimiter = ",")
    for row in reader:
        pass
        #cursor.execute(add, row)

try:
    name = input("Enter the name : ")
    phone_number = input("Enter the phone number : ")
    curr.execute(add, (name, phone_number))
    print("Contact Successfully Added!")
except:
    print("The requested contact already exists :( ")


curr.close()

config.commit()
config.close()

