import psycopg2
import xlwt


def main():
    conn =  psycopg2.connect(dbname='gis', user='postgres', host='192.168.230.138', port='5432', password='Fyukjafkjljh123_hfdctnjdfkjyjh!')
    cur = conn.cursor()
    cur.execute("""select table_name from information_schema.tables where table_schema='public' and table_type = 'BASE TABLE'""")
    print(cur.fetchall())
    cur.execute("""select count(name) from planet_osm_point where shop != ''""")
    print(cur.fetchall())

if __name__ == "__main__":
    main()