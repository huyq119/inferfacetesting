import requests

url = "http://test.chinau.com.cn:8090/app/gateway.do"

querystring = {"app_key":"1001001","service_type":"cn.com.chinau.shopcart.modify","version":"1.0","phone_info":"iOS,10.2,1280*1080","user_id":"204","token":"ea7e5239-897e-49ac-a3fe-78e8c630e3aa","goods_info":"[{\"goods_sn\":\"241516965249\",\"goods_count\":\"1\"}]","op_type":"JR","sign":"83f3a1ddc62d5921036702f22493c894"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "8e93831c-f3dd-f9b2-3109-34274d33d12b"
    }

response = requests.request("POST", url, headers=headers, params=querystring)

print(response.text)