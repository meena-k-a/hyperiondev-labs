# Capstone III task_manager.py 

# import libraries
from datetime import datetime

# Definition for registering user
def reg_user(username):
    # This activity only for user admin not for any one
    if username=="admin":
        new_username=input("\tEnter new username to register:\t") #Request input of a new username
        # check new user already exits or not
        while new_username in users_dict:
            print(f"{new_username} is already exists")
            new_username=input("\tEnter new username to register:\t") 
        while True:
            new_password=input("\tEnter new password:\t")  #Request input of a new password   
            confirm_new_password=input("\tconfirm new password:\t")# Request input of password confirmation
            if new_password==confirm_new_password: #Check if the new password and confirmed password are the same.
                user_credentials=open('users.txt','a+',encoding='utf-8-sig')    #If they are the same, add them to the users.txt file
                user_credentials.write(new_username+", "+new_password+"\n")
                print("\tNew username and password updated in users.txt file successfully!\n")
                user_credentials.close()
                break
            else:
                print("\t Enter passwords correctly! Try again!") # If they are not same ask again to enter until passwords match 
                continue
    else:
        print("you are not authorized to do this activity!") 

#In this block you will put code that will allow a user to add a new task to task.txt file
def add_task():
    task_user=input("\tEnter a username of the person whom this task assigned to :\t")#A username of the person whom the task is assigned to
    task_title=input("\tEnter task title:\t")   # A title of a task     
    task_description=input("\tEnter task description:\t") # A description of the task
    today=datetime.today()
    date_assigned=today.strftime("%d %b %Y")#get the current date
    while True:
        try:
            due_date=input("\tEnter due date (ex: 01 Jan 2023) :\t") #the due date of the task
            date_obj = datetime.strptime(due_date, '%d %b %Y')
            #print(date_obj)
            break
        except:
            print("Invalid date! Use this format 01 Jan 2023 ")

    task_complete= 'no' # default task completion is no

    # Casting all the user input info into a list, to add to the tasks_dict.
    task_list = [task_user, task_title, task_description, date_assigned, due_date, task_complete]
    tasks_dict[f"Task {count}:"] = task_list    
    file_tasks=open('tasks.txt','a+', encoding='utf-8-sig') #Add the data to the file task.txt
    file_tasks.writelines(f"{task_user}, {task_title}, {task_description}, {date_assigned}, {due_date}, {task_complete}\n")
    print("\t\n New Task added to tasks file successfully!\n")  
    
# Viw all tasks 
def view_all():
    '''
    In this block you will put code so that the program will read the task from task.txt file and
    print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
    '''
    tasks={} 
    task_number = 0   
    file_tasks=open('tasks.txt','r',encoding='utf-8-sig') # Read a line from the file.
    for task in file_tasks:
        task_number += 1
        temp_task=task.split(",") #Split that line where there is comma and space.
        print("____________________________________________________________________________________\n")
        tasks["Task number"] = task_number
        tasks["Task Tile"]=temp_task[1]
        tasks["Assigned to "]=temp_task[0]
        tasks["Assigned date"]=temp_task[3]
        tasks["Task due date"]=temp_task[4]
        tasks["Task completed?"]=temp_task[5]
        tasks["Description"]=temp_task[2]
        for keys,values in tasks.items():# Then print the results in the format shown in the Output 2 using a for loop.
            print(f"{keys}\t\t{values}") 
    print("____________________________________________________________________________________\n") 
    file_tasks.close()

# This function displays my tasks only (called in view_mine())
def display_my_tasks():
    task_count=0
    my_task_numbers = []
    for key in tasks_dict:
            task_count += 1  # calculating the total number of tasks by increasing the count through tasks_dict. 
            if username == (tasks_dict[key][0]):  # If the task is assigned to the user, it is displayed.
                my_task_numbers.append(task_count)
                print(f"""____________________________________________
                Task {str(task_count)}:      \t{str(tasks_dict[key][1])}
                Assigned to:        {str(tasks_dict[key][0])}
                Date assigned:      {str(tasks_dict[key][3])}
                Due Date:           {str(tasks_dict[key][4])}
                Task Complete?      {str(tasks_dict[key][5])}
                Task Description:   {str(tasks_dict[key][2])}
                ________________________________________________""")  # This is a user friendly format with numbered tasks.
    return my_task_numbers
# This function edits/updates tasks.txt file (called in view_mine())
def edit_updated_task(tasks_dict):
    updated_str=[", ".join(t) for t in tasks_dict.values()]
    with open('tasks.txt','w', encoding='utf-8-sig') as tk_file:
        tk_file.write('\n'.join(updated_str))
    print("Your task has been successfully updated.")    
    tk_file.close()

# View my tasks 
def view_mine(username):
    my_task_numbers = display_my_tasks() # First Display all tasks that belongs to login user
    # The user can now choose to either edit a task by number or return to the main menu.
    while True:    
        task_selection = input("\n To Edit, Select a a task by number (e.g. 1, 2,3) or type -1 to return to the main menu. \n")
    
        if task_selection == "-1":  # If they select '-1', they return to the outer while loop main menu.
            return(menu)
            break        
        elif task_selection.isnumeric() : 
            if int(task_selection) in my_task_numbers :
                if (tasks_dict[f"Task {task_selection}:"][5]).lower() != "yes":
                    # If they enter a task number, they can choose to edit task details.
                    option = input('''Select one of the following options 
                                        A- Change Task assigned to
                                        B- change Task Title
                                        C- Change Task Description
                                        D- Change Due Date
                                        Y- Change Task Completed to yes
                                        E- Exit \n''').upper()
                    if option == "A":
                        # If they choose 'A', task assigned to can be changed in tasks_dict.
                        assigned_to = input("whom you wants to assign this task:\t")
                        tasks_dict[f"Task {task_selection}:"][0] = assigned_to
                        edit_updated_task(tasks_dict)
                    elif option == "B":
                        # If they choose 'B', task title can be changed in tasks_dict.
                        new_task_title = input("Please enter new Task Title:\t")
                        tasks_dict[f"Task {task_selection}:"][1] = new_task_title
                        edit_updated_task(tasks_dict)  
                    elif option == "C":
                        # If they choose 'c', task description can be changed in tasks_dict.
                        new_task_description = input("Please enter new due date of the task (e.g. dd-mm-yyyy)::\t")
                        tasks_dict[f"Task {task_selection}:"][2] = new_task_description
                        edit_updated_task(tasks_dict)    

                    elif option == "D":
                        # If they choose 'D', new due date can be changed in tasks_dict.
                        new_due_date = input("Please enter new due date of the task (e.g. dd-mm-yyyy)::\t")
                        tasks_dict[f"Task {task_selection}:"][4] = new_due_date
                        edit_updated_task(tasks_dict) 

                    elif option == "Y":
                        # If they choose 'Y', the item linked to that task for completion is changed to 'Yes' in tasks_dict.
                        tasks_dict[f"Task {task_selection}:"][5] = "yes"
                        edit_updated_task(tasks_dict) 
                    elif option == "E":
                        # If they choose 'E', Exit from this menu and return to choose task menu.
                        break
                    else:
                        # Message for wrong  option entry
                        print("Invalid choice.")                      
                else:
                    # Message for user if the task completed 
                    print(f" The task {task_selection} is already completed. You cant edit anymore.")  
            else:
                print(f" The task {task_selection} is not your task. Please enter your task number.")       
        else:
            # message to enter correct choice
            print("Task Number is numeric! Enter Correct Task number or '-1' to exit and go to main menu") 

# Generate Task overview (called in gen_reports()
def generate_task_overview():
    # Read tasks from file
    task_file = open("tasks.txt",'r',encoding='utf-8-sig')
    task_list = task_file.readlines()
    task_file.close()
    total_tasks = 0
    uncompleted = 0
    completed = 0
    over_due = 0
    for line in task_list:
        total_tasks += 1 
        data_list = line.strip('\n').split(', ')
        # task completed  or not
        if data_list[5].lower() == "no":
            uncompleted += 1
            due_date = data_list[-2] # date string
            date_obj = datetime.strptime(due_date, '%d %b %Y')
            current_date = datetime.today() # date object
            if date_obj < current_date: #  due date checking 
                over_due += 1
        else :
            completed += 1
    incomplete_percent = round(((uncompleted / total_tasks) * 100),2)
    over_due_percent =  round(((over_due / total_tasks) * 100),2) 
    # Write into task overview details and calculations
    with open('task_overview.txt','w', encoding='utf-8-sig') as tsk_ovi:
        tsk_ovi.writelines(f'''\t\tTASK OVERVIEW\n
            Total tasks\t\t\t\t:\t{total_tasks}\n
            Completed tasks\t\t\t:\t{completed}\n
            Uncompleted tasks\t\t\t:\t{uncompleted}\n
            Uncompleted and Overdue tasks\t:\t{over_due}\n
            percentage of incomplete\t:\t{incomplete_percent} %\n
            Percentage of Overdue tasks\t:\t{over_due_percent} %''')
    tsk_ovi.close()    
        
#  Generate user overview file (called in gen_reports()
def generate_user_overview():   
    # Read Users file data 
    user_file = open("users.txt",'r', encoding='utf-8-sig')
    user_file_list = user_file.readlines() 
    
    total_users = 0
    user_tasks_dict = {}

    #Read tasks file data 
    task_file = open("tasks.txt",'r', encoding='utf-8-sig')
    task_list = task_file.readlines()
    
    # for each user check in task file details 
    for line in user_file_list: 
        total_users += 1  
        each_user_tasks = 0
        user_data_list = line.strip('\n').split(', ') # Users data list 

        total_tasks = 0
        uncompleted = 0
        completed = 0
        over_due = 0

        for task in task_list:
            total_tasks += 1 
            data_list = task.strip('\n').split(', ') # Tasks Data list
            if user_data_list[0] == data_list[0]: # checking user to the task assigned
                each_user_tasks += 1
                if data_list[5].lower() == "no":
                    uncompleted += 1
                    due_date = data_list[-2] # date string
                    date_obj = datetime.strptime(due_date, '%d %b %Y')
                    current_date = datetime.today()#date object
                    if date_obj < current_date:
                        over_due += 1
            else :
                completed += 1
        completed_percent = round(((completed / total_tasks) * 100),2)
        incomplete_percent = round(((uncompleted / total_tasks) * 100),2)
        over_due_percent =  round(((over_due / total_tasks) * 100),2)
        percent_each_user_task = round(((each_user_tasks / total_tasks) * 100), 2)
        user_tasks_dict[user_data_list[0]] = [each_user_tasks, percent_each_user_task, completed_percent,incomplete_percent, over_due_percent]
    
    task_file.close()
    user_file.close()
    # write into user overview details and calculations in file  
    with open('user_overview.txt','w',encoding='utf-8-sig') as usr_ovi:
        usr_ovi.write("\t\tUsers OVERVIEW\n")
        usr_ovi.write(f"Total Number of users registered\t:\t{total_users}\n")
        for key in user_tasks_dict.keys():    
            usr_ovi.write("-----------------------------------------------------------------------------------------\n")  
            usr_ovi.write(f'''{key}:\tThe total number of tasks assigned to {key} is {user_tasks_dict[key][0]}.\n
            The percentage of the total number of tasks assigned to {key} is {user_tasks_dict[key][1]}%.\n
            The percentage of tasks assigned to {key} that have been completed is {user_tasks_dict[key][2]}%.\n
            The percentage of tasks still to be completed by {key} is {user_tasks_dict[key][3]}%.\n
            The percentage of incomplete and overdue tasks assigned to {key} is {user_tasks_dict[key][4]}%.\n''')
    usr_ovi.close()  

# Generating Reports for Admin only
def gen_reports():
    if username=="admin":
        generate_task_overview() 
        generate_user_overview()
        print("Generated 2 reports and saved in task_overview.txt and user_overview.txt in this folder.")
    else:
        print("you are not authorized to do this activity!")

# Display Statistics only for admin
def display_statistics(username):
    if username == "admin":
        # Open task overview file and print in easy readable format
        try:
            print("\t___________________________________________________________")
            with open("task_overview.txt",'r', encoding='utf-8-sig') as tsk_ovi:
                print(tsk_ovi.read())  
            print("\t___________________________________________________________")
        except:
            print("task_overview.txt has not generated yet. Select 'gr' for generating file, then select 'ds' option to overview")
        # open user overview file and print in easy readable format     
        try:
            print("_______________________________________________________________________________________")
            with open("user_overview.txt",'r', encoding='utf-8-sig') as usr_ovi:
                print(usr_ovi.read())  
            print("_______________________________________________________________________________________")
        except:
            print("user_overview.txt has not generated yet. Select first 'gr' for generating file, then select 'ds' option to overview")    
    else :
        # message for user if not admin
        print("You are not authorized to do this activity")   

# Main Program starts here

#creating an users dictionary to store user names and passwords from users.txt file
users_dict={}
with open ("users.txt",'r', encoding='utf-8-sig') as user_credentials:
    for line in user_credentials:
        username, password = line.strip('\n').split(", ")
        users_dict[username] = password     

# Opening the tasks.txt file to read and write information to tasks dictionary
tasks_dict = {}
count = 0
with open('tasks.txt', 'r+', encoding='utf-8-sig') as task_details:
    for line in task_details:
        count += 1  # Count used to change key value for each list of info
        newline = line.rstrip('\n')  # Stripping newline characters.
        split_line = newline.split(", ")  # Splitting line into a list of items.
        tasks_dict[f"Task {count}:"] = split_line # Assigning each list of items to a key in tasks_dict.
               
# Checking authorization of the user
authorized=False
while authorized==False:
    username=input("Enter Username:\t")
    password=input("enter password:\t")
  
    if username in users_dict.keys(): #checking username with keys of the dictionary
        if password in users_dict.values(): #checking password with values in the dictionary
            authorized=True
            break # if both matches make authorized variable to TRUE and break from the loop
        else:
            print ("password is invalid! Try again")
    else:
        print("username is invalid! Try again")# else try again ,continue in the loop until user gives correct password and username

while  authorized==True:
    #presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    if username == "admin":
        menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - View my task
        gr _ Generate reports 
        ds - Display statistics
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
        reg_user(username)
        
    elif menu == 'a':
        add_task()
        
    elif menu == 'va':
        view_all()  
        
    elif menu == 'vm':
        view_mine(username)
    
    elif menu == 'gr':
        gen_reports()
    
    elif menu == 'ds':
        display_statistics(username)
                     
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    # If user enters anything other than menu choices
    else:
        print("You have made a wrong choice, Please Try again")
      