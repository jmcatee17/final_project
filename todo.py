import argparse
import pickle
from datetime import datetime
import pytz
import os
from pathlib import Path
import math

class Task:
    """Representation of a task

      Attributes:
              - created - date
              - completed - date
              - name - string
              - unique id - number
              - priority - int value of 1, 2, or 3; 1 is default
              - due date - date, this is optional
    
    """
    def __init__(self, name, largest_task, priority, due_date):
        """Initialize constructor"""
        self.name = name
        self.priority = priority
        # Unique id's are integers to easily view metadata about number of tasks and which task user is on.
        self.unique_id = largest_task + 1
        self.created = self.calculate_datetime()
        self.completed = False
        if due_date != None:
            self.due_date = self.clean_due_date(due_date)
        else:
            self.due_date = due_date
    
    def calculate_datetime(self):
        """This function calculates the current time in Chicago timezone and returns it as a datetime object"""
        # defining the timezone - source: https://www.geeksforgeeks.org/python/working-with-datetime-objects-and-timezones-in-python/
        # Program is designed to work with Chicago timezones
        tz = pytz.timezone('America/Chicago')
        dt = datetime.now(tz = tz)
        return dt
    
    def calculate_age(self):
        """This function calculates the age of a task from now"""
        # defining the timezone - source: https://www.geeksforgeeks.org/python/working-with-datetime-objects-and-timezones-in-python/
        # Program is designed to work with Chicago timezones
        tz = pytz.timezone('America/Chicago')
        now = datetime.now(tz = tz)
        # Source: https://stackoverflow.com/questions/151199/how-to-calculate-number-of-days-between-two-given-dates
        delta = now - self.created
        days = delta.days
        return days
    
    def clean_due_date(self, due_date):
        """This function takes in user input due date in and converts to datetime object"""
        #Source: https://docs.python.org/3/library/datetime.html
        date_str = due_date
        date_obj = datetime.strptime(date_str, "%m/%d/%Y")
        return date_obj

    def __str__(self):
        """This function overwrites the default behavior when a print statement is called on the Task object"""
        return f"name : {self.name}, priority : {self.priority}, id : {self.unique_id}, created : {self.created}, completed : {self.completed}, due_date : {self.due_date}"

class Tasks:
    """Representation of a series of tasks

      Attributes:
              - created - date
              - completed - date
              - name - string
              - unique id - number
              - priority - int value of 1, 2, or 3; 1 is default
              - due date - date, this is optional
    
    """
    def __init__(self):
        self.tasks = self.read_pickle_tasks()

    # Task Open
    
    # Before exits - resave all tasks to pickle file

    # Most of logic in tasks class

    def pickle_tasks(self):
        """Pickle your task list to a file"""
        # Ensure at root home directory
        os.chdir('/Users/jacksonmcatee')
        with open('todo.pickle', 'wb') as f:
            pickle.dump(self.tasks, f)

    def read_pickle_tasks(self):
        """Read pickled tasks if they exist"""
        # Ensure at root home directory
        os.chdir('/Users/jacksonmcatee')

        # Check if File exists:
        # Source: https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions
        my_file = Path('/Users/jacksonmcatee/todo.pickle')
        if my_file.is_file():
            # file exists
            with open('todo.pickle', 'rb') as f:
                tasks = pickle.load(f)
            # Return List of Pickled tasks
            return tasks
        else:
            # Return empty list (no tasks)
            return []

    def list(self):
        """This method prints"""
        print('ID   Age  Due Date   Priority   Task')
        print('--   ---  --------   --------   ----')

        # Loop through each task and print to console
        for task in self.tasks:
            # Only print uncompleted tasks
            if task.completed == False:
                id = task.unique_id
                # Add space for formatting smaller task numbers
                if id < 10:
                    id = str(id) + ' '
                else:
                    id = str(id)
                age = task.calculate_age()
                
                # Add space for formatting smaller task numbers
                if age < 10:
                    age = str(age) + 'd '
                else:
                    age = str(age) + 'd'

                # Source: https://stackoverflow.com/questions/17245612/formatting-time-as-d-m-y
                if task.due_date == None:
                    due_date = '-        '
                else:
                    due_date = task.due_date.strftime('%m/%d/%Y')
                priority = task.priority
                priority = ' ' + str(priority)
                name = task.name
                print(f'{id}   {age}  {due_date} {priority}         {name}')

    def report(self):
        pass

    def delete(self, delete_id):
        """This method removes the element from the tasks list with the corresponding id"""
        # Loop through each task
        for task in self.tasks:
            # Remove element if id matches
            if task.unique_id == delete_id:
                self.tasks.remove(task)
        # Print metadata to console
        print(f'Deleted task {delete_id}')

    def done(self):
        pass

    def query(self):
        pass
    
    def max_id(self):
        if len(self.tasks) == 0:
            return 0
        # Get greatest task number. O(N) run time
        largest_task = -math.inf
        for task in self.tasks:
            if task.unique_id > largest_task:
                largest_task = task.unique_id
        return largest_task

    def add(self, name, priority, due):
        # Since we do not 
        largest_task = self.max_id()
        # Create task with specified input parameters (defaulted to None when optional)
        task = Task(name, largest_task, priority, due)
        
        # Append task to list
        self.tasks.append(task)

        # Print metadata to console
        print(f'Created task {task.unique_id}')



def main():
    parser = argparse.ArgumentParser(description = "Update your ToDo list.")
    parser.add_argument("--add", type = str, required = False, help = "a task string to add to your list")
    parser.add_argument("--due", type = str, required = False, help = "due date in dd/MM/YYYY format")
    parser.add_argument("--priority", type = int, required = False, default = 1, help = "priority of task; default value is 1")
    parser.add_argument("--query", type = str, required = False, nargs = "+", help = "query")
    parser.add_argument("--delete", type = int, required = False, help = "deletes task with unique_id from tasks list")
    parser.add_argument("--list", action = 'store_true', required = False, help = "list all tasks that have not been completed")
    parser.add_argument("--report", help = "list all tasks that have not been completed")

    # Parse the arguments
    args = parser.parse_args()

    # Read out arguments (note the types)
    print("Add:", args.add)
    print("Due:", args.due)
    print("Priority:", args.priority)
    print("List:", args.list)
    print("Query:", args.query)

    task_list = Tasks()

    if args.add:
        task_list.add(args.add, args.priority, args.due)

    elif args.list:
        task_list.list()

    elif args.delete:
        task_list.delete(args.delete)
    # elif args.report:
    #     print("Print out Report")

    print("These are all the tasks in the Tasks() object")
    for t in task_list.tasks:
        print(t)

        ## Do something with data based on the user command

        task_list.pickle_tasks()

if __name__ == "__main__":
    main()