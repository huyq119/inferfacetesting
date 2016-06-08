#coding=utf-8

import requests
import xlsxwriter

response = requests.post("http://124.205.39.212:8090/app/gateway.do?app_key=1001001&service_type=cn.com.chinau.homepage&version=0.5&phone_info=iOS%2C9.3.2%2C1280*1080&sign=3e681b94e19a9f544958c9995fa4e955")
httpstatus = response.status_code
if httpstatus == 200:
    text = response.json()
    workbook = xlsxwriter.Workbook('homepage_result.xlsx')
    worksheet = workbook.add_worksheet()
    assert text["rsp_msg"] == u"成功"
    if text["rsp_msg"] == u"成功":
        jsontext = [["rsp_code", text["rsp_code"]], ["timestamp", text["timestamp"]], ["sign", text["sign"]],
                    ["buyback_scan", text["buyback_scan"]], ["rsp_msg", text["rsp_msg"]],
                    ["banners", text["banners"]]]
        a = []
        b = []
        i = 0
        for i in range(len(text["buyback_order_list"])):
            a += list(text["buyback_order_list"][i])
            b += list(text["buyback_order_list"][i].values())
            i += 1
        j = 0
        for j in range(len(a)):
            jsontext.append([a[j], b[j]])
            j += 1
        row = 0
        col = 0
        for [item, cost] in jsontext:
            worksheet.write(row, col, item)
            worksheet.write(row, col + 1, cost)
            row += 1
        workbook.close()
    else:
        print text["rsp_msg"]
else:
    print httpstatus




