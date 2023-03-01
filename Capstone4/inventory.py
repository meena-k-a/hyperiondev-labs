'''
Software Engineering ,Task 32
Capstone Project IV, OOP concepts
'''
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity    

    def __str__(self):
        return f'''--------------------------------------
        country : {self.country}
        shoe code : {self.code}
        product name : {self.product}
        shoe cost : {self.cost}
        shoe quantity :{self.quantity} 
============================================= '''
    def get_cost(self):
        return self.cost  

    def get_quantity(self):
        return self.quantity
 
#=============Shoe list===========
'''The list will be used to store a list of objects of shoes.'''
shoe_list = []

read_once = 0
#==========Functions outside the class==============
def read_shoes_data():
    global read_once
    txt_file = None
    if (read_once == 0) :   
        try:
            # open the file inventory.txt and  read the data from file
            txt_file = open("inventory.txt","r", encoding='cp1252') 
            txt_file_data = txt_file.readlines() 
            # create a shoes object with this data and append this object into the shoes list
            for index,line in enumerate(txt_file_data):
                if index > 0: # Skipping fist line which is in 0 index 
                    line = (line.strip("\n")).split(",")
                    shoe = Shoe(line[0],line[1],line[2],line[3],line[4])
                    shoe_list.append(shoe)
            read_once = 1        
        except  FileNotFoundError: # this error pop up when file doesn't exist
                print("The file inventory.txt does not exist.")
        finally:
            # file close if its exist and opened 
            if txt_file is not None:
                txt_file.close()

# This function will allow a user to capture data about a shoe 
def capture_shoes():
    country = input("Country :\t")
    code = input("Code :\t")
    product = input("Product :\t")
    cost = get_int("Cost :\t")
    quantity = get_int("Quantity :\t")
    shoe_obj = Shoe(country,code,product,cost,quantity)
    shoe_list.append(shoe_obj) 
    #update_file()

# this function prints all details of the shoes in easy readable format
def view_all():
    # print each shoe details from the shoe list        
    if (len(shoe_list) > 0):
        for item in shoe_list:
            print(item)
    else:    
        print("None in the Shoe list.  First Read data from file") 
# This function allows to restock the low quantity shoe
def re_stock():
    # check if shoes are there in the list or not
    if (len(shoe_list) > 0):
        # find the shoe object with the lowest quantity
        min =  int(shoe_list[0].quantity)
        min_object = shoe_list[0]
        for shoe in shoe_list:
            if int(shoe.get_quantity()) < min :
                min = int(shoe.get_quantity())
                min_object = shoe
        #  Ask the user if they want to add this quantity of shoes and then update it 
        add_stock = input("Do you want to add more stock of this product (Yes / No):\t").lower()
        if add_stock == 'yes':
            updated_shoe = min_object
            new_quantity = int(input("How much stock you want add :\t"))
            updated_shoe.quantity = str(min + new_quantity)
            shoe_list.remove(min_object)
            shoe_list.append(updated_shoe)
            # quantity should be updated on the file inventory.txt for this shoe
            update_file()
            print("Restocked shoe updated successfully!")  
        else:
            print("No Stock refilled.")    
    else:
        print("None in the Shoe list")   

# This function allows user to search for a shoe with its code
def search_shoe():
    if (len(shoe_list) > 0):
        search_shoe_code = input("Enter shoe code to search shoe:\t")
        searched = False
        for shoe in shoe_list:
            if shoe.code == search_shoe_code :
                print(shoe)
                searched = True
        if searched == False :   
            print(f"We couldn't find shoe with code {search_shoe_code}")    
    else:
        print("None in the Shoe list.") 
# prints total cost of all shoes     
def value_per_item():
    if (len(shoe_list) > 0):
        for shoe in shoe_list:
            total_value = int(shoe.get_cost()) * int(shoe.get_quantity())
            print (f"{shoe}\n Total value : {total_value}")
    else:
        print("None in the Shoe list.") 
# This function checks for highest quantity shoe and keep it for sale/discount   
def highest_qty():
    if (len(shoe_list) > 0):
        # find the shoe object with the highest quantity
        max =  int(shoe_list[0].quantity)
        for shoe in shoe_list:
            if int(shoe.get_quantity()) > max :
                max = int(shoe.quantity)
                max_obj = shoe
        print(f"{max_obj}\nThis shoe is for sale. 25% discount.")    
    else:
        print("None in the Shoe list. So we cant fine highest quantity") 

# This function updates details of shoes in the file
def update_file():
    txt_file = None
    try:
        txt_file = open("inventory.txt","w", encoding='cp1252') 
        txt_file.writelines("Country,Code,Product,Cost,Quantity\n")
        for line in shoe_list:    
            txt_file.writelines (f"{line.country},{line.code},{line.product},{line.cost},{line.quantity}\n")
    except  FileNotFoundError: # this error pop up when file doesn't exist
            print("The file inventory.txt does not exist.")
    finally:
        # file close if its exist and opened 
        if txt_file is not None:
            txt_file.close()

# This function makes user to enter a correct integer value as input            
def get_int(message):  
    while True:
        try:
            num = int(input(message)) 
            # check if user enters 0 or less value
            if num >= 0:  
                return num
            else :
                print(f"We wont accept negative value.")    
        except:
            # message if they entered other than integer
            print("You have entered an invalid integer , try again") 

#==========Main Menu=============
while True:
    choice = input('''\t\t=============Menu=============
                A - Read Data of each shoe form File
                B - Capture shoe Data 
                C - View Data in readable format
                D - Restock shoe with minimum quantity
                E - Search shoe with shoe code
                F - Total value of each shoe
                G - Product with highest quantity
                Q - Quit
                -----------------------------------
                select one of the option from menu :\t''').upper()
    if choice == "A":                
        read_shoes_data()
        
    elif choice == "B":                
        capture_shoes()
        
    elif choice == "C":
        view_all()
        
    elif choice == "D":    
        re_stock()
        
    elif choice == "E":    
        search_shoe()
        
    elif choice == "F":    
        value_per_item()
        
    elif choice == "G":    
        highest_qty()
        
    elif choice == "Q":
        break
    else:
        print ("Invalid Choice. Try again!")