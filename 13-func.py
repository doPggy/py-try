# 函数
## 定义
def add(x, y):
    return x + y
## 使用
print(add(2, 3))
print(add(y = 3, x = 2))
print(add(2, y = 3))


## 参数默认值
def q(x, a = 1, b = 0, c = 0):
    return a * x ** 2 + b * x + c
print(q(2))
print(q(2, b = 3))
'''给默认参数的赋值，从左到右赋值'''
print(q(2, 1, b = 3))
'''
比如这样，
print(q(2, 1, b = 3, 3))
就不行，b = 3 和接下来的 3 重复位置
'''

## 接收不定参数
def add(x = 1, y = 2, *args):
    print(*args)
    # for x in args:
    #     print(x)
'''默认参数在这里其实不起作用了，都会被传入 x，y 参数中，剩下的传入 args'''
add(1, 2, 3, 4)
add(*[1, 2, 3, 4])

def add(x = 0, y = 1, **kwargs):
    print(x, y)
    print(kwargs)
add(1, k = 2, z = 3)
add(k = 2, z = 3)
add(1, 2, **{'k' : 2, 'z' : 3})


## map
'''将传入序列每个元素都经过 map_func 处理一遍'''
def map_func(x):
    return x ** 2

print(list(map(map_func, [1, 2, 3, 4, 5])))

def map_func(x, y):
    return x + y
m = list(map(map_func, [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))
print(m)
