FILEPATH = 'todo_data.txt'


def get_todolist(local_filepath=FILEPATH):  # Just put in default parameter because learning o.o
    """
    Reads a text file on disk and returns it as a list of to-do items.
    """
    with open(local_filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todolist, local_filepath=FILEPATH):
    with open(local_filepath, 'w') as file:
        file.writelines(todolist)


# __name__ can equal two things:
# 1. It will equal __main__ if it's inside the file that was executed directly
# 2. It will equal the name of the file, in this case "helper_functions", if it's not inside the file that was run
# That way you can have code that's only run when you execute that file only and not if it's imported somewhere
# Kinda...
if __name__ == '__main__':
    print('You have run this script directly')
