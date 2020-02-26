# 修饰符使用

## @classmethod
print('------@classmethod')
class Foo(object):
    '''对象方法 -> 类方法'''
    @classmethod
    def bar(cls, x):
        print(x)
    def __init__(self):
        pass
Foo.bar(222)


## @property
print('------property')
class Foo(object):
    '''对象方法 -> 类方法'''
    @classmethod
    def bar(cls, x):
        print(x)
    def __init__(self, data):
        self.data = data
    '''
    只读，不可写
    '''
    @property
    def x(self):
        return self.data
foo = Foo(23)
print(foo.x)
'''
foo.x = 1, 不可以
'''
class Foo(object):
    '''对象方法 -> 类方法'''
    @classmethod
    def bar(cls, x):
        print(x)
    def __init__(self, data):
        self.data = data
    '''
    只读，不可写
    '''
    @property
    def x(self):
        return self.data
    '''
    这样就可以写属性了
    '''
    @x.setter
    def x(self, data):
        self.data = data
foo = Foo(23)
'''主要实现通过对属性的赋值或者调用就能完成操作'''
foo.x = 22222
print(foo.x)

## @wraps
print('------wraps')
'''
使用修饰符时，原函数的元数据都没了，比如 docstring, name 变成新函数名字
'''
def logging_call(f):
    def wrapper(*args, **kw):
        print('call {}'.format(f.__name__))
        return f(*args, **kw)
    return wrapper

@logging_call
def square(x):
    return x * x
print(square(22))
''' __name__ 不是 square'''
print(square.__name__)

import functools
def logging_call(f):
    @functools.wraps(f)
    def wrapper(*args, **kw):
        print('call {}'.format(f.__name__))
        return f(*args, **kw)
    return wrapper
@logging_call
def square(x):
    return x * x
print(square(22))
print(square.__name__)