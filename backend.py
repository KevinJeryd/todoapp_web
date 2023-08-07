from helper_functions import get_todolist, write_todos
import time

global_filepath = 'todo_data.txt'


def add_todo(todolist, input_todo):
    todolist.append(input_todo + '\n')
    write_todos(todolist)
    print('\n')


def print_todos(todolist):
    for todo_index, todo in enumerate(todolist):
        todo = todo.strip()
        output = f"{todo_index + 1}. {todo.capitalize()}"
        print(output)


def edit_todo(todolist, old_todo, new_todo):
    edit_index = todolist.index(old_todo)
    todolist[edit_index] = new_todo + '\n'
    write_todos(todolist)


def complete_todo(todolist, completed_todo):
    todolist.remove(completed_todo)
    write_todos(todolist)


''' # Commandline edit-function
def edit_todo(todolist):
    number = input("Which item do you want to edit? (Enter a number): ")

    try:
        if number.isdigit():
            new_todo = input("What should the new todo be?: ") + '\n'
            old_todo = todolist[int(number) - 1]
            todolist[int(number) - 1] = new_todo

            write_todos(todolist)

            print("Todo number: " + number + " has been changed from: " + old_todo.strip() + " to: " + new_todo.strip())
        else:
            print("'" + number + "'" + " Is not a number.")
    except IndexError:
        print('ERROR: --There is no item with that index in the list--')
'''

'''
# CommandLine Complete_Todo function
def complete_todo(todolist):
    index_removals = input("Which item do you want to remove? Input a number or several separated by ', ': ")
    numbers = "".join(c for c in index_removals if c.isdecimal())  # Removes ',' from the list

    try:
        if numbers.isdigit() and ',' not in index_removals:
            removed_item = todolist.pop(int(index_removals) - 1)
            write_todos(todolist)
            print(removed_item + " has been removed.")
        elif ',' in index_removals and all(isinstance(int(element), int) for element in numbers):
            # Probably better solutions but this does so the program removes from the top
            # Which makes it so the indexes doesn't move around on remove
            unsorted_num_arr = []
            for unsorted_num in numbers:
                unsorted_num_arr.append(unsorted_num)

            sorted_num_arr = sorted(unsorted_num_arr, reverse=True)

            for num in sorted_num_arr:
                removed_item = todolist.pop(int(num) - 1)
                write_todos(todolist)
                print(removed_item.strip() + " has been removed.")
        else:
            print("'" + index_removals + "'" + " Is not a number.")
    except IndexError:
        print('ERROR: --There is no item with that index in the list.--')
'''

'''
def loop():
    while True:
        current_list_on_disk = get_todolist()
        user_action = input("What do you want to do? Options: \n"
                            "'Add' + 'TODO' (1)\n"
                            "'Show' todos (2)\n"
                            "'Edit' a todo (3)\n"
                            "'Complete' todo (4)\n"
                            "Exit Program (Any other input) \n")

        if user_action.title().startswith('Add') or user_action.startswith('1'):
            add_todo(current_list_on_disk, user_action.title().strip('Add') + '\n')  # Could do user_action[4:]
        elif user_action.title().startswith('Show') or user_action == '2':
            print_todos(current_list_on_disk)
            print('\n')
        elif user_action.title().startswith('Edit') or user_action == '3':
            print_todos(current_list_on_disk)
            edit_todo(current_list_on_disk)
            print('\n')
        elif user_action.title().startswith('Complete') or user_action == '4':
            print_todos(current_list_on_disk)
            complete_todo(current_list_on_disk)
            print('\n')
        else:
            print("Exiting Program...")
            return current_list_on_disk


def main():
    time_now = time.strftime("%b %d, %Y %H:%M:%S")
    print("Today's date: " + time_now + '\n')
    loop()

    
main()
'''
