'''set 是一个无序序列'''
# 生成
a = set()
print(a)

a = set([12, 22, 33, 33, 4])
'''自动去重'''
print(a)

# 操作
a = {1, 2 ,3, 4}
b = {3, 4 ,5, 6}
## 并集
print(a | b)
'''不修改 a b'''
print(a.union(b))
print(b.union(a))
print(a)
print(b)

## 交集
print(a.intersection(b))
print(b.intersection(a))
print(a & b)
print(a, b)

## 差集
print(a.difference(b))
print(a - b)

## 对称差
'''相同为 0, 不同 为1 -> 两集合都有为 0 ，不同时有为 1'''
print(a.symmetric_difference(b))
print(a ^ b)


## 包含
a = {1, 2, 3}
b = {1, 2}
print(b <= a)
print(b.issubset(a))
print(a >= b)
print(a.issuperset(b))

# 集合方法
## add
s =  {1, 2 ,3}
s.add(4)
s.add(3)
print(s)
## update
s.update([5, 6, 7])
s.update({66, 77})
print(s)
s.remove(66)
print(s)
'''不存在的值不会报错'''
s.discard(20)
print(s)
## 从 a 中去除所有 b 的值
a = {1, 2, 3, 4, 5}
b = {2, 3 ,4}
a.difference_update(b)
print(a)