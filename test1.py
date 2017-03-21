import requests

url = "http://192.168.1.84:8090/app/gateway.do"

querystring = {"app_key":"1001001","service_type":"cn.com.chinau.nation.query","version":"1.0","phone_info":"iOS9.3.31136*640","sign":"34ebe237eaacbe1e4caa1fb86a33ceed"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "314d52c8-41ff-6cdc-df59-a9d74cec37d9"
    }

response = requests.request("POST", url, headers=headers, params=querystring)

print(response.text)