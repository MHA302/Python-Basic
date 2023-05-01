year_of_birth = input("Enter your birth  Year:")


def get_age(year_of_birth, current_year = 2023):
    age = int(year_of_birth)
    year_running = int(current_year)
    user_age = year_running - age
    return f"Your are {user_age} years old"


print(get_age(year_of_birth))
