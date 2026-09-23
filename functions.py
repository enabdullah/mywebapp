from sys import modules
FILEPATH = "todos.txt"

def get_todos(filepath= FILEPATH):
    with open(filepath, "r") as file:
        list_read = file.readlines()
    return list_read
def write_todos(list_write, filepath=  FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(list_write)
    #return list_write # no need use the return no data need to return
# print("hello")
# print(__name__)
# if __name__ == "__main__":
#     print(get_todos("../todos.txt"))
#     print("Hello World")

