import json
import os
from datetime import datetime
from pprint import pprint

# File path 
FILEPATH = 'data.json'

# Read data from JSON file 
def read_data_():
    if os.path.exists(FILEPATH):
        try:
            if os.stat(FILEPATH).st_size == 0:
                return {}
            with open(FILEPATH, 'r') as json_file:
                data = json.load(json_file)
            return data
        except json.JSONDecodeError:
            print("Error decoding JSON. Returning empty data.")
            return {}
    else:
        return {}

# Store data in JSON file
def store_data_json(data):
    with open(FILEPATH, 'w') as store_file:
        json.dump(data, store_file, indent=4)

# Generate ID
def generate_id(data):
    return str(len(data) + 1)

# Add expense
def add_expense(name, expense):
    data = read_data_()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format the date
    expense_id = generate_id(data)
    
    try:
        expense = float(expense)  # Convert expense to float
    except ValueError:
        print("Expense must be a valid number.")
        return
    
    current_data = {
        "id": expense_id,
        "date": current_time,
        "Expense": name,
        "Expense Price": expense
    }
    
    data[expense_id] = current_data
    store_data_json(data)
    print(f"Expense '{name}' added successfully.")

# Update expense
def update_expens(id, new_name, new_expense):
    data = read_data_()
    if id in data:
        data[id]['Expense'] = new_name
        data[id]['Expense Price'] = new_expense
        store_data_json(data)
        print(f"Task with ID {id} has been updated.")
    else:
        print(f"Task with ID {id} not found.")

# Remove a task
def remove_task(id):
    data = read_data_()
    if id in data:
        del data[id]  # Delete the task with the given ID
        store_data_json(data)
        print(f"Task with ID {id} has been removed.")
    else:
        print(f"Task with ID {id} not found.")

def view_expenses_by_month(month, year):
    data = read_data_()
    expenses_for_month = []
    
    for entry in data.values():
        if 'date' not in entry:
            print(f"Skipping entry with missing 'date': {entry}")
            continue  # Skip this entry if it doesn't have a 'date' key
        
        try:
            # Parse the stored string date into a datetime object
            entry_date = datetime.strptime(entry['date'], "%Y-%m-%d %H:%M:%S")
            
            # Check if the month and year match the user's input
            if entry_date.month == month and entry_date.year == year:
                expenses_for_month.append(entry)
        except ValueError as e:
            print(f"Error parsing date for entry {entry['id']}: {e}")
    
    if expenses_for_month:
        print(f"\nExpenses for {month}/{year}:")
        pprint(expenses_for_month)
    else:
        print(f"No expenses found for {month}/{year}.")