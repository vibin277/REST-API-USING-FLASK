import sqlite3

conn = sqlite3.connect("database.db")

print("opened databaase successfully")

conn.execute("CREATE TABLE students (name TEXT ,addr TEXT,city TEXT,pin TEXT)")

print("Table created successfully")

conn.close()