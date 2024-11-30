from flask import Flask
import json
import sqlite3
app = Flask(__name__)
database = 'airport.db'
connection = sqlite3.connect(database)
cursor = connection.cursor()
cursor.execute("SELECT * FROM airport")
rows = cursor.fetchall()
