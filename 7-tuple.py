# 基本操作
'''可索引，不可修改'''
t = (10, 11, 12, 13, 14)
print(t)
print(t[0])
print(t[1:3])
a = [1, 2, 3]
at = tuple(a)
print(at)
#单元素元组生成
t = (10,)
tt = (10)
print(type(t))
print(type(tt))
# 元组方法
t = (1, 2,   3, 40, 5, 5, 5)
print(t.count(5))
print(t.index(40))