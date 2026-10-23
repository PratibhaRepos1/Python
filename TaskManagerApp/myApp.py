""" Task Manager App - To Do List
"""
user_input = 'Enter a todo:'

# todo1 = input(user_input)
# todo2 = input(user_input)
# todo3 = input(user_input)

# todos = [todo1,todo2,todo3]
# print(todos)
# print(type(todos))

todos = []
# while loop
while True:
    todo = input(user_input)
    todos.append(todo.capitalize())
    print(todos)