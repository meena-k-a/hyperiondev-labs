import sqlite3
from  tabulate import tabulate

# Definition to print records in a tabular formate
def tabular_view(data):
    head_row = ['id','name','grade']    
    print(tabulate(data,head_row))

# create a database and connect to it
db = sqlite3.connect('data/Python_programming')

# get a cursor object
cursor = db.cursor()
cursor.execute('''Drop table python_programming''')
# Create a table called python_programming 
cursor.execute(''' create table if not exists python_programming( id int, name varchar(50), grade int)''')
db.commit() # saves a table into database

# insert new rows into the python_programming Table
cursor.execute('''insert into python_programming values (55,'Carl Davis',61)''')
cursor.execute('''insert into python_programming values (66,'Dennis Fredrickson',88)''')
cursor.execute('''insert into python_programming values (77,'Jane Richards',78)''')
cursor.execute('''insert into python_programming values (12,'Peyton Swayer',45)''')
cursor.execute('''insert into python_programming values (2,'Lucas Brooke',99)''')
db.commit()
# Retrieve all records 
records = cursor.execute('''Select * from python_programming''').fetchall() # this query returns a list 
tabular_view(records)

# Select All records with grade between 60 and 80
grade_range_records = cursor.execute('''select * from python_programming where grade between 60 and 80''').fetchall()
tabular_view(grade_range_records)

# Change Carl Davis's grade to 65
cursor.execute('''update table python_programming''')
# Delete Dennis Fredrickson's row
# Change the grade of all people with an id below than 55