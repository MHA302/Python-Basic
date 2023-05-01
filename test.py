def greet(message):

    new_message = message.capitalize()
    return new_message
user_entry = input("WHat greeting entry you want:")
greeting = greet(user_entry)
print(greeting)