a = [1, 2, 3]
b = [4, 5, 6]
c = list(zip(a, a, b))
print(c)


def fun1(x, y):
    z = x + y
    return z


print(fun1(2, 3))

fun2 = lambda x, y: x * y
print("z=", fun2(2, 3))

print(list(map(fun1, [2, 8], [8, 1])))
