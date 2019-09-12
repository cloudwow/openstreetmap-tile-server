import psycopg2
try:
   connection = psycopg2.connect(user="dude",
                                 password="dude",
                                  host="127.0.0.1",
                                  database="gis")
   cursor = connection.cursor()
   query = """ select *,st_astext(st_transform(way,4326)) from planet_osm_point where way && ST_TRansform(  ST_MakeEnvelope (                     
        -110, 33, -109, 34, 4326), 900913) and amenity='school' limit 1"""
  
   cursor.execute(query)
   print("Selecting rows using cursor.fetchall")
   mobile_records = cursor.fetchall()

   print("Print each row and it's columns values")
   for row in mobile_records:
       print("ROW", row )

except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)
finally:
    #closing database connection.                                                                                                                             
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

