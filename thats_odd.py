n = int(input()) #this is for sum even numbers.
sum = 0
for _ in range(n):
    a = int(input())
    list1 = []
    list1.append(a)

    for _ in list1:
        if _ % 2 == 0:
            sum += _

print(sum)

