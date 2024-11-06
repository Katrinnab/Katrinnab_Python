lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
print(*[i for i in lst if i < 30 and i % 3 == 0])
