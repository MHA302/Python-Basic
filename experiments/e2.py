user_prompt = "Please Enter To-DO:"

todos = []

while True:
    todo = input(user_prompt)
    print(todo.title())
    # WE use APPEND Method to add every TODO  that is entered by the user
    todos.append(todo)
    print(todos)