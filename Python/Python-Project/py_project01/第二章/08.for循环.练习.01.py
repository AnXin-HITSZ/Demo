n = int(input("请输入等腰直角三角形的直角边的边长："))

for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()
