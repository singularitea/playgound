#!/usr/bin/python
 
import psycopg2
from config import config
from generate_data import generate_data
import time
 
 
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

def insert_sensor_data(data):
    """ insert data into the sensor_data table  """
    sql = "INSERT INTO sensor_data(time, sensor_id, data, metadata) VALUES(%s,%s,%s,%s)"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,data)
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
    # insert_sensor("VWP02", "Piezometer")

    # insert data
    # time, sensor_id, data, metadata

    reading_amount = 10000

    sensor_id = 1
    generated_data = []

    for i in range(reading_amount, 1, -1):
        generated_data.append(generate_data(sensor_id, 6449.1, 6450.7, i))


    insert_sensor_data(generated_data)     

    # insert_sensor_data([
    #     ('2020-03-12 08:00:00', 1, 6453.2, "comment",),
    #     ('2020-03-12 08:01:00', 1, 6453.4, "comment",),
    #     ('2020-03-12 08:02:00', 1, 6453.6, "comment",),
    #     ('2020-03-12 08:03:00', 1, 6453.3, "comment",),
    #     ('2020-03-12 08:04:00', 1, 6453.9, "comment",)
    # ])            