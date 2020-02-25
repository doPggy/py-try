## 函数是基本类型
'''
可作为变量作为 dict 的 value
作为参数
'''

def square(x):
    return x * x
def cube(x):
    return x * x * x

funcs = {
    'square' : square,
    'cube'   : cube,
}

x = 2
for func in sorted(funcs):
    print(func, funcs[func](x))

## 函数参数
'''传入引用，所以修改生效'''
def mod_f(x):
    x[0] = 99
    # return x
def mod_f_(x):
    x = [1, 3, 4]

x = [1, 2, 3]
print(x)
mod_f(x)
print(x)
mod_f_(x)
print(x)
### 默认参数
'''
默认参数绑定在函数定义的时候，每次使用默认参数其实是使用同一个引用
'''
def f(x = []):
    x.append(1)
    print(x)
f()
f()
f()
f([3, 3, 3])

## 高阶函数
'''以函数作为参数或返回一个函数，叫做高阶'''
### map
'''
map(f, sq) 相当于 [f(s) for s in sq]
'''
def square(x):
    return x * x
print(list(map(square, [1, 2, 3, 4])))

### filter
'''
filter(f, sq)
只返回 f 为 True 的 sq 中的 s
'''
def is_even(x):
    return x % 2 == 0
print(list(filter(is_even, [1, 2, 3, 4, 5, 6])))
print(list(map(square, filter(is_even, [1, 2, 3, 4, 5, 6]))))

### reduce
from functools import reduce
def my_add(x, y):
    return x + y
'''
1 + 2 = 3
3 + 4 = 7
'''
print(reduce(my_add, [1, 2, 3, 4]))


### 闭包
def make_counter(t):
    x = [t]
    def counter():
        x[0] += 1
        return x[0]
    return counter

c = make_counter(1)
print(c())
print(c())
print(c())


## 匿名函数
'''
lambda <var>:<exp>
'''
print(list(map(lambda x : x ** 2, range(5))))
'''
x ** 2 for x in range(1, 10)
返回的是 genrator
'''
print([x ** 2 for x in range(1, 10)])