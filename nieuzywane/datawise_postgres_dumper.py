# ! pip install psycopg2
import psycopg2

try:
    connect_str = "dbname='locit_sample' user='sample_user' host='85.194.245.31' " + \
                  "password='!TajemniczaTajemnica7'"
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()

    # download the population data from Poznan

except Exception as e:
    print("Can't connect. Invalid dbname, user or password?")
    print(e)