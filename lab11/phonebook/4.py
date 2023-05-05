import psycopg2
from config import data
 
db = psycopg2.connect(**data)
curr = db.cursor()

sql = '''
    CREATE OR REPLACE FUNCTION get_data_with_pagination(limit_int INTEGER, offset_int INTEGER) RETURNS SETOF phonebook_2v AS $$
    BEGIN
        RETURN QUERY SELECT * FROM phonebook_2v LIMIT $1 OFFSET $2;
    END;
    $$ LANGUAGE plpgsql;
''' 

curr.execute(sql)

first_int = input("limit : ")
second_int = input("offset : ")

curr.execute('SELECT * FROM get_data_with_pagination (%s, %s)',(first_int, second_int))

result = curr.fetchall()
print(result)

curr.close()

db.commit()
db.close()

# limit_int is the maximum number of rows to return per page, and offset_int is the starting position of the first row to return.
