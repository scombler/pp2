import psycopg2
from config import data
 
sql = ''' SELECT * FROM phonebook_2v ORDER by name DESC ''' 

db = psycopg2.connect(**data)
curr = db.cursor()

curr.execute(sql)

result = curr.fetchall()
for i in result:
    print(i)  # in decreasing orser.

curr.close()

db.commit()
db.close()