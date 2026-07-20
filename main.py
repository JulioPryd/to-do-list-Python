from tabulate import tabulate

tasks = []

print("\n==To-do-list==")
def main():
    while True:
        print("\n1. View task")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            if not tasks:
                print("Task empty!")
            else:
                for i, task in enumerate(tasks, start=1):
                    headers= "num", "task"
                    a = f"{i}.{task}"
                    print(tabulate(a, headers=headers))

        elif choice == "2":
            new_task = input("Enter your task: ")
            tasks.append(new_task)
            print(new_task)
        
        elif choice == "3":
            if not tasks:
                print("No task to delete")
                continue
            for i, task in enumerate(tasks, start=1):
                print(f"{i}.{task}")
            try:
                num = input("Enter your number: ")
                removed = num.pop(num -1)
                print("Enter a number to delete: ")
            except (ValueError, IndexError):
                print("Invalid task number")

        elif choice == "4":
            print("Good bye...")
            break            
                    

main()            