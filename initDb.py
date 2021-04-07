import db
import psycopg2

#initialize the database and commit
def create_tables():
    """Initializes database with pre designed tables."""
    commands = ("""CREATE TABLE IF NOT EXISTS Product (
                id  SERIAL PRIMARY KEY,
                name VARCHAR(256) NOT NULL,
                image_link VARCHAR(512) NOT NULL,
                price MONEY NOT NULL)""",("""SELECT version()""")
                )
        #,
        #"""set LC_MONETARY to "en_GB.utf8" 
        #""")#TODO: fix this shit
    conn = db.connect()
    try:
        
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        print("tyables created lmao")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()