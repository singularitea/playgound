#!/usr/bin/python
 
import psycopg2
from config import config

def get_sensors():
    """ query sensors from the sensors table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM sensors ORDER BY sensor_name")
        rows = cur.fetchall()
        print("The number of sensors: ", cur.rowcount)
        for row in rows:
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def get_data():
    """ query sensors from the sensors table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM sensor_data ORDER BY time")
        rows = cur.fetchall()
        print("Data points: ", cur.rowcount)
        for row in rows:
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_sensors()
    get_data()