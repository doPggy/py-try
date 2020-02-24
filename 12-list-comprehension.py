# 产生式表达式
## 循环生成 list
values = [10, 21, 3, 44, 5]
squares = []
for x in values:
    squares.append(x ** 2)
print(squares)

## 列表生成式生成 list
values = [10, 21, 3, 44, 5]
squares = [x ** 2 for x in values]
print(squares)
'''还可以带判断语句'''
squares = [ x ** 2 for x in values if x >= 10 ]
print(squares)
## 生成集合字典
values = [10, 21, 3, 44, 5]
squares = { x ** 2 for x in values }
print(squares)
squares = { x:x ** 2 for x in values }
print(squares)


## 一个应用
'''这样不会一次性把列表生成'''
total = sum(x ** 2 for x in values)
print(total)
