# Errors found:
# 1. TypeError: student[1] = 24 -> tuples are immutable, so created new tuple
# 2. Logical error: show(23, 'Khadeejah') -> arguments were in reverse order
# 3. TypeError: age_entered > 18 -> input() gives string, need to convert to int
# 4. NameError: total was not defined before print

student = ('Khadeejah', 23, 3.75)
# student[1] = 24 (failed because tuples cannot be modified)
student = (student[0], 24, student[2])
print(student)

def show(name, age):
    print('Name : ', name)
    print('Age : ', age)

# fixed argument order
show('Khadeejah', 24)

age_entered = input('Enter age: ')
# converted string input to int
if int(age_entered) > 18:
    print('Adult')

marks = [90, 85, 78]
# defined total sum of marks
total = marks[0] + marks[1] + marks[2]
print('Average : ', total / 3)
