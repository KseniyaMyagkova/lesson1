first=input('Введите целое число 1: ')
a=int(first)
second=input('Введите целое число 2: ')
b=int(second)
third=input('Введите целое число 3: ')
c=int(third)
if a==b and a==c:
    print(3)
elif a==b or a==b or b==c:
    print(2)
else:
    print(0)