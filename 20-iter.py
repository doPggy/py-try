## 迭代器对象
x = [1, 2, 3]
'''
[] 就是一个可迭代对象,
for 中返回一个迭代器对象
'''
for n in x:
    print(n)
d = { 1:1, 2:2 }
# i = d.iterkeys()
# print(type(i))
'''
__iter__() 返回一个迭代器对象
'''
i = x.__iter__()
j = x.__iter__()
print(next(i))
print(next(j))

## 自定义迭代器
class RListIter(object):
    def __init__(self, list):
        self.list  = list
        self.index = len(list)

    '''自己是可迭代对象 返回迭代器'''
    def __iter__(self):
        return self

    '''是迭代器 迭代方法'''
    def __next__(self):
        self.index -= 1
        if self.index >= 0:
            return self.list[self.index]
        else:
            raise StopIteration

x = [1, 2, 3, 4, 5, 6]
it = RListIter(x)
print("-----")
for i in it:
    print(i)

'''可迭代对象和迭代器分开'''
class AIter(object):
    def __init__(self, list):
        self.list = list
        self.index = len(list)
    def __next__(self):
        self.index -= 1
        if self.index >= 0:
            return self.list[self.index]
        else:
            raise StopIteration
        

class A(object):
    def __init__(self, list):
        self.list = list
    def __iter__(self):
        return AIter(self.list)

print("-----")
for i in A([2, 3, 4, 5]):
    print(i)
    
    
