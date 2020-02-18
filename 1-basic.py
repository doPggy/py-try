# 简单数学运算
print(2 + 2)


# 字符串
s = "hello world"
print(s)


## 使用三引号包含多行文字的字符串
s = """hello
world
"""
print(s)

## 字符串加法
s = "hello" + "world"
print(s)

## 字符串索引
print(s[0])
print(s[-1])
print(s[0:5]) # [0, 5)

# 列表
a = [1, 2., 'hello', 5 + 1.]
print(a)
print(a + a)

# set
s = {2, 3, 4, 2}
print(s)
print(len(s))
s.add(1)
print(s)
## 集合交
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
print(a & b)
## 集合并
print(a | b)
## 集合差
print(a - b)
## 对称差
print(a ^ b)


# dict
d = {'dog' : 5, 'cat' : 4 }
print(d.keys())
print(d.values())
print(d.items())