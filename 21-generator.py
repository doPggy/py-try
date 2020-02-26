# 生成器

def collatz(n):
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        yield n

g = collatz(22)
'''生成器也算一种迭代器'''
print("---------------")
print(g)
print(next(g))
print(next(g))
print(next(g))
print("---------------")
for r in collatz(22):
    print(r)