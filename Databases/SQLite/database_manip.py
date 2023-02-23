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
print("ALL RECORDS FROM TABLE python_programming")
tabular_view(records)
db.commit()

# Select All records with grade between 60 and 80
grade_range_records = cursor.execute('''select * from python_programming where grade between 60 and 80''').fetchall()
print("All records with grade between 60 and 80")
tabular_view(grade_range_records)
db.commit()

# Change Carl Davis's grade to 65
name = 'Carl Davis'
grade = 65
cursor.execute('''update python_programming set grade = ? where name = ?''',(grade,name))
updated_records = cursor.execute('''Select * from python_programming''').fetchall()
print("All Records after changing Carl Davis's grade to 65")
tabular_view(updated_records)
db.commit()

# Delete Dennis Fredrickson's row
cursor.execute('delete from python_programming where name = "Dennis Fredrickson"')
remain_records = cursor.execute('''select * from python_programming ''').fetchall()
print("All Records after deleting Dennis Fredrickson's row")
tabular_view(remain_records)
db.commit()

# Change the grade of all people with an id below than 55
cursor.execute('update python_programming set grade = 100 where id < 55')
records = cursor.execute('select * from python_programming').fetchall()
print("All records after changing grades of all people with an id below than 55 ")
tabular_view(records)
db.commit()