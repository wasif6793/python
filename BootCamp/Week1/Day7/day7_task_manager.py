import os
import json as js
#FIle to store tasks

FILE_NAME="tasks.txt"
def export_tasks_to_json(tasks, filename):
    with open(filename,'w') as file:
        js.dump(tasks, file, indent=4)
#Load tasks from file
def load_tasks():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,"r") as file:
            for line in file:
                task_id,title,status, priority = line.strip().split(" | ")
                tasks[int(task_id)] = {"title":title,"status":status,"priority":priority}
    return tasks

#save tasks to file
def save_task(tasks):
    with open(FILE_NAME,"w") as file:
        for task_id,task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']} | {task['priority']}\n")

#Add a new task
def add_task(tasks):
    title = input("Enter a new task: ")
    task_id = max(tasks.keys(),default=0) + 1
    print("Give Priority: ")
    print("1. Low")
    print("2. Medium")
    print("3. High")
    choice = input("Enter your choice 1,2 or 3: ")
    if choice == '1':
        tasks[task_id] = {"title": title, "status": "incomplete","priority":"Low"}
    elif choice == '2':
        tasks[task_id] = {"title": title, "status": "incomplete", "priority": "Medium"}
    elif choice == '3':
        tasks[task_id] = {"title": title, "status": "incomplete", "priority": "High"}
    else:
        print("Invalid choice... Reassign the task.")
    # tasks[task_id] = {"title":title,"status":"incomplete"}
    print(f"task '{title}' added.")


#View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available...")
    else:
        for task_id,task in tasks.items():
            print(f"{task_id} {task['title']} - {task['status']} - {task['priority']}")

#Mark task as complete
def mark_task_complete(tasks):
    task_id = int(input("Enter task id to mark as complete: "))
    if task_id in tasks:
        tasks[task_id]["status"] = "complete"
        print(f"Task '{tasks[task_id]['title']}' marked as complete")
    else:
        print("task id not found")


#Delete a task
def delete_task(tasks):
    task_id = int(input("Enter task id to mark as complete: "))
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print(f"Task '{deleted_task['title']}' is deleted...")
    else:
        print("task id not found")

#Main Menu
def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager Menu")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark task as complete")
        print("4. Delete a task")
        print("5. Export to json")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice =='1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice =='3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice =='5':
            export_tasks_to_json(tasks,filename="task.json")
        elif choice == '6':
            save_task(tasks)
            print("Good Bye")
            break
        else:
            print("Invalid choice, Try again")

if __name__ == "__main__":
    main()
