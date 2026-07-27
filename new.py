from sys import getrefcount


def true_enough(n):
    dr = 3
    i = 0
    while i < n:
        yield i
        print(getrefcount(i))
        i += 3

res =0
for i in true_enough(50):
    print(getrefcount(res))
    res += i


print(f"This is the result of generator: {res}")
print(getrefcount(res))

print(getrefcount(i))
