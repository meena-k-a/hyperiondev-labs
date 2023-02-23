'''
SQlite:
'''
import sqlite3
from tabulate import tabulate

# create a database and connect to it
database = sqlite3.connect('Company_db')

def get_emp():
    emp_n = int(input('Enter employee number: '))
    emp_name = input('Employee Name : ')
    emp_sname = input('employee surname: ')
    age = int(input('age : '))
    return emp_n,emp_name,emp_sname,age
def view_data(data):
    for row in data:
        print(f'''
        ==========================
        Employee Number : {row[0]}
        Employee Name : {row[1]}
        Employee Surname : {row[2]}
        Employee age : {row[3]}''')

def table_view(data):
    heading = ['Employee number', 'Employee Name', 'Employee Surname','Employee age']
    print(tabulate(data,heading))

# get cursor object 
curs = database.cursor()
# execute a query for creating an Employee table if not exists
curs.execute('''create table  if not exists Employees(
Emp_num int,
Emp_name varchar(50) not null,
Emp_sname varchar(50) not null,
Emp_age int 
)''')
# Save the Employee table into Company_db  (get complete state)
database.commit()
'''

'''
# Add data/rows
#emp_n,emp_name,emp_sname,age = get_emp()
#curs.execute('''insert into Employees
#                 values (?,?,?,?)''',(emp_n,emp_name,emp_sname,age))

# retrieve data/rows
data = curs.execute('''select * from Employees''').fetchall() # here data is a list
#view_data(data)
table_view(data) 
database.commit()

#curs.execute('''drop table Employees''')
database.close()