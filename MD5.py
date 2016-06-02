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
d = md5("1001001iOS,9.3.2,1280*1080cn.com.chinau.homepage0.5C3BofasVsQlfaj4R8KuPw7Jc")
print d
f = file('md5code.txt','r+')
f.write(d)
f.close()