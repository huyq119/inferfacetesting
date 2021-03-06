import requests
import hashlib
import types
import json
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
'''import smtplib'''
import time
from yattag import Doc

f=open("testresult.txt","w")
def md5(str):
    if type(str) is types.:
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()
    else:
        return "ERROR"
def sign_get(str):
    items = str.items()
    items = list(items)
    items.sort()
    array_items = ""
    for key, value in items:
        array_items = array_items + value
    array_items=array_items.strip()
    sign = md5(array_items + "C3BofasVsQlfaj4R8KuPw7Jc")
    return  sign
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

url = "http://test.chinau.com.cn:8090/app/gateway.do"
querystring_homepage = {"app_key":"1001001","service_type":"cn.com.chinau.homepage","version":"1.1","phone_info":"Android,5.0,1920*1080" \
    ,"current_index":"0","offset":"20","imei":"A00000457A3E85"}
querystring_homepage["sign"] = sign_get(querystring_homepage)
response_homepage = requests.request("POST", url, params=querystring_homepage)
response_homepage_result = json.loads(response_homepage.text)
if response_homepage_result["rsp_code"] == "0000":
    result_homepage = u"首页接口测试成功: " +  response_homepage.text
else:
    result_homepage = u"首页接口测试失败" + response_homepage.text
print (result_homepage)

querystring_login = {"app_key":"1001001","service_type":"cn.com.chinau.user.login.register","version":"1.1","phone_info":"iOS,10.2,1280*1080" \
    ,"mobile":"13366040193","password":"MkxMSS3iZy8=","op_type":"DL"}
querystring_login["sign"] = sign_get(querystring_login)
response = requests.request("POST", url, params=querystring_login)
response_login = json.loads(response.text)
if response_login["rsp_code"] == "0000":
    result_login = u"登录接口测试成功: " +  response.text
else:
    result_login = u"登录接口测试失败" + response.text
print (result_login)
userid = response_login["userId"]
usertoken = response_login["token"]

querystring_refund_TK = {"app_key":"1001001", "service_type":"cn.com.chinau.order.refund", "version":"1.1", "phone_info":"iOS,10.2,1280*1080",\
                         "user_id":"204", "token":"aab9c9b5-85e6-49fd-a62e-34dafbf5b373", "refund_type":"TK", "order_sn":"Req00002099O",\
                         "goods_sn":"221523279215"}
querystring_refund_TK["user_id"] = userid.encode("utf-8")
querystring_refund_TK["token"] = usertoken.encode("utf-8")
querystring_refund_TK["sign"] = sign_get(querystring_refund_TK)
querystring_refund_TK["detail"] = "Req00002068N"
response_refund_TK = requests.request("POST",url,params=querystring_refund_TK)
response_refund_TK_json = json.loads(response_refund_TK.text)
if response_refund_TK_json["rsp_code"] == "0000":
    result_refund_TK = u"未发货退款接口测试成功: " +  response_refund_TK.text
else:
    result_refund_TK = u"未发货退款接口测试失败" + response_refund_TK.text
print (result_refund_TK)

'''querystring_refund_TH = {"app_key":"1001001", "service_type":"cn.com.chinau.order.refund", "version":"1.1", "phone_info":"iOS,10.2,1280*1080",\
                         "user_id":"204", "token":"aab9c9b5-85e6-49fd-a62e-34dafbf5b373", "refund_type":"TH", "order_sn":"Req00002074N",\
                         "goods_sn":"271772076215","express_comp":"sf","express_no":"2323232232"}
querystring_refund_TH["user_id"] = userid.encode("utf-8")
querystring_refund_TH["token"] = usertoken.encode("utf-8")
querystring_refund_TH["sign"] = sign_get(querystring_refund_TH)
querystring_refund_TH["detail"] = "Req00002068N"
response_refund_TH = requests.request("POST",url,params=querystring_refund_TH)
response_refund_TH_json = json.loads(response_refund_TH.text)
if response_refund_TH_json["rsp_code"] == "0000":
    result_refund_TH = u"已发货退款接口测试成功: " +  response_refund_TH.text
else:
    result_refund_TH = u"已发货退款接口测试失败" + response_refund_TH.text
print (result_refund_TH)

querystring_refund_PTJR = {"app_key":"1001001", "service_type":"cn.com.chinau.order.refund", "version":"1.1", "phone_info":"iOS,10.2,1280*1080",\
                         "user_id":"204", "token":"aab9c9b5-85e6-49fd-a62e-34dafbf5b373", "refund_type":"PTJR", "order_sn":"Req00002068N",\
                         "goods_sn":"271772076215"}
querystring_refund_PTJR["user_id"] = userid.encode("utf-8")
querystring_refund_PTJR["token"] = usertoken.encode("utf-8")
querystring_refund_PTJR["sign"] = sign_get(querystring_refund_PTJR)
querystring_refund_PTJR["detail"] = "Req00002068N"
response_refund_PTJR = requests.request("POST",url,params=querystring_refund_PTJR)
response_refund_PTJR_json = json.loads(response_refund_PTJR.text)
if response_refund_PTJR_json["rsp_code"] == "0000":
    result_refund_PTJR = u"退款申请平台介入接口测试成功: " +  response_refund_PTJR.text
else:
    result_refund_PTJR = u"退款申请平台介入接口测试失败" + response_refund_PTJR.text
print (result_refund_PTJR)

querystring_refund_detail = {"app_key":"1001001", "service_type":"cn.com.chinau.refund.detail.query", "version":"1.1", "phone_info":"iOS,10.2,1280*1080",\
                         "user_id":"204", "token":"aab9c9b5-85e6-49fd-a62e-34dafbf5b373", "order_sn":"Req00002074N"}
querystring_refund_detail["user_id"] = userid.encode("utf-8")
querystring_refund_detail["token"] = usertoken.encode("utf-8")
querystring_refund_detail["sign"] = sign_get(querystring_refund_detail)
response_refund_detail = requests.request("POST",url,params=querystring_refund_detail)
response_refund_detail_json = json.loads(response_refund_detail.text)
if response_refund_detail_json["rsp_code"] == "0000":
    result_refund_detail = u"查看退款详情页接口测试成功: " +  response_refund_detail.text
else:
    result_refund_detail = u"查看退款详情页接口测试失败" + response_refund_detail.text
print (result_refund_detail)'''

# 输入Email地址和口令:
from_addr = "huyuqi@chinau.cc"
password = "huyuqi119+1"
# 输入SMTP服务器地址:
smtp_server = "smtp.ym.163.com"
# 输入收件人地址:
to_addr = "54234133@qq.com"

doc, tag, text = Doc().tagtext()

""" The "doc, tag, text = Doc().tagtext()" line is thus equivalent to the longer code:
 doc = Doc()
 tag = doc.tag
 text = doc.text """

'''with tag('html'):
    with tag('body'):
        with tag('p', id = 'main'):
            text(result_login+"\r\n")
        with tag('p', id='sub1'):
            text(result_refund_TK + "\r\n")
        with tag('p',id='sub2'):
            text(result_refund_TH+"\r\n")
        with tag('p',id='sub3'):
            text(result_refund_PTJR+"\r\n")
        with tag('p',id='sub4'):
            text(result_refund_detail+"\r\n")
        with tag('a', href='http://192.168.51.32:8060/user-login-Lw==.html'):
            text(u'展示结果')
result = doc.getvalue()

msg = MIMEText(result,"html","utf-8")
msg['From'] = _format_addr(u'APP测试 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
text_subject = u"退款接口测试报告 " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
msg['Subject'] = Header(text_subject, 'utf-8').encode()'''


'''server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()'''
