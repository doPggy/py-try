# 索引
'''对一个有序序列就可以利用 [] 来索引，list,str,tuple 等等'''
## 正向索引
s = "hello?"
print(s[0])
''' 索引从 0 起算, 这个主要从计算两个索引间长度来考虑的'''
print(s[4])
## 反向索引
print(s[-1])
print(s[-2])


# 分片
'''
var[begin:end:step]
[begin, end)
'''
s = 'hello world'
print(s[1:3])
print(s[1:-2])
print(s[:3])
'''包含结尾'''
print(s[-3:])
## 加上 step
print(s[::2])
'''step 为负数，从反方向开始切片'''
print(s[::-1])
print(s[::-2])
'''以 begin 开头，向着 end 去切片，所以 begin 要 >= end'''
print(s[4:1:-2])
