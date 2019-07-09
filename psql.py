import psycopg2
conn = psycopg2.connect("host=localhost dbname=pv user=postgres password=N0rC@1Life!")
print("Connecting to database")
cur = conn.cursor()
insert_query = "INSERT INTO metadata VALUES {}".format("('999','Solar Mission III','2000.06.048','Vail Academy', '154.05', 'API', 'Also Energy', '7762 E Science  Park Dr', 'AZ', '85747', '32.09662', '-110.826', 'Tucson')")
cur.execute(insert_query)
conn.commit()
