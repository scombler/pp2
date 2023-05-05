import psycopg2
from config import data

db = psycopg2.connect(**data)
curr = db.cursor()

sql = '''
        CREATE OR REPLACE FUNCTION get_records_by_pattern(pattern text)
        RETURNS SETOF phonebook_2v AS $$
        BEGIN
            RETURN QUERY SELECT * FROM phonebook_2v 
            WHERE name LIKE '%' || pattern || '%' 
            OR number LIKE '%' || pattern || '%';
        END;
        $$ LANGUAGE plpgsql; ''' 


curr.execute(sql)

findit = input("find the requested name or number : ")

curr.execute('SELECT * FROM get_records_by_pattern (%s)', (findit, ))

result = curr.fetchall()
for r in result:
    print(r)

curr.close()

db.commit()
db.close()