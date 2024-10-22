from pprint import pprint
from util import add_expense, update_expens, remove_task, read_data_, view_expenses_by_month
def main():
    while True:
        print("\nSelect your task")
        print("add")
        print("update")
        print("remove")
        print("view")
        print("month")
        print("exit")

        choice = input("What's the action you want to perform? ")

        if choice == "add":
            name = input("Enter task name: ")
            expense = input("Enter task expense: ")
            add_expense(name, expense)
            print("Task added.")
        elif choice == "update":
            id = input("Enter task ID to update: ")
            new_name = input("Enter new task name: ")
            new_expense = input("Enter new expense: ")
            update_expens(id, new_name, new_expense)
        elif choice == "remove":
            task_id = input("Enter task ID to remove: ")
            remove_task(task_id)
        elif choice == "view":
            print("Current data in JSON file:")
            pprint(read_data_())
        elif choice == "month":
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year (e.g., 2024): "))
            view_expenses_by_month(month, year)
        elif choice == "exit":
            print("Exiting the program.")
            break
        else:
            print("Invalid option selected")

        # Display the current contents of the JSON file
        print("\nCurrent data in JSON file:")
        pprint(read_data_())

if __name__ == "__main__":
    main()