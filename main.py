import os

# Name of the text file where tasks will be saved permanently
TASKS_FILE = "my_tasks.txt"

def load_saved_tasks():
    """
    Reads the text file and loads the saved tasks into a list.
    Returns an empty list if the file doesn't exist yet.
    """
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:  # Skip empty lines
                    tasks.append(line)
    return tasks

def save_to_archive(actual_list):
    """
    Takes the current task list and overwrites the text file
    to keep the data updated.
    """
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        for item in actual_list:
            f.write(item + "\n")

def main():
    print(".-..-..-..-..-..-..-..-..-..-..-..-..-..-.")
    print("         WELCOME TO THE TASK MANAGER  ")
    print(".-..-..-..-..-..-..-..-..-..-..-..-..-..-.")

    # Initialize the list with previously saved tasks
    task_list = load_saved_tasks()

    on = True
    while on:
        total_tasks = len(task_list)
        print(f"\nYour current list ({total_tasks} pending):")
        
        # Show a special message if there are no pending tasks
        if not task_list:
            print("[You are free, there are no pending tasks at the moment]") 
        else:
            for num, task in enumerate(task_list, start=1):
                print(f" {num}) {task}")
        print("--------------------------------")

        print("1. Note new task")
        print("2. Cross off task completed")
        print("3. Clear all tasks")
        print("4. Close the program")
        print("----------------------------------")
        
        option = input("Choose the option you need (1-4): ").strip()

        # Option 1: Add a new task to the list
        if option == "1":
            new_task = input("Enter the new task: ").strip()
            if new_task:
                due_date = input("Enter due date (or press Enter to skip): ").strip()
                # Format the task depending on whether there is a due date or not
                if due_date:
                    full_task = f"{new_task} [Due: {due_date}]"
                else:
                    full_task = new_task
                
                task_list.append(full_task)
                save_to_archive(task_list)  # Save changes right away
                print(f"-> Okay, I've already written it down: '{full_task}'")
            else:
                print("Hey, you can't add a task that's empty.")
                
         # Option 2: Mark a task as completed (remove from the list)
        elif option == "2":
            if not task_list:
                print("\nYou have nothing to cross off yet.")
            else:
                try:
                    num_input = input("\nWhat task number did you complete? (or press Enter to go back): ").strip()
                    if num_input: 
                        index = int(num_input) - 1
                        # Check if the number matches a valid task index
                        if 0 <= index < len(task_list):
                            erased = task_list.pop(index)
                            save_to_archive(task_list)
                            print(f"\nSuccessfully crossed out: '{erased}'")
                        else:
                            # Raise error if the number is not on the list
                            raise IndexError
                except ValueError:
                    # Handle error if the user enters letters instead of a number
                    print("Please enter a valid number, not letters.")
                except IndexError:
                    # New block to handle numbers out of range
                    print("That number is not on the list, please try again.") 
        # Option 3: Delete all tasks at once
        elif option == "3":
            if not task_list:
                print("\nThe list is already empty.")
            else:
                confirm = input("Are you sure you want to delete ALL tasks? (y/n): ").strip().lower()
                if confirm == 'y':
                    task_list.clear()
                    save_to_archive(task_list)
                    print("\nAll tasks have been deleted.")
        
        # Option 4: Exit the program
        elif option == "4":
            print("\nSaving everything to the file... See you later!")
            on = False
        else:
            print("\nInvalid option. Choose a number from 1 to 4.")

if __name__ == "__main__":
    main()
