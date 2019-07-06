import psycopg2
conn = psycopg2.connect("host=localhost dbname=pv user=postgres password=N0rC@1Life!")
cur = conn.cursor()
cur.execute('SELECT * FROM metadata')
first = cur.fetchone()
print(first)
