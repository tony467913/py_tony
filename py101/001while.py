condition = 0
while condition < 10:
    print(condition)
    condition = condition + 1


a = range(10)
while a:
    print(a[-1])
    a = a[:len(a)-1]