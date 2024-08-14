#numbers1=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#numbers2=[1,2,3,4,5,6,7,8,9]
def generate_password(n):
    password = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                password += str(i) + str(j)
    return password

for n in range(3, 21):
    password = generate_password(n)
    print(f"{n} - {password}")