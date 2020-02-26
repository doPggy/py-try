# 上下文管理
## with
'''with 可以调用上下文管理器'''
with open("my", "w") as fp:
    data = fp.write('hello')
    print(fp.__enter__)
    print(fp.__exit__)

## 自定义上下文管理器
'''
其实有点像装饰器包装代码，不过多了退出时的操作定义，
所以多用于资源的正确创建使用和释放
'''
class ContextMgr(object):
    def __enter__(self):
        print("enter")
    def __exit__(self, type, value, traceback):
        print("exit")

with ContextMgr():
    print("in")

## __enter__ 返回值
'''
不过通常返回管理器自己
'''
class ContextMgr(object):
    def __enter__(self):
        print("enter")
        return "my v"
    def __exit__(self, type, value, traceback):
        print("exit")

with ContextMgr() as c:
    print(c)

## 错误处理
class ContextMgr(object):
    def __enter__(self):
        print("enter")
        return "my v"
    def __exit__(self, type, value, traceback):
        print("exit", type, value, traceback)
        if  type is not None:
            print("exception ", value)
        '''可以不中断'''
        return True

with ContextMgr():
    print(1 / 0)