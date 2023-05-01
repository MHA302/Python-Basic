def get_max():
    grades = [9.6, 9.2, 9.7]
    high = max(grades)
    low = min(grades)
    return f"Max : {high}, Min: {low}  \nWhere {high} is maximum and {low} is the minimum"


grade = get_max()
print(grade)
