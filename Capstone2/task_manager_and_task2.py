#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import date

#====Login Section====
users={}#creating an empty dictionary to store user names and passwords
user_credentials=open("users.txt","r")#opening user credentials file in read mode
for user in user_credentials:#reading the user credentials stored in the file line by line
    temp_user=[]
    temp_user=user.split(", ")#categorizing the data in a line by using comma(,)
    #storing the user name and password in the dictionary as key value pairs
    users[temp_user[0]]=temp_user[1].replace("\n","")
# Checking authorization of the user
authorized=False
while authorized==False:
    username=input("Enter Username:\t")
    password=input("enter password:\t")
  
    if username in users.keys(): #checking username with keys of the dictionary
        if password in users.values(): #checking password with values in the dictionary
            authorized=True
            break # if both matches make authorized variable to TRUE and break from the loop
        else:
            print ("password is invalid! Try again")
    else:
        print("username is invalid! Try again")# else try again ,continue in the loop until user gives correct password and username

while  authorized==True:
    #presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    if username=="adminA":
        menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        d - Display statistics
        e - Exit
        : ''').lower()
    else:    
        menu = input('''Select one of the following Options below:
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
        : ''').lower()

    if menu == 'r':
    #In this block you will write code to add a new user to the user.txt file
        if username=="adminA":
            new_username=input("\tEnter new username to register:\t") #Request input of a new username
            while True:
                new_password=input("\tEnter new password:\t")  #Request input of a new password   
                confirm_new_password=input("\tconfirm new password:\t")# Request input of password confirmation
                if new_password==confirm_new_password: #Check if the new password and confirmed password are the same.
                    user_credentials=open('users.txt','a+')    #If they are the same, add them to the users.txt file
                    user_credentials.write("\n"+new_username+", "+new_password)
                    break
                else:
                    print("\t Enter passwords correctly! Try again!") # If they are not same ask again to enter until paswords match 
                    continue
        else:
            print("you are not authorized to do this activity!")     

    elif menu == 'a':
    #In this block you will put code that will allow a user to add a new task to task.txt file
        task_user=input("\tEnter a username of the person whom this task assigned to :\t")#A username of the person whom the task is assigned to
        task_title=input("\tEnter task title:\t")   # A title of a task     
        task_description=input("\tEnter task description:\t") # A description of the task
        today=date.today()
        date_assigned=today.strftime("%d/%m/%Y")#get the current date
        due_date=input("\tEnter due date (DD/MM/YYYY) :\t") #the due date of the task
        task_complete=input("\tIs task complete? yes/no :\t") # status of the task
        file_tasks=open('tasks.txt','a+') #Add the data to the file task.txt
        file_tasks.write(f"{task_user}, {task_title}, {task_description}, {date_assigned}, {due_date}, {task_complete}\n")
        
    elif menu == 'va':
        '''In this block you will put code so that the program will read the task from task.txt file and
            print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
        '''
        tasks={}    
        file_tasks=open('tasks.txt','r') # Read a line from the file.
        for task in file_tasks:
            temp_task=task.split(",") #Split that line where there is comma and space.
            print("____________________________________________________________________________________\n")
            tasks["Task Tile"]=temp_task[1]
            tasks["Assigned to "]=temp_task[0]
            tasks["Assigned date"]=temp_task[3]
            tasks["Task due date"]=temp_task[4]
            tasks["Task completed?"]=temp_task[5]
            tasks["Description"]=temp_task[2]
            for keys,values in tasks.items():# Then print the results in the format shown in the Output 2 using a for loop.
                print(f"{keys}\t\t{values}") 
        print("____________________________________________________________________________________\n")       
    elif menu == 'vm':
        '''In this block you will put code the that will read the task from task.txt file and
            print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
        '''
        tasks={}    
        file_tasks=open('tasks.txt','r') # Read a line from the file
        for task in file_tasks:
            temp_task=task.split(",") # Split the line where there is comma and space.
            tasks["Task Tile"]=temp_task[1]
            tasks["Assigned to"]=temp_task[0]
            tasks["Assigned date"]=temp_task[3]
            tasks["Task due date"]=temp_task[4]
            tasks["Task completed?"]=temp_task[5]
            tasks["Description"]=temp_task[2]
            #Check if the username of the person logged in is the same as the username you have read from the file.
            if username == tasks["Assigned to"] : #If they are the same print it in the format of Output 2 in the task PDF
                print("____________________________________________________________________________________\n") 
                for keys,values in tasks.items():                       
                    print(f"{keys}\t\t{values}") 
                print("____________________________________________________________________________________\n")
            else:#username and task assigned person not same continue checking remaining records
                continue   
    elif menu == 'd':
        # check if user is admin or not
        if username=="adminA":
            # get the total no. of users and display
            user_credentials=open("users.txt","r")   
            lines=user_credentials.readlines()
            print(f"Total number of users are {len(lines)}") 
            # Get the total number of tasks and display 
            file_tasks=open("tasks.txt","r")   
            lines=file_tasks.readlines()
            print(f"Total number of tasks assigned are {len(lines)}")  
        else:
            print("You are not authorized to check the statistics.")                
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    # If user enters anything other than menu choices
    else:
        print("You have made a wrong choice, Please Try again")
 