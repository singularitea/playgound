#!/usr/bin/python
 
import psycopg2
from config import config
 
 
def insert_sensor(sensor_name, sensor_type):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO sensors(sensor_name, sensor_type)
             VALUES(%s,%s) RETURNING sensor_id;"""
    conn = None
    sensor_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (sensor_name, sensor_type))
        # get the generated id back
        sensor_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return sensor_id

def insert_vendor_list(vendor_list):
    """ insert multiple vendors into the vendors table  """
    sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,vendor_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    # insert one sensor
    insert_sensor("VWP02", "Piezometer")
    # insert multiple vendors
    # insert_sensor_list([
    #     ('AKM Semiconductor Inc.',),
    #     ('Asahi Glass Co Ltd.',),
    #     ('Daikin Industries Ltd.',),
    #     ('Dynacast International Inc.',),
    #     ('Foster Electric Co. Ltd.',),
    #     ('Murata Manufacturing Co. Ltd.',)
    # ])            