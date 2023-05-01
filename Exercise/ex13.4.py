def get_nr_items(user_input):
    items = user_input.split(',')
    return len(items)


names = input("Enter names seperated by comma(no spaces:")
number_of_names = get_nr_items(names)
print(number_of_names)