#Todo list program

tasks= []

def show_tasks():
   if tasks:
      print ("\nYour Tasks:")
      for i, task in enumerate(tasks, 1):
          print (f"{i}.{task}")
   else:
        print("No tasks in your list!")


def add_task():
    task = input("Enter the task:")
    tasks.append(task)
    print(f"Task '{task}' added.")


def delete_task():
     show_tasks()
     try:
        task_number = int(input ("Enter the task number to delete: "))
        deleted_task = tasks.pop(task_number - 1)
        print (f"Task '{deleted_task}' deleted. ")
     except (IndexError, ValueError):
       print ("Invalid task number")

while True:
      print ("\n1. Show tasks")
      print ("2. Add task")
      print ("3. Delete task")
      print ("4. Exit")

      choice = input("Select an option (1/2/3/4): ")

      if choice == '1':
          show_tasks()
      elif choice == '2':
          add_task()
      elif choice == '3':
          delete_task()
      elif choice == '4':
          print("Goodbye")
          break
      else:
          print("Invalid choice.")
