
students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies

# create a function that takes a list of students and prints:
#  - how many candies they have on average

def candies(students):

    for i in range(0, len(students), 1):
        if students[i]['candies'] > 4:
            print(students[i]['name'])
candies(students)

def average(students):
    sum = 0

    for i in range(0, len(students), 1):
        sum += students[i]['candies']
    sum = sum / len(students)

    return sum
print(average(students))
