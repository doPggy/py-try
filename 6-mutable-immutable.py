# 列表可变
a = [1, 2, 3, 4]
a[0] = 100
a.insert(3, 200)
a.sort()

# 字符串不可变
'''利用索引修改会报错'''
## 修改字符串方法
s = "hello wordl"
s = s.replace('wordl', 'world')
print(s)

'''
s = bytearray('abcd')
s[1:3] = '12'
print(s)
'''