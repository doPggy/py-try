# sys 模块简介
import sys
## 命令行参数
'''python3 ./15-sys.py'''
print(sys.argv)

## 异常消息
try:
    x = 1 / 0
except Exception:
    print(sys.exc_info())

## python 搜索模块的路径和查找顺序
print(sys.path)