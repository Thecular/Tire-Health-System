# Data Generator
import mysql.connector
import random
import time

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1203",
    database = "temperature_db"
)

cursor = conn.cursor()

while True:
    temp = random.randint(20, 40)
    cursor.execute("INSERT INTO temperature(temp_value) VALUES(%s)", (temp,))
    
    conn.commit()
    time.sleep(2)

