import psycopg2 as psql
from config import config

"""     app = Flask(__name__)
    api = Api(app)
 """

def connect():
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
            
def add_values(*sql):
    print(sql)





