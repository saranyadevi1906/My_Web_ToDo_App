FILEPATH = "todo_tasks.txt"

def file_read(filename = FILEPATH):
    """
    Read a file and store data ina  list
    :param filename:
    :return todo_list:
    """
    with open(filename, 'r') as file_local:
        todo_list_local = file_local.readlines()
    return todo_list_local


def file_write(todo_arg,filename= FILEPATH):
    """ Write todo items to file """
    with  open(filename, 'w') as file:
        file.writelines(todo_arg)


#print(__name__)
#print(type(__name__))
if(__name__ == "__main__"):
    print("Hi! functions are executed!")
