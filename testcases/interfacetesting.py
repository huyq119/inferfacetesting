#coding=utf-8

import requests
import xlsxwriter

response_homepage = requests.post("http://test.chinau.com.cn:8090/app/gateway.do?app_key=1001001&service_type=cn.com.chinau.homepage&version=0.5&phone_info=iOS%2C9.3.2%2C1280*1080&sign=3e681b94e19a9f544958c9995fa4e955")
response_goodsmarketlist = requests.post("http://test.chinau.com.cn:8090/app/gateway.do?app_key=1001001&service_type=cn.com.chinau.goods.marketlist.query&version=0.5&phone_info=iOS%2C9.3.2%2C1280*1080&current_index=0&offset=1&order_by=XL&sort_by=A&sign=a32d3f9c89353c9a5266cafe8f228c9f")
response_goodsmarket = requests.post("http://test.chinau.com.cn:8090/app/gateway.do?app_key=1001001&service_type=cn.com.chinau.goods.market.query&version=0.5&phone_info=iOS%2C9.3.2%2C1280*1080&goods_sn=201605261001&sign=5a5472cd8d9b7ae5458a19d4b7e1a779")
httpstatus_homepage = response_homepage.status_code
httpstatus_goodsmarketlist = response_goodsmarketlist.status_code
httpstatus_goodsmarket = response_goodsmarket.status_code
workbook = xlsxwriter.Workbook('testresult.xlsx')
worksheet = workbook.add_worksheet()
if httpstatus_homepage == 200:
    text_homepage = response_homepage.json()
    if text_homepage["rsp_msg"] == u"成功":
        jsontext =  [[u"首页接口", text_homepage["rsp_msg"]]]
    else :
        jsontext = [[u"首页接口", u"失败："+text_homepage["rsp_msg"]]]
else:
    jsontext = [[u"首页接口",u"失败"+httpstatus_homepage]]
if httpstatus_goodsmarket == 200:
    text_goodsmarket =  response_goodsmarket.json()
    if text_goodsmarket["rsp_msg"] == u"成功":
        jsontext = jsontext + [[u"商品行情列表",text_goodsmarket["rsp_msg"]]]
    else :
        jsontext = jsontext + [[u"商品行情列表",u"失败："+text_goodsmarket["rsp_msg"]]]
else:
    jsontext = jsontext + [[u"商品行情列表",u"失败："+httpstatus_goodsmarket]]
if httpstatus_goodsmarketlist == 200:
    text_goodsmarketlist = response_goodsmarketlist.json()


print jsontext
row = 0
col = 0
for [item, cost] in jsontext:
    worksheet.write(row, col, item)
    worksheet.write(row, col + 1, cost)
    row += 1
workbook.close()


