# lib/config.py
import sqlite3

CONN = sqlite3.connect('company.db') #conn is a constant equal to a hash that contains a connection to the database
CURSOR = CONN.cursor() #a constant that allows us interact with the database and execute SQL statements
