import psycopg2, csv
from lab10.phonebook.config import data

config = psycopg2.connect(**data)

curr = config.cursor()

change = input("What do you want to change : name -> 1, number -> 2")
changer=input("Ok, who is this? ")

if change == 1:
    sql = """
            UPDATE PhoneBook SET name = %s WHERE name = %s;
    """
if change == 2:
    sql = """
            UPDATE PhoneBook SET number =%s WHERE name=%s;
    """

config = psycopg2.connect(**data)

curr = config.cursor()

curr.execute(sql, input("new value :"), changer)

curr.close()

config.commit()
config.close()