# 异常
import math

## 自定义异常
class myError(ValueError):
    pass

## 基本用法
while True:
    try:
        text = input('> ')
        if text[0] == 'q':
            break
        elif text[0] == 'e':
            raise myError("123123123123123")
        x = float(text)
        y = math.log10(x)
        print(x, y)
## 捕捉不同的错误
    except myError:
        print("??")
    except ValueError as exc:
        print("value > 0!")
    except ZeroDivisionError:
        print("not 1")
    except Exception:
        print("unexcept")
    # '''不论报错与否，都会走这里，而且有报错没捕获，会先执行'''
    # 有捕获，就最后执行
    finally:
        print("hhhhhh")

