def outer(a):
#    a += 1
    def inner(b):
        nonlocal a
        a += 1
        return a+b
    return inner
demo1 = outer(1)
print(demo1(10))
print(demo1(10))
print(demo1(10))
print(demo1(10))
print(demo1(10))
