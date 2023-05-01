todos = []
while True:
    user_In = input("Type add, show, edit or exit:")
    user_In = user_In.strip()
    match user_In:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'edit':
            number = int(input("Enter number of ToDO to Edit :"))
            number = number-1
            new_todo = input("Enter new todo:")
            todos[number] = new_todo
        case 'exit':
            break
print("Bye")