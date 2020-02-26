## 修饰符
'''
修饰符是一个函数，用于接收一个函数，输出一个函数
'''
def dec(f):
    print("i am decorating function", id(f))
    return f

declen = dec(len)

def loud(f):
    def new_func(*args, **kw):
        print('call with', args, kw)
        rtn = f(*args, **kw)
        print('return : ', rtn)
        return rtn
    return new_func
loudlen = loud(len)
loudlen([1, 2, 3])


## @ 用来使用修饰符
def foo(x):
    print(x)
foo = dec(foo)

@dec
def foo(x):
    print(x)
@loud
def foo(x):
    print(x)
foo(33)
print('----')
'''从下到上,链式修饰'''
@loud
@dec
def foo(x):
    print(x)
foo(333)


## 修饰器工厂
print("--------")
def super_loud(name):
    print(name)
    def loud(f):
        def new_func(*args, **kw):
            print("args", args)
            print("kw", kw)
            return f(*args, **kw)
        return new_func
    return loud
@super_loud("foo_super")
def foo(x):
    print(x)
foo(22)