# 单引双引号都可以创建字符串
s = "hello world"
print(s)
s = 'hello, world'
print(s)

# 简单操作
## 加法
s = 'h' + 'w'
print(s)
## 与数字相乘
print("echo" * 3)

# 字符串方法
## 分割
line = "1 2 3 \t 4 5"
print(line.split())
line = '1, 2, 3, 4, 5'
print(line.split(','))
## 连接
s = ','
'''以 s 为连接符连接成一个字符串'''
ss = s.join(['1', '2', '3']) # char list
print(ss)
## 替换
s = "hello world"
'''s.replace(p1, p2), 将 s 的 p1 部分换成 p2。'''
ss = s.replace('world', '111')
print(ss)
## 大小写转化
print('hello'.upper())
print('HELLO'.lower())
## 去除多余空白字符
s = "            he\t\n   "
print(s.strip())
print(s.lstrip())
print(s.rstrip())
## 查看更多成员方法
print(dir(s))

# 使用 \ 来换行
"""最后一行不用加 '\'"""
a = "hellll" \
    "1111" \
    "my name"
print(a)

# 强制转化为 str
print(str(1.1 + 2.2))
print(repr(1.1 + 2.2))

# 整数 -> 不同进制 str
'''to 16 进制'''
print(hex(255))
'''to 8 进制'''
print(oct(255))
'''to 2 进制'''
print(bin(255))

# str -> int
print(int('23'))
'''指定进制'''
print(int('FF', 16))
print(int('377', 8))
print(int('11111111111', 2))

# str -> float
print(float('4.55'))

# 格式化字符串
print('{} {} {}'.format('a', 'b', 'c'))
## 指定参数位置
print('{2} {1} {0}'.format('a', 'b', 'c'))
## 指定参数名称
print('{color} {0} {x} {1}'.format(10, 'foo', x = 1.5, color = 'blue'))
## 占位符
'''类似 c 的 printf'''
print('{color:10} {0:10d} {x} {1}'.format(10, 'foo', x = 1.5, color = 'blue'))