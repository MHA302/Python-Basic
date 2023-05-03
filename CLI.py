# from functions import get_todos, add_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is:", now)
while True:
    user_action = input("Type Add, Show, Edit, Complete or exit: ")
    user_action = user_action.strip()
    if user_action.startswith('add'):
        todo = user_action[4:]
        # calling the get_todos function
        todos = functions.get_todos()
        # Adding the new todo in todos list
        todos.append(todo + "\n")
        # calling the add_todos function
        functions.add_todos(todos)
    elif user_action.startswith('show'): 
        # calling the get_todos function
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1 }-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            # calling the get_todos function
            todos = functions.get_todos()
            new_todo = input("Enter New ToDo:")
            todos[number] = new_todo + '\n'
            # calling the add_todos function
            functions.add_todos(todos)
        except ValueError:
            print("Wrong Command!")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            # calling the get_todos function
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index] .strip('\n')
            todos.pop(number - 1)
            # calling the add_todos function
            functions.add_todos(todos)
            message = f"Todo :{todo_to_remove} was Removed from the list."
            print(message)
        except ValueError:
            print("The number Does not match to any ITEM")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Command Not Valid")
print("Bye")
