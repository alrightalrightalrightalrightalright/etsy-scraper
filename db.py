import psycopg2
from config import config
import initDb
import logging
from Product import Product

class Db:
    conn= None
    params= None

    def __init__(self):
        try:
            self.params = config()

            print('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect(**self.params)
            
            #test connection
            cur = self.conn.cursor()
            
            print('PostgreSQL database version:')
            cur.execute('SELECT version()')

            db_version = cur.fetchone()
            print(db_version)
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is  None:
                self.conn = None  
            else:
                self.conn.close()

    def AinitDb(self):
        initDb.create_tables()

def connect():
    """ Connect to the PostgreSQL database server and returns connection object"""
    conn = None
    try:
        params = config()

        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        #test connection
        cur = conn.cursor()
        
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        db_version = cur.fetchone()
        print(db_version)
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            return conn
        else:
            return None

def initDatabase():
    initDb.create_tables()

def insertProduct(product):
    try:         
        conn=connect()
        cur = conn.cursor()
        cur.execute( "INSERT INTO Product (name, price, image_link)"+ 
        "VALUES ( %s , %s, %s)" ,(product.title,product.price,product.link))
        cur.close()
        conn.commit()
        print("Product successfuly inserted at database.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        conn.close()

def getAllProducts():
    try:         
        conn=connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Product ORDER BY id ASC ")
        products = cur.fetchall()#warning: returns as list
        cur.close()

        products_asObjects=[]
        for p in products:
            products_asObjects.append(Product(p[1],p[3],p[2],p[0]))

        return products_asObjects
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        conn.close()    

def getProductById(id):
    try:         
        conn=connect()
        cur = conn.cursor()
        cur.execute( "SELECT * FROM Product WHERE id="+str(id))
        #return tuple: (id, title, link, price)
        product= cur.fetchone()
        product= Product.tupleToObj(product)
        cur.close()
        return product

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        conn.close()    


def getNextIndex():
    try:         
        conn=connect()
        cur = conn.cursor()
        cur.execute("SELECT last_value FROM product_id_seq;")
        last_index = cur.fetchone()[0] 
        cur.close()
        return last_index
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        conn.close()    


