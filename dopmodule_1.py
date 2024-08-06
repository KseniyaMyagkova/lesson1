grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_=(sorted(students))
print(list_)
def average(*args): return([sum(x) / len(x) for x in args])
a = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
b=(average(*a))
result = [int(item) for item in b]
c=result
print(c)
print("Original key list is : " + str(list_))
print("Original value list is : " + str(c))
res = {}
for key in list_:
    for value in c:
        res[key] = value
        c.remove(value)
        break
print("Resultant dictionary is : " + str(res))

