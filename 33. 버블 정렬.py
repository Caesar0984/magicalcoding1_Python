#버블 정렬 알고리즘
a = [7, 6, 9, 5, 8]

for i in range(0, 5):
    for j in range(0, 4 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)

#1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(0, 10):
    for j in range(0, 9 - i):
        if a[j] < a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)