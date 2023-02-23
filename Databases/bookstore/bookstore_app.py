'''
This program allows a bookstore clerk to 
    add new books,
    update books,
    delete books,
    search the database to find a specific book.
'''
import sqlite3
from tabulate import tabulate

def execute_query(query):
    cursor.execute(query)
    db.commit()

def insert_a_record(id,title,author,qty) :
    cursor.execute(''' insert into books values (?,?,?,?)''',(id,title,author,qty))   
    db.commit()
# definition to view records
def view_all_records():
    records = cursor.execute('select * from books') 
    col_names = ['ID','Title','Author','Quantity']
    print(tabulate(records,col_names))

# get/create a database connection to a database ebookstore
db = sqlite3.connect("ebookstore")
cursor = db.cursor() # get cursor object to point the database
execute_query('Drop table books')
# Create a table book  if it doesn't exists
cursor.execute('''create table if not exists books (
                ID int,
                Title varchar(100),
                Author varchar(100),
                Quantity int )''')
db.commit()  

# insert records into table books
insert_a_record(3001,'A Tale of Two Cities','Charles Dickens',30)
insert_a_record(3002,'Harry potter and the philosopher\'s stone','J.K.Rowling',40)
insert_a_record(3003,'The Lion,The witch and the Wardrobe','C.S.Lewis',25)
insert_a_record(3004,'The Lord of the rings','J.R.R.Tolkien',37)
insert_a_record(3005,'Alice in wonderland','Lewis Carroll',12)
view_all_records()
while True:
    # Choice menu 
    choice = int (input (''' Choose one of the following option
                            1. Enter book
                            2. Update book
                            3. Delete book
                            4. Search books
                            0. Exit  '''))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 0:
        break
    else :
        print ("Invalid Choice !")
        
db.close() # always close the database at the end