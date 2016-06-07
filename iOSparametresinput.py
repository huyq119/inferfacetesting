#coding=utf-8

app_key = "1001001"
version = "0.5"
phone_info = "iOS,9.3.1,1280*1080"
scan_code = "chinau.com"
mobile = "13366040193"
password = "MkxMSS3iZy8="
sms_code = "000000"
is_agree = "1"

secret_key = "C3BofasVsQlfaj4R8KuPw7Jc"

service_type = raw_input("请输入 service_type:")

if service_type == "cn.com.chinau.homepage":
    signname = app_key+phone_info+service_type+version+secret_key
elif service_type == "cn.com.chinau.buyback.goods.query":
    signname = app_key+phone_info+scan_code+service_type+version+secret_key
elif service_type == "cn.com.chinau.user.login.register":
    op_type = raw_input("请输入选择登录还是注册（DL or ZC）：")
    if op_type == "DL":
        signname = app_key + mobile + op_type + password + phone_info + service_type + version + secret_key
    elif op_type == "ZC":
        signname = app_key + is_agree + mobile + op_type + password + phone_info + service_type + sms_code + version + secret_key
    else:
        print "Error"
elif service_type == "cn.com.chinau.buyback.confirm":




else :
    print "Error"
print signname

