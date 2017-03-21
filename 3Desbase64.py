#coding=utf-8

from pyDes import *
import base64

data = raw_input("请输入要加密的内容：")
k = triple_des("C3BofasVsQlfaj4R8KuPw7Jc",padmode=PAD_PKCS5)
d = k.encrypt(data)
print "3Des Encrypted: %r" % d
f = base64.b64encode(d)
print "最终加密结果是：%s" % f

j = open("3Desbase64.txt", 'a+')
j.write("\n"+"最终加密结果是:" + f)
j.close()