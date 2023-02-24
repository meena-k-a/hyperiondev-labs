''' This program allows a bookstore clerk to 
    add new books,
    update books,
    delete books,
    search the database to find a specific book.
'''
import sqlite3
from tabulate import tabulate
            
# get/create a database connection to a database ebookstore
db = sqlite3.connect("ebookstore")
# get cursor object to point the database
cursor = db.cursor() 

#--------Function definitions here-------
def init_database():
    # Create a table book  if it doesn't exists
    cursor.execute('''create table if not exists books (
                ID int primary key,
                Title varchar(100) not null,
                Author varchar(100) not null,
                Quantity int )''')
    # insert records into table books
    insert_a_record(3001,'A Tale of Two Cities','Charles Dickens',30)
    insert_a_record(3002,'Harry potter and the philosopher\'s stone','J.K.Rowling',40)
    insert_a_record(3003,'The Lion,The witch and the Wardrobe','C.S.Lewis',25)
    insert_a_record(3004,'The Lord of the rings','J.R.R.Tolkien',37)
    insert_a_record(3005,'Alice in wonderland','Lewis Carroll',12)
    view_all_records()

# Adding a book to database
def insert_a_record(id,title,author,qty) :
    try:
       
        cursor.execute(''' insert into books values (?,?,?,?)''',(id,title,author,qty))  
        db.commit()
        #print("New book inserted successfully")
        #view_all_records()
    except sqlite3.IntegrityError:  
        print(f"This Book Id : {id} already used. Give a unique ID.")
        print("Sorry, No Book inserted ")   

def get_last_row_id():
    last_row = cursor.execute('select * from books').fetchall()[-1]
    return last_row[0]

# Updating book's Title/Author/quantity   
def  update_book_info():
    print('Book details will be updated using book ID')
    print('which book details you want to change')        
    book_id = get_int_input("Book ID : ") 
    print("Enter the details of book")
    new_book_title = get_not_null_input("Book Title : ")
    new_book_author = get_not_null_input("Book Author : ")
    new_book_qty=get_int_input("Book Quantity : ")
    cursor.execute('''update books set Title = ?, Author = ?, Quantity = ? 
                    where ID = ?''',(new_book_title,new_book_author,new_book_qty,book_id))
    db.commit()
    
# definition to view  all records in tabular format
def view_all_records():
    records = cursor.execute('select * from books') 
    col_names = ['ID','Title','Author','Quantity']
    print(tabulate(records,col_names))

# checking input value integer
def get_int_input(message):
    while True:
        try:
            num = int(input(message))
            if num >= 0 :
                break
            else:
                print(" Enter Positive integers only")
        except :
            print("Invalid positive integer. Enter again.")
    return num
def get_not_null_input(message):
    str_input = ""
    while True:
        str_input = input(message)
        if len(str_input.strip()) != 0:
            break
        else:
            print(" It wont accept null value")
    return str_input        
# ------------main code starts here-----------
# initializing the database
init_database()
while True:
    choice = get_int_input('''
                Choose one of the following option
                    1 - Enter book
                    2 - Update book
                    3 - Delete book
                    4 - Search books
                    0 - Exit 
                your choice is : ''')
    if  choice == 0:
        print("Than you for visiting our Book store. See you again.\n")
        cursor.execute('Drop table books')
        db.commit() 
        break
    elif choice == 1:
        print("Enter Your book details below :")
        book_id = get_last_row_id() + 1
        book_title = get_not_null_input("Book Title : ")
        book_author = get_not_null_input("Book Author : ")
        book_qty=get_int_input("Book Quantity : ")
        insert_a_record(book_id,book_title,book_author,book_qty)
        view_all_records()
    elif choice == 2: # update book by ID 
        update_book_info()
        view_all_records()
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice > 4 :
        print ("Invalid Choice !")
        continue

db.close() # always close the database at the end