def get_age(year_of_birth, current_year=2023):
    age = current_year - year_of_birth
    return age

birth = int(input("What is your asge:"))
age = get_age(birth)

if age <= 120:
    print(age)
else:
    print('Hold on you are Elder than my grandpa!')


