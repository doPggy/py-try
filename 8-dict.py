# 基操
## 生成
a = {}
print(a)
a = dict()
print(a)


## 插入键值
a = {}
a["one"] = "1"
a["two"] = "2"
a[3] = "3"
print(a)
## 查看键值
print(a["one"])
## 更新键值
a["one"] = 11
## 无顺序
print(a)
print(a)

# 键值需要不可变类型
synonyms = {}
synonyms['mutable'] = ['changeable', 'variable', 'varying', 'fluctuating',
                       'shifting', 'inconsistent', 'unpredictable', 'inconstant',
                       'fickle', 'uneven', 'unstable', 'protean']
synonyms['immutable'] = ['fixed', 'set', 'rigid', 'inflexible', 
                         'permanent', 'established', 'carved in stone']
print(synonyms)
# 初始化
d = {'1':1}
d = dict(
    [('1', 1),
    ('2', 2),
    ('3', 3)]
)
print(d)


# 字典方法
## get
a = {}
a['1'] = 1
'''这样不会抛出错误'''
print(a.get('2'))
print(a.get('2', 'nonononon'))
'''get 没有把默认数加到字典'''
print(a)
## pop
d = dict(
    [('1', 1),
    ('2', 2),
    ('3', 3)]
)
d.pop('2')
print(d)
print(d.pop('no', 'not exist'))
## del
del d["1"]
print(d)
## update
person = {}
person[1] = "1"
person[2] = "2"
person[3] = 3
person.update({1 : 11, 4 : "400"})
print(person)
## in
barn = {'cow':1, 'dog':5, 'cat':3}
print('c' in barn)
print('cow' in barn)
## keys values items
print(barn.keys())
print(barn.values())
print(barn.items())