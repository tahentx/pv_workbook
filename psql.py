import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
cur = conn.cursor()
cur.execute('SELECT * FROM metadata')
