import psycopg2

db  = psycopg2.connect(
     host = 'localhost',
     database = 'suppliers',
     user = 'postgres',
     password = '123'
)

curr = db.cursor()

snake = '''
     CREATE TABLE snake (
          username VARCHAR(100),
          user_score VARCHAR(100),
          highscore VARCHAR(100),
          level VARCHAR(12)
     );
'''
curr.execute(snake)

curr.close()

db.commit()
db.close()