import psycopg2
import xlwt
import modules.misc as misc


def main():

    properties = misc.read_properties("properties.ini")
    print(properties['DATABASE']['password'])
    conn =  psycopg2.connect(dbname=properties['DATABASE']['dbname'], user=properties['DATABASE']['user'],
                             host='192.168.230.138', port='5432', password=properties['DATABASE']['password'])
    cur = conn.cursor()
    cur.execute("""select table_name from information_schema.tables where table_schema='public' and table_type = 'BASE TABLE'""")
    print(cur.fetchall())
    cur.execute("""select count(name) from planet_osm_point where shop != ''""")
    print(cur.fetchall())

if __name__ == "__main__":
    main()