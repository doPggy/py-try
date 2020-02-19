# 列表生成
l = [1, 2.0, 'h']
print(l)
## 生成空列表
l = []
l = list()
print(l)

# 列表操作
l = [1, 2.0, 'h']
## 长度
print(len(l))
## 加法和乘法
a = [1, 2, 3]
b = [3.2, 'hell']
'''顺序连接'''
print(a + b)
'''重复连接'''
print(a * 2)
## 索引
a = [1, 2, 3]
a[0] = 2
print(a)

## 切片
'''可利用切片改原 list 数据'''
a = [10, 11, 12, 13, 14, 15]
'''对于连续的一段分片，可以不等长替换'''
a[1:4] = [1, 2, 3 ,4 ,5]
print(a)
'''对于不连续的一段分片，等长替换'''
a = [10, 11, 12, 13, 14, 15]
a[1::2] = [1, 3, 5]
print(a)

## 删除元素
a = [1002, 'a', 'b', 'c']
del a[0]
print(a)
del a[1:]
print(a)
a = ['a', 1, 'b', 2, 'c']
del a[1::2]
print(a)

## 测试从属关系
a = [10, 11, 12, 13, 14]
print(10 in a)
print(10 not in a)
s = 'hello w'
print('he' in s)


# 列表方法
## 元素出现个数
a = [11, 10, 11, 12, 13, 14]
print(a.count(11))
## 元素的位置
'''只会返回第一个出现的位置'''
print(a.index(11))
## 添加元素
a = [10, 11, 12]
a.append(11)
a.append([11, 12])
print(a)
## 添加序列
a = [10, 11, 12]
a.extend([1, 2, 3, 4])
print(a)
## 插入元素
a = [10, 11, 12, 13, 11]
a.insert(3, 'a')
print(a)
## 移除元素
a = [10, 11, 12, 13, 11]
'''移除第一个 11'''
a.remove(11)
print(a)
## 弹出元素
a = [10, 11, 12, 13, 11]
print(a.pop(2))
## 排序
a = [10, 1, 11, 13, 11, 2]
a.sort()
print(a)
a = [10, 1, 11, 13, 11, 2]
aa = sorted(a)
print(a)
print(aa)
## 列表反向
a = [1, 2, 3, 4, 5, 6]
a.reverse()
print(a)
a = [1, 2, 3, 4, 5, 6]
b = a[::-1]
print(b)
'''
直接修改切片可以改变原 list
但是赋值给另一变量，就不再影响
'''
b[1] = 100
print(a)
a[1:2] = [11]
print(a)
