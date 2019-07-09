import psycopg2
conn = psycopg2.connect("host=localhost dbname=pv user=postgres password=N0rC@1Life!")
print("Connecting to database")
cur = conn.cursor()
with open(r'C:\Users\thendricks\pfdrivedev\pv_workbook\oasg.csv') as f:
    next(f)
    cur.copy_from(f,'metadata', sep=',')
    conn.execute()
    conn.close()
