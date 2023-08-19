
import psycopg2 as psql
from db_config import config

"""     app = Flask(__name__)
    api = Api(app)
 """

def check_connect():
    conn = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')

        conn = psql.connect(**params)
        cur = conn.cursor()

        cur.execute('Select version()')


        db_ver = cur.fetchone()
        print(db_ver)
        cur.close()
    except (Exception, psql.DatabaseError) as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()
            print("db conn closed")

def show_table():

    conn = None
    try:
        params = config()
        conn = psql.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT * FROM weather')

        print(cur.fetchall())
        cur.close()
    except Exception as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()

""" alr created table
def create_tables():
    commands = [
        """ """ 
        CREATE TABLE weather (
        tempCelsius real, 
        humidity real,
        pressure real 
        ) """ """ 
    ]
    conn = None
    try: 
        params = config() 
        conn = psql.connect(**params)
        cur = conn.cursor()

        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psql.DatabaseError) as e:
        print(e)
    finally:
        if conn is not None:
            conn.close() """

def get_values(*sql):
    conn = None
    return_list = []
    try:
        params = config()
        conn = psql.connect(**params)
        cur = conn.cursor()

        for cmd in sql:
            cur.execute(cmd)
            return_list.append(cur.fetchall())
        cur.close()
    except Exception as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()
            return return_list

