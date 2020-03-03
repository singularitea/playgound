#!/usr/bin/python
 
import psycopg2
from config import config
 
 
def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE sensors (
            sensor_id SERIAL PRIMARY KEY,
            sensor_type VARCHAR(50),
            sensor_name VARCHAR(50) NOT NULL
        )
        """,
        """
        CREATE TABLE sensor_data (
            time TIMESTAMPTZ NOT NULL,
            sensor_id INTEGER,
            data DOUBLE PRECISION,
            metadata VARCHAR(50),
            FOREIGN KEY (sensor_id) REFERENCES sensors (sensor_id)
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
 
if __name__ == '__main__':
    create_tables()