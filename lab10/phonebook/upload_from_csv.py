from config import data
import psycopg2, csv

db = psycopg2.connect(**data)
curr = db.cursor()

# upload data from info.csv :
with open("info.csv", "r") as f:
     reader = csv.reader(f)
     next(reader)   # skip the header row 
     curr.copy_from(f, "phonebook", sep = ";")
        #for row in reader:
             #curr.execute(add, row)

curr.close()

db.commit()
db.close()


# delete all the previous info from the table :
""" def upload_from_csv(curr): 
    remove = ''' DELETE FROM telephonebook ; '''
    curr.execute(remove) """
