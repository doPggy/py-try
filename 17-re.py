# re 模块，正则
import re

str     = 'hello world'
pattern = 'hello (\w+)'
match = re.match(pattern, str)
print(match.group(0))
print(match.group(1))
## compile
'''pattern 需要重复使用'''
pattern1 = re.compile('hello (\w+)')
match = pattern1.match(str)
'''
group(0) 返回匹配整个的内容
group(1 .. n) 返回规则中每个括号匹配的部分
'''
print(match.group(0))
print(match.group(1))