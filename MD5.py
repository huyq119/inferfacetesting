#coding=utf-8
import hashlib
import types
def md5(str):
    if type(str) is types.StringType:
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()
    else:
        return "ERROR"
textinput = raw_input("请输入要加密的内容（勿忘输入密匙）：")
d = md5(textinput)
print textinput + " " + "加密结果为：" + d
f = open('md5code.txt','a+')
f.write("\n" + textinput + " " + "加密结果为：" + d)
f.close()