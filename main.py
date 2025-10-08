import json
import os

# import datetime as dt

file_path = "task_list.json"
if not os.path.exists(file_path):
    print("File not found!")
    json_err = input("do you want to make new file? (y/n)")
    if json_err.lower() == 'y':
        with open(file_path, "w") as file:
            json.dump([], file, indent=4)
        print("New JSON file created")
    else:
        print("Operation canceled")
else :
    try:
        with open(file_path, 'r', encoding='utf-8') as read_file:
            data = json.load(read_file)
        print("JSON File loaded sucessfully")

    except json.JSONDecodeError:
        print("JSON file error detected")
        json_err = input("do you want to make new file? (y/n)")
        if json_err.lower() == 'y':
            with open(file_path, "w") as file:
                json.dump([], file, indent=4)
            print("New JSON file created")
        else:
            print("Operation canceled")
# with open(file_path, 'r', encoding='utf-8') as read_file:
#     data = json.load(read_file)
try:
    last_id = data[-1]['id']
except IndexError:
    last_id = 1

print(last_id)





def main():
    print("TASK SCHEDULER MENU:\n"
          "1. List Task\n"
          "2. Add Task\n"
          "3. Update Task\n"
          "4. Delete Taks")

    menu = input("Select Menu (1-4) : ")

    if menu == "1" and "list":
        list_task()
    elif menu == '2':
        add_task()
    elif menu == '3':
        update_task()
    elif menu == '4':
        delete_task()
    else:
        print("\n!!! WRONG INPUT!, Choose only 1-4 !!! \n")
        main()

def add_task():
    print('-Add task-')
    id = last_id + 1
    desc = input('Description :')
    status = "todo"
    task= {'id':id, 'description':desc, 'status':status}

    data.append(task)
    with open(file_path,'w',encoding='utf=8') as file:
        json.dump(data, file, indent=4)
    print('data added succesfully')
    main()

def update_task():
    print("-- update task --")
    task_id = int(input('Input id:'))
    found = False

    for task in data:
        if task['id'] == task_id:
            print(f"ID : {task_id}",'Task description :',task['description'])
            option = input('Status (todo/in progress/ done :')
            if option == "1":
                new_status = 'todo'
            elif option == '2':
                new_status = 'in progress'
            elif option == '3':
                new_status = 'done'
            else:
                print("wrong input")

            task['status'] = new_status
            found = True
            break

    if not found:
        print('id not found')
        update_task()
    else:
        with open(file_path, 'w', encoding='utf=8') as file:
            json.dump(data, file, indent=4)
        print('Data Updated succesfully')
        main()

def delete_task():
    global data
    delete_id = input("Enter task ID to DELETE : ").isdigit()
    new_data = []
    for task in data:
        if task['id'] != delete_id:
            new_data.append(task)
    data =new_data
    main()

def list_task():
    print("Here the lists:")
    print('id', 'description', 'status')

    for task in data:
        print(task['id'], task['description'], task['status'])
    main()





if __name__ == '__main__':
    main()