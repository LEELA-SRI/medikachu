import os
import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="medikachu_db",
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD'])

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS medicine')
cur.execute('CREATE TABLE medicine ('
             'medicine_name varchar(150) PRIMARY KEY,'
             'bag_name varchar(100) NOT NULL,'
             'description text,'
             'expiry TIMESTAMP)')

conn.commit()

cur.close()
conn.close()

