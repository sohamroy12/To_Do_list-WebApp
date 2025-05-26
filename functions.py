
FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items stripped of newlines
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.read().splitlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file,
    adding newlines.
    """
    todos_arg = [arg + '\n' for arg in todos_arg]
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)