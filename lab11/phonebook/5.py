import psycopg2
from config import data

db = psycopg2.connect(**data)
curr = db.cursor()

sql = '''
    CREATE OR REPLACE PROCEDURE delete_user(IN value VARCHAR)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        DELETE FROM phonebook_2v WHERE name = value OR number = value;
    END;
    $$;
''' 

value = input("delete by the name or the number : ")

curr.execute(sql)

curr.execute("CALL delete_user (%s)", (value, ))

curr.close()

db.commit()
db.close()