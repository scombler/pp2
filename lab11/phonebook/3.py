import psycopg2
from config import data

db = psycopg2.connect(**data)
curr = db.cursor()

names = input().split()
numbers = input().split()

sql = '''
    CREATE OR REPLACE PROCEDURE insert_new_users(
        names VARCHAR[],
        phones VARCHAR[]
    )
    LANGUAGE plpgsql
    AS $$
    BEGIN
        IF array_length(names, 1) <> array_length(phones, 1) THEN
            RAISE EXCEPTION 'Number of names and phones do not match';
        END IF;

        FOR i IN 1..array_length(names, 1) LOOP
            IF length(phones[i]) = 3 AND phones[i] ~ '[0-9]{3}' THEN
                INSERT INTO phonebook_2v(name, number)
                VALUES (names[i], phones[i]);
            ELSE
                RAISE NOTICE 'Wrong number for %: %', names[i], phones[i];
            END IF;
        END LOOP;

    END;
    $$;

'''

curr.execute(sql)
curr.execute('CALL insert_new_users (%s,%s)', (names, numbers))

errors = db.notices
for e in errors:
    print(e)

curr.close()

db.commit()
db.close()