grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_=(sorted(students))
print(list_)
print("Original key list is : " + str(list_))
print("Original value list is : " + str(grades))
res = {}
for key in list_:
    for value in grades:
        res[key] = value
        grades.remove(value)
        break

# Printing resultant dictionary
print("Resultant dictionary is : " + str(res))

