import psycopg2
from config import data

db = psycopg2.connect(**data)
curr = db.cursor()

sql1 = ''' SELECT * FROM phonebook_2v WHERE name = %s '''

name = input("enter the name : ")
number = input("enter the number : ")

curr.execute(sql1, (name,))
result = curr.fetchone()

if result: 
    upd = '''
        CREATE OR REPLACE PROCEDURE update_user(new_name VARCHAR, new_number VARCHAR)
        LANGUAGE plpgsql
        AS $$
        BEGIN
            UPDATE phonebook_2v
            SET number = new_number
            WHERE name = new_name;
        END;
        $$;
'''

    curr.execute(upd)
    curr.execute('CALL update_user(%s,%s)', (name, number))

else:
    newone = '''
        CREATE OR REPLACE PROCEDURE new_user(new_name VARCHAR, new_number VARCHAR)
        LANGUAGE plpgsql
        AS $$
        BEGIN
            INSERT INTO phonebook_2v (name, number) VALUES (new_name, new_number);
        END;
        $$;
'''

    curr.execute(newone)
    curr.execute('CALL new_user(%s,%s)', (name, number))
    
curr.close()

db.commit()
db.close()
