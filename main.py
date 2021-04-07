# coding=utf-8

import db 
import os
import time
time.sleep(5)#let the postgresql be ready to accept connections


db.initDatabase()
os.system("flask run --port=3333  --host=0.0.0.0")


