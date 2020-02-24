# 与操作系统交互
import os

## 文件路径操作
print(os.getcwd())
'''当前目录符号'''
print(os.curdir)
'''当前目录下的文件'''
print(os.listdir(os.curdir))

f = open("t", "w")
f.close()
os.rename("t", "t.new")
print("t" in os.listdir(os.curdir))
print("t.new" in os.listdir(os.curdir))
os.remove("t.new")

## 系统常量
'''换行符'''
print(os.linesep)
'''路径分隔符'''
print(os.sep)
'''环境变量中分隔符'''
print(os.pathsep)


## os.path
print(os.path.join("1", "333", "ffjfjfj"))